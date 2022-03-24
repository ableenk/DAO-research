'''Execution file

'''
from visualize.graph_tools import ReputationVisualizer as RV

FILE_NAME = 'reps.txt'

def show_graph():
    '''Show graph with input data.
    
    '''
    rv = RV(FILE_NAME)
    rv.show_info()
    rv.show_analyze_graph()

if __name__ == '__main__':
    show_graph()
