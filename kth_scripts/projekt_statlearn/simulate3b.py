import os
import csv
import pandas as pd
from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt
from scipy.special import loggamma
from statinlprojekt import Theta_MoM_skattning, AlphaBeta_MoM_skattning, tricks_data, get_parameters_tricks, get_avg_alpha_beta_tricks
from simulate import xparams, print_dic
