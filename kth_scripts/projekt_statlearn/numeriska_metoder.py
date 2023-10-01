from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import pandas as pd
from scipy.special import psi


# def grad_logL(alpha: float,beta: float,data: np.array):
#     k = len(data)
#     partial_alpha = k*psi(alpha+beta) -k*psi(alpha) + sum(np.log(data))
#     partial_beta = k*psi(alpha+beta) - k*psi(beta) + sum(np.log(1-data))
#     result = np.array([partial_alpha,partial_beta])
#     return result

# def gradient_descent(data):
#     h = 10**-6
#     tau = 10**-6
#     error_term = 1
#     alpha_0 = np.mean(data)*((1-np.mean(data))/np.var(data,ddof=1)-1)
#     beta_0 = (1-np.mean(data))*((1-np.mean(data))/np.var(data,ddof=1)-1)
#     parameters = np.array([alpha_0,beta_0])
#     while error_term>tau:
#         print(parameters)
#         alpha = parameters[0]
#         beta = parameters[1]
#         parameters = parameters + h*grad_logL(alpha,beta,data)
#         error_term = np.linalg.norm(np.array([alpha,beta]-parameters))
#     return parameters


# import numpy as np
# from scipy.optimize import minimize
# from scipy.special import gammaln
# # Define the likelihood function for the Beta distribution
# def beta_likelihood(params, data):
#     alpha, beta = params
#     log_likelihood = gammaln(alpha + beta) - (gammaln(alpha) + gammaln(beta)) + np.sum((alpha - 1) * np.log(data) + (beta - 1) * np.log(1 - data))
#     return -log_likelihood  # We minimize the negative log-likelihood

# # Manually input your data as a list
# data = np.array([0.1, 0.2, 0.5, 0.5])

# # Initial guess for alpha and beta
# initial_guess = [5, 2]

# # Optimize the likelihood function to find MLE parameters
# result = minimize(beta_likelihood, initial_guess, args=(data,), method='L-BFGS-B')

# if result.success:
#     alpha_mle, beta_mle = result.x
#     print(f"MLE of alpha: {alpha_mle:.4f}")
#     print(f"MLE of beta: {beta_mle:.4f}")
# else:
#     print("MLE estimation failed. Check your data and initial guess.")
