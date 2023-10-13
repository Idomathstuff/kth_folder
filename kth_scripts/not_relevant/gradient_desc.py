# import numpy as np
# from scipy.special import polygamma, gammaln, psi
# global_svariance = 0.16403415647726363
# def Theta_MoM_skattning(xdata):
#     data = xdata>0.0
#     return np.mean(data)

# def AlphaBeta_MoM_skattning(xdata):
#     data = [x for x in xdata if x>0]
#     if len(data)==1:
#         svariance = global_svariance
#     else:
#         svariance = np.var(data,ddof=1)
#     # print(svariance)
#     svariance = global_svariance
#     alpha_0 = np.mean(data)*((1-np.mean(data))/svariance-1)
#     beta_0 = (1-np.mean(data))*((1-np.mean(data))/svariance-1)
#     return np.array([alpha_0,beta_0])   


# def grad_logL(alpha: float,beta: float,data: np.array):
#     k = len(data)
#     partial_alpha = k*psi(alpha+beta) -k*psi(alpha) + np.sum(np.log(data))
#     partial_beta = k*psi(alpha+beta) - k*psi(beta) + np.sum(np.log(1-data))
#     result = np.array([partial_alpha,partial_beta])
#     return result

# def beta_likelihood(alpha, beta, data):
#     log_likelihood = gammaln(alpha + beta) - (gammaln(alpha) + gammaln(beta)) + np.sum((alpha - 1) * np.log(data) + (beta - 1) * np.log(1 - data))
#     return log_likelihood

# def gradient_descent(data):
#     h = 0.01
#     tau = 10**-10
#     error_term = 1
#     alpha_0 =  AlphaBeta_MoM_skattning(data)[0]
#     beta_0 = AlphaBeta_MoM_skattning(data)[1]
#     parameters = np.array([alpha_0,beta_0])
#     while error_term>tau:
#         print(parameters, beta_likelihood(parameters[0],parameters[1],data))
#         alpha = parameters[0]
#         beta = parameters[1]
#         parameters = parameters + h*grad_logL(alpha,beta,data)
#         error_term = np.linalg.norm(np.array([alpha,beta]-parameters))
#     return parameters


# def get_parameters_descent():
#     tmpdic = {}
#     for name in ids:
#         theta = Theta_MoM_skattning(np.array(tricks_data[name]))
#         alpha = gradient_descent(np.array(tricks_data[name]))[0]
#         beta = gradient_descent(np.array(tricks_data[name]))[1]
#         tmpdic[name] = [theta,alpha,beta]
#         # print(name,"done")
#     return tmpdic