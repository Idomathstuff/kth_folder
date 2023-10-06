
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import pandas as pd
from scipy.special import gamma, loggamma

data = np.array([0.16, 0.32, 0.15, 0.27, 0.3, 0.16, 0.36, 0.41, 0.48, 0.28])

def log_prior(alpha, beta):
    return np.log(1**3) - loggamma(3) + (3 - 1)*np.log(alpha + beta + 1) - 1*(alpha + beta + 1) - np.log(alpha + beta)

def log_posterior(alpha, beta):
    log_p = log_prior(alpha, beta)
    for x in data:
        log_p += loggamma(alpha + beta) - loggamma(alpha) - loggamma(beta)
        log_p += (alpha - 1)*np.log(x) + (beta - 1)*np.log(1 - x)
    return log_p

def make_contour_plot():
    alpha_grid = np.linspace(0.1, 10, 100)
    beta_grid = np.linspace(0.1, 10, 100)
    log_posterior_grid = [[log_posterior(alpha, beta)
                        for alpha in alpha_grid] for beta in beta_grid]
    posterior_grid = np.exp(log_posterior_grid - np.max(log_posterior_grid))
    plt.figure(figsize=(10, 6))
    plt.contour(alpha_grid, beta_grid, posterior_grid)
    plt.xlabel(r"$\alpha$", fontsize=12)
    plt.ylabel(r"$\beta$", fontsize=12)
    plt.show()

def method_moments(list):
    m1 = np.mean(list)
    m2 = np.mean([x**2 for x in list])
    alpha = (m1*(m1-m2))/(m2-m1**2)
    beta = ((m1-m2)*(1-m1))/(m2-m1**2)
    return([alpha,beta])

def metropolis():
    def genY(X):
        X = np.array(X)
        proposal_alpha = np.exp(np.log(X[0]) + delta * stats.norm.rvs())
        proposal_beta = np.exp(np.log(X[1]) + delta * stats.norm.rvs())
        return np.array([proposal_alpha,proposal_beta])

    n_samples = int(1e4)
    n_chains = 1
    delta = 0.5
    alphas = np.zeros((n_samples, n_chains))
    betas = np.zeros((n_samples, n_chains))
    
    init_guess = method_moments(data)

    # initial values are randomly shifted for the other chains
    alphas[0] = init_guess[0] + np.exp(stats.cauchy.rvs(size=n_chains, scale=0.05)) 
    betas[0] = init_guess[1] + np.exp(stats.cauchy.rvs(size=n_chains, scale=0.05))

    for i in range(n_samples - 1):
        for j in range(n_chains):
            last_alpha = alphas[i, j]
            last_beta = betas[i, j]

            Y = genY([last_alpha,last_beta])
            proposal_alpha = Y[0]
            proposal_beta = Y[1]

            rho = np.exp(log_posterior(proposal_alpha, proposal_beta)) / np.exp(log_posterior(last_alpha, last_beta)) # f(Y)/f(Xi-1)
            u = stats.uniform.rvs()
            if u <= rho:
                alphas[i + 1, j] = proposal_alpha
                betas[i + 1, j] = proposal_beta
            else:
                alphas[i + 1, j] = last_alpha
                betas[i + 1, j] = last_beta
    
    for j in range(n_chains):
        plt.plot(alphas[:, j], betas[:, j], '.-', markersize=10, alpha=0.5)

    plt.xlabel('alpha', fontsize=12)
    plt.ylabel('beta', fontsize=12)
    plt.show()

metropolis()
