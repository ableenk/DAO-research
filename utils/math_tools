'''Math tools for reputation analyze

'''

import numpy as np

def get_gini_coefficient(reputations: np.array, accuracy=3) -> float:
    '''Get gini coefficient of owner decentralization system.

    Args:
        reputations (np.array): list of all reputation distribution
        accuracy (int): how many digits after point

    Return:
        number (float): gini coefficient of the current system

    '''
    reputations = np.sort(reputations)
    count = reputations.shape[0]
    amount = reputations.sum()
    rep_cumsum = np.cumsum(reputations)
    height = count**-1
    all_bases = rep_cumsum / amount
    area_under_lorenz_curve = height * (all_bases.sum() - all_bases[-1]/2)
    return round(1 - 2*area_under_lorenz_curve, accuracy)

def get_nakamoto_score_and_coefficient(reputations: np.array, accuracy=3) -> tuple:
    '''Get gini coefficient of owner decentralization system.

    Args:
        reputations (np.array): list of all reputation distribution
        accuracy (int): how many digits after point

    Return:
        tuple (float, int): nakamoto coefficient and score of the current system

    '''
    reputations = np.sort(reputations)
    reversed_cumsum = np.cumsum(reputations[::-1])
    count = reputations.shape[0]
    amount = reputations.sum()
    score = ((reversed_cumsum * 2 - amount) < 0).sum() + 1
    coefficient = round(score / count, accuracy)
    return coefficient, score

def get_lorenz_curve_data(reputations: np.array) -> tuple:
    '''Calculate data for lorenz curve plot.

    Args:
        reputations (np.array): list of all reputation distribution

    Return:
        (float, float): dots coordinates corresponding to lorenz_curve

    '''
    reputations = np.sort(reputations)
    cumsum = np.cumsum(reputations)
    count = reputations.shape[0]
    amount = reputations.sum()
    x_axis = np.arange(count + 1) / count
    y_axis = np.concatenate(([0], cumsum / amount))
    return (x_axis, y_axis)
