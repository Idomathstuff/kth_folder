
from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt
from scipy.special import gamma, loggamma

data = np.array([0.16, 0.32, 0, 0, 0, 0.16, 0.36, 0.41, 0.48, 0.28])

def log_datafördelning(data,theta, alpha,beta):
    log_beta_pdf = lambda x, alpha, beta: loggamma(alpha + beta) - loggamma(alpha) - loggamma(beta) + (alpha - 1)*np.log(x) + (beta - 1)*np.log(1 - x)
    DF = 0
    for x in data:
        if x==0:
            DF+= np.log(1-theta)
        else:
            DF+= log_beta_pdf(x,alpha,beta) + np.log(theta)
    return DF

def log_prior(alpha, beta):
    lambd = 0.001
    thet = 5
    return np.log(thet**lambd) - loggamma(thet) + (thet - 1)*np.log(alpha + beta + 1) - lambd*(alpha + beta + 1) - np.log(alpha + beta)

def log_posterior(data,alpha, beta):
    theta = 0.0001
    log_p = log_prior(alpha, beta)
    # for x in data:
    #     log_p += loggamma(alpha + beta) - loggamma(alpha) - loggamma(beta)
    #     log_p += (alpha - 1)*np.log(x) + (beta - 1)*np.log(1 - x)
    return log_p+log_datafördelning(data,theta,alpha,beta)

# print(log_posterior(data,2,2))

def make_contour_plot():
    alpha_grid = np.linspace(0.1, 30, 100)
    beta_grid = np.linspace(0.1, 30, 100)
    log_posterior_grid = [[log_posterior(data,alpha, beta)for alpha in alpha_grid] for beta in beta_grid]
    posterior_grid = np.exp(log_posterior_grid - np.max(log_posterior_grid))
    plt.figure(figsize=(10, 6))
    plt.contour(alpha_grid, beta_grid, posterior_grid)
    plt.xlabel(r"$\alpha$", fontsize=12)
    plt.ylabel(r"$\beta$", fontsize=12)
    plt.show()

# make_contour_plot()

def method_moments(list):
    m1 = np.mean(list)
    m2 = np.mean([x**2 for x in list])
    alpha = (m1*(m1-m2))/(m2-m1**2)
    beta = ((m1-m2)*(1-m1))/(m2-m1**2)
    return([alpha,beta])

def metropolis():
    def genY(X):
        X = np.array(X)
        # proposal_alpha = stats.norm.rvs(np.exp(X[0]),1)
        # proposal_beta= stats.norm.rvs(np.exp(X[1]),1)

        proposal_alpha = np.exp(np.log(X[0]) + delta * stats.norm.rvs())
        proposal_beta = np.exp(np.log(X[1]) + delta * stats.norm.rvs())
        # proposal_theta = 
        return np.array([proposal_alpha,proposal_beta])

    n_samples = int(1e4)
    n_chains = 1
    delta = 0.5
    alphas = np.zeros((n_samples, n_chains))
    betas = np.zeros((n_samples, n_chains))
    thetas = np.zeros((n_samples,n_chains))
    
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

            rho = np.exp(log_posterior(data,proposal_alpha, proposal_beta)) / np.exp(log_posterior(data,last_alpha, last_beta)) # f(Y)/f(Xi-1)
            u = stats.uniform.rvs()
            if u <= rho:
                alphas[i + 1, j] = proposal_alpha
                betas[i + 1, j] = proposal_beta
            else:
                alphas[i + 1, j] = last_alpha
                betas[i + 1, j] = last_beta
    
    for j in range(n_chains):
        plt.plot(alphas[:, j], betas[:, j], '.-', markersize=10, alpha=0.5, label="chain"+str(j))
    plt.legend()
    plt.xlabel('alpha', fontsize=12)
    plt.ylabel('beta', fontsize=12)
    plt.show()

metropolis()

# import numpy as np
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()

# a = np.array(np.random.beta(2,2,50))
# b = np.array(np.random.beta(2,2,50))

# plt.scatter(a,b)
# plt.scatter(a[0],b[0], color="green", marker="o", label="starting point")
# plt.scatter(a[-1],b[-1], color="red", marker="o", label="end")

# for i in range(len(a) - 1):
#     ax.annotate('', xy=(a[i + 1], b[i + 1]), xytext=(a[i], b[i]),arrowprops=dict(arrowstyle='->', lw=1))
# ax.legend()
# plt.show()
