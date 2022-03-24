'''Class for graphing DAO data.

'''

import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

sys.path.append('../')

import utils.math_tools as formules    

class ReputationVisualizer():
    '''Utility for analyzing different DAO cases.

    '''
    def __init__(self, file_name, numbers_accuracy=3, rep_sample=None, from_file=True):
        self.accuracy = numbers_accuracy
        self.gini_coefficient = 0
        self.nakamoto_coefficient = 0
        self.nakamoto_score = 0
        if from_file:
            self.init_rep_info(file_name)
        else:
            self.rep_array = rep_sample
        self.count_all()

    def init_rep_info(self, file_name: str):
        '''Get reputation distribution data from input file.

        Args:
            string (str): name of file with current reputation distribution

        '''
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.rep_array = np.array([])
            for line in lines:
                self.rep_array = np.append(self.rep_array, float(line[:-2]))
            file.close()

    def count_all(self):
        '''Count whole data with current reputation.

        '''
        self.rep_array = np.sort(self.rep_array)
        self.number_of_participants = self.rep_array.shape[0]
        self.reputation_amount = self.rep_array.sum()
        self.reputation_cumsum = np.cumsum(self.rep_array)
        gini_c = formules.get_gini_coefficient(self.rep_array)
        coefficient, score= formules.get_nakamoto_score_and_coefficient(self.rep_array)
        self.gini_coefficient = gini_c
        self.nakamoto_coefficient = coefficient
        self.nakamoto_score = score

    def show_analyze_graph(self, title='OWNER DECENTRALIZATION'):
        '''Show graph for current reputation case.

        Kwargs:
            string (str): title of graph

        '''
        x_axis, y_axis = formules.get_lorenz_curve_data(self.rep_array)
        x_info, y_info = 'part of DAO', 'part of reputation amount'
        lorenz_curve_data = pd.DataFrame({x_info: x_axis, y_info: y_axis})
        equality_line_data = pd.DataFrame({x_info: x_axis, y_info: x_axis})
        coefficients_values = [self.gini_coefficient, self.nakamoto_coefficient]
        constants_data = {"coefficient": ["Gini", "Nakamoto"], "value": coefficients_values}
        constants_barplot_data = pd.DataFrame(constants_data)
        sns.set_theme(style="darkgrid")
        sns.color_palette('pastel')
        _, plots = plt.subplots(1, 2, figsize=(12, 6))
        sns.lineplot(x=x_info, y=y_info, data=lorenz_curve_data,
            color='g', ax=plots[0]).set_title(title)
        sns.lineplot(x=x_info, y=y_info, data=equality_line_data,
            color='b', ax=plots[0])
        plots[0].axvline(1-self.nakamoto_coefficient, 0.05, 0.95, color='r', linestyle='--')
        plots[0].scatter(x=1-self.nakamoto_coefficient, y=0, color='r')
        plots[0].scatter(x=1, y=0, color='r')
        plots[0].legend(labels=["lorenz curve", "equality line", '51 percent',
            f'nakamoto_coefficient({self.nakamoto_coefficient})'])
        sns.barplot(data=constants_barplot_data, x='coefficient', y='value',
            ax=plots[1]).set_yticks(np.arange(0, 11) / 10)
        plots[1].axis(ymin=0,ymax=1)
        plots[1].legend(labels=[f'{self.gini_coefficient}', f'{self.nakamoto_coefficient}'])
        plt.show()

    def show_info(self):
        '''Print current constants data.

        '''
        print(f'Nakamoto coefficient is {self.nakamoto_coefficient}')
        print(f'Nakamoto score is {self.nakamoto_score}')
        print(f'Gini coefficient is {self.gini_coefficient}')
