from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import pandas as pd
from scipy.special import psi
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
ids = list(set(ndf['id']))
# print(len(ids))

def make_histogram():
    # fig, ax = plt.subplots(1, 1)
    plt.hist(ndf["trick 1"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 1")
    plt.hist(ndf["trick 2"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 2")
    plt.hist(ndf["trick 3"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 3")
    plt.hist(ndf["trick 4"], density=True, histtype='stepfilled', alpha=0.5, label = "Trick 4")
    plt.legend()
    plt.show()


def make_histogram_runs():
    # fig, ax = plt.subplots(1, 1)
    plt.hist(ndf["run 1"], density=True,
             histtype='stepfilled', alpha=0.5, label="run 1")
    plt.hist(ndf["run 2"], density=True,
             histtype='stepfilled', alpha=0.5, label="run 2")
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

# make_histogram_runs()
# print(calculate_Q1_partd())
# plot_run1_run2()

Lcq_ids = ["Majerus", "Oliveira","Decenzo","Santiago", "Papa", "Eaton", "Mota", "Shirai", "Jordan", "Hoefler", "Hoban", "Gustavo", "Ribeiro C", "O’neill", "Foy", "Midler"]

def var(data):
    data = np.array(data)
    mean = np.mean(data)
    n = len(data)
    return sum((data-mean)**2)/(n-1)
def Theta_MoM_skattning(xdata):
    data = xdata>0.0
    return np.mean(data)

def AlphaBeta_MoM_skattning(xdata):
    data = [x for x in xdata if x>0]
    alpha_0 = np.mean(data)*((1-np.mean(data))/np.var(data,ddof=1)-1)
    beta_0 = (1-np.mean(data))*((1-np.mean(data))/np.var(data,ddof=1)-1)
    return np.array([alpha_0,beta_0])   


def init_trick_data():
    ndf.set_index('id',inplace=True)
    # print(ndf.loc['Gustavo'])
    tricks_data = {}
    n = len(ndf)
    for name in list(ids):
        # print(name)
        namesdata = ndf.loc[name]
        if isinstance(namesdata['trick 1'],float):
            tricks_data[name] = np.array([namesdata['trick 1']]+[namesdata['trick 2']]+[namesdata['trick 3']]+[namesdata['trick 4']])
        else:
            tricks_data[name] = np.array(list(namesdata['trick 1'])+list(namesdata['trick 2'])+list(namesdata['trick 3'])+list(namesdata['trick 4']))
    return tricks_data


tricks_data = init_trick_data()

# print(tricks_data)
# for key,value in tricks_data.items():
#     value = [x for x in value if x>0]
#     if key in Lcq_ids:
#         # print(key,var(np.array(value)))
#         # print(key,np.mean(np.array(value)))
#         print(key,value)
#     # print(key,value)

def get_parameters():
    # tmpdic = {}
    params_frame = {'id': ids ,'theta':[0]*len(ids), 'alpha':[0]*len(ids),'beta':[0]*len(ids)}
    paramf = pd.DataFrame(params_frame)
    paramf.set_index('id',inplace=True)
    for name in tricks_data.keys():
        print(name)
        theta = Theta_MoM_skattning(np.array(tricks_data[name]))
        alpha = AlphaBeta_MoM_skattning(np.array(tricks_data[name]))
        # beta = AlphaBeta_MoM_skattning(np.array(tricks_data[name]))[1]
        # print(theta)
        # tmpdic[name] = [theta,alpha,beta]
    return paramf

def grad_logL(alpha: float,beta: float,data: np.array):
    k = len(data)
    partial_alpha = k*psi(alpha+beta) -k*psi(alpha) + sum(np.log(data))
    partial_beta = k*psi(alpha+beta) - k*psi(beta) + sum(np.log(1-data))
    result = np.array([partial_alpha,partial_beta])
    return result

def gradient_descent(data):
    h = 0.001
    tau = 10**-10
    error_term = 1
    alpha_0 = np.mean(data)*((1-np.mean(data))/np.var(data,ddof=1)-1)
    beta_0 = (1-np.mean(data))*((1-np.mean(data))/np.var(data,ddof=1)-1)
    parameters = np.array([alpha_0,beta_0])
    while error_term>tau:
        print(parameters)
        alpha = parameters[0]
        beta = parameters[1]
        parameters = parameters + h*grad_logL(alpha,beta,data)
        error_term = np.linalg.norm(np.array([alpha,beta]-parameters))
    return parameters

print(gradient_descent(np.array([0.1,0.2,0.5,0.5])))