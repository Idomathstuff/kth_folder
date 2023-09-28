from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import pandas as pd
import csv
# pdf = lambda x: 2*np.exp(-2*x);
# Finv = lambda u: -(1/2)*np.log(u)
df = pd.read_csv("SLS22.csv") #data frame

def init_normal_dataframe():
    ndf = df
    ndf["run 1"] = [x/10 for x in df["run 1"]]
    ndf["run 2"] = [x/10 for x in df["run 2"]]
    ndf["trick 1"] = [x/10 for x in df["trick 1"]]
    ndf["trick 2"] = [x/10 for x in df["trick 2"]]
    ndf["trick 3"] = [x/10 for x in df["trick 3"]]
    ndf["trick 4"] = [x/10 for x in df["trick 4"]]
    ndf["trick 5"] = [x/10 for x in df["trick 5"]]
    ndf["trick 6"] = [x/10 for x in df["trick 6"]]
    ndf["make 1"] = [int(bool(x)) for x in df["trick 1"].values.tolist()]
    ndf["make 2"] = [int(bool(x)) for x in df["trick 2"].values.tolist()]
    ndf["make 3"] = [int(bool(x)) for x in df["trick 3"].values.tolist()]
    ndf["make 4"] = [int(bool(x)) for x in df["trick 4"].values.tolist()]
    return ndf
ndf = init_normal_dataframe()

def make_histogram():
    # fig, ax = plt.subplots(1, 1)
    plt.hist(ndf["trick 1"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 1")
    plt.hist(ndf["trick 2"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 2")
    plt.hist(ndf["trick 3"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 3")
    plt.hist(ndf["trick 4"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 4")
    plt.legend()
    plt.show()

def calculate_Q1_partd():
    count_lands = ndf["make 1"].values.tolist().count(1) + ndf["make 2"].values.tolist().count(1) +ndf["make 3"].values.tolist().count(1) + ndf["make 4"].values.tolist().count(1) 
    count_bigger_than6 = 0;
    alltricks = ndf["trick 1"].values.tolist() + ndf["trick 2"].values.tolist() + ndf["trick 3"].values.tolist() + ndf["trick 4"].values.tolist()
    for x in alltricks:
        if x>0.6:
            count_bigger_than6+=1
    return float(count_bigger_than6)/float(count_lands)


def plot_run1_run2():
    plt.scatter(ndf["run 1"],ndf["run 2"],color='blue', marker='o')
    plt.xlabel('run 1')
    plt.ylabel('run 2')
    plt.legend()
    plt.show()

# make_histogram()
# print(calculate_Q1_partd())
# plot_run1_run2()


tmpset = set(df["id"].values.tolist())
# tmpset.remove("Horigome")
# tmpset.remove('Joslin')
# tmpset.remove('Milou')
# tmpset.remove('Ribeiro G')

