from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statinlprojekt import get_parameters_tricks, get_parameters_runs, Lcq_ids, ids

def get_LCQ_params():
    resultx = get_parameters_tricks()
    resulty = get_parameters_runs()
    for e in ids:
        if e not in Lcq_ids:
            resultx.pop(e)
            resulty.pop(e)
    return resultx, resulty
def print_dic(dic):
    for keys,values in dic.items():
        print(keys,values)

xparams, yparams = get_LCQ_params()

