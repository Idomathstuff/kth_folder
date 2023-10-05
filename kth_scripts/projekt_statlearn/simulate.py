from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from statinlprojekt import get_parameters_tricks, get_parameters_runs, Lcq_ids, ids

Lcq_ids_index = {Lcq_ids[e]:e for e in range(len(Lcq_ids))}
# print(Lcq_ids_index)
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


def sort_with_indices(arr):
    indexed_arr = list(enumerate(arr))
    sorted_arr = sorted(indexed_arr, key=lambda x: x[1])
    indices = [index for index, _ in sorted_arr]
    return indices

def total_betyg(tricks, runs):
    sorted_trick = sorted(tricks)
    return (sorted_trick[-2]+sorted_trick[-1]) + max(runs)


def sim_trick_betyg(theta,alpha,beta):
    V = np.array(
        np.random.choice([0,1], 4, p = [1-theta,theta]))
    Z = np.array(
        np.random.beta(alpha,beta,4))
    X = [0,0,0,0]
    for i in range(len(X)):
        X[i] = Z[i]*V[i]
    return X

def get_rand_LCQ(): # returns an array of n LCQs. An LCQ is an array representing 
    new_LCQ = [0]*16
    for name in Lcq_ids:
        x_theta,x_alpha,x_beta = xparams[name][0],xparams[name][1],xparams[name][2]
        y_alpha,y_beta = yparams[name][0],yparams[name][1]
        skaters_tricks = sim_trick_betyg(x_theta,x_alpha,x_beta)
        skaters_runs = np.random.beta(y_alpha,y_beta,2)
        new_LCQ[Lcq_ids_index[name]] = total_betyg(
            skaters_tricks, skaters_runs)
    return new_LCQ

def get_rand_finalists():
    sorted_players = sort_with_indices(get_rand_LCQ())
    return [sorted_players[-4],sorted_players[-3],sorted_players[-2],sorted_players[-1]]

def get_rand_finalists_array(n):
    W_array = []
    for i in range(n):
        W = get_rand_finalists()
        W_array.append(W)
    return W_array


def most_common_array(arrays):
    tuple_arrays = [tuple(inner_list) for inner_list in arrays]
    array_counts = Counter(tuple_arrays)
    most_common_tuple, count = array_counts.most_common(1)[0]
    # Convert the tuple back 
    most_common_array = list(most_common_tuple)
    return most_common_array, count

def make_finalist_histogram():
    winner_count = [0] * 16
    winner_array = []
    y = []
    x_labels = []  
    for i in range(5000):
        new_W = get_rand_finalists()
        winner_array.append(new_W)
        for e in new_W:
            y.append(e)
            winner_count[e] += 1
    plt.hist(y, density=True, histtype='stepfilled',alpha=0.5, label="Trick 1")
    for lcq_id in Lcq_ids:
        x_labels.append(lcq_id)
    
    plt.xticks(range(len(x_labels)), x_labels, rotation=90)
    print(most_common_array(get_rand_finalists_array(5000)))

    plt.show()


# make_finalist_histogram()
