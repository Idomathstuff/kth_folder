from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import gamma, loggamma
# import statinlprojekt as statproj
from statinlprojekt import Theta_MoM_skattning


data = np.array([0, 0, 0.15, 0.27, 0.3, 0.16, 0.36, 0.41, 0.48, 0.28])

beta_pdf = lambda x,alpha,beta: (gamma(alpha+beta) / (gamma(alpha)+gamma(beta))) * (x**(alpha-1)) * (1-x)**(beta-1)


def log_datafördelning(data, alpha,beta):
    DF = 0
    for x in data:
        if x==0:
            DF+=0
        else:
            DF+=np.log(beta_pdf(x, alpha, beta))
    return DF

# def log_prior(alpha, beta):
#     lambd = 2
#     thet = 5
#     return np.log(lambd**thet) - loggamma(thet) + (thet - 1)*np.log(alpha + beta + 1) - lambd*(alpha + beta + 1) - np.log(alpha + beta) + np.log(1) #np.log(1) is the prior of theta

def log_prior(alpha, beta):
    return np.log(1**3) - loggamma(3) + (3 - 1)*np.log(alpha + beta + 1) - 1*(alpha + beta + 1) - np.log(alpha + beta)

def log_posterior(data, alpha, beta):
    return log_prior(alpha,beta) + log_datafördelning(data,alpha, beta)

def method_moments(list):
    m1 = np.mean(list)
    m2 = np.mean([x**2 for x in list])
    alpha = (m1*(m1-m2))/(m2-m1**2)
    beta = ((m1-m2)*(1-m1))/(m2-m1**2)
    return([alpha,beta])

def make_contour_plot():
    uL = 10
    alpha_grid = np.linspace(0.1, uL, 100)
    beta_grid = np.linspace(0.1, uL, 100)
    log_posterior_grid = [[(log_posterior(data, alpha, beta)) for alpha in alpha_grid] for beta in beta_grid]
    posterior_grid = (np.exp(log_posterior_grid) - np.max(np.exp(log_posterior_grid)))
    plt.figure(figsize=(6, 6))
    plt.contour(alpha_grid, beta_grid, posterior_grid)
    plt.xlabel(r"$\alpha$", fontsize=12)
    plt.ylabel(r"$\beta$", fontsize=12)

    # Adjust the limits and center the contour plot
    plt.xlim(0, uL)  # Set the desired x-axis limits
    plt.ylim(0, uL)   # Set the desired y-axis limits

    plt.show()

# def make_contour_plot():
#     alpha_grid = np.linspace(0.1, 10, 100)  # Fixed range for alpha
#     print(alpha_grid)
#     beta_grid = np.linspace(0.1, 10, 100)    # Fixed range for beta    
#     alpha_grid, beta_grid = np.meshgrid(alpha_grid, beta_grid)    
#     log_posterior_grid = log_posterior(data, alpha_grid, beta_grid)
#     unnormalized_posterior = np.exp(log_posterior_grid)
#     plt.figure(figsize=(6, 6))
#     plt.contour(alpha_grid, beta_grid, unnormalized_posterior, levels=50)
#     plt.xlabel(r"$\alpha$", fontsize=12)
#     plt.ylabel(r"$\beta$", fontsize=12)
#     plt.title("Contour Plot of Posterior Distribution")
#     plt.show()


make_contour_plot()


# from mpl_toolkits.mplot3d import Axes3D

# def make_3d_plot():
#     alpha_grid = np.linspace(0.1, 10, 1000)  # Fixed range for alpha
#     beta_grid = np.linspace(0.1, 10, 1000)    # Fixed range for beta    
#     alpha_grid, beta_grid = np.meshgrid(alpha_grid, beta_grid)    
#     log_posterior_grid = log_posterior(data, 0.22, alpha_grid, beta_grid)
#     unnormalized_posterior = np.exp(log_posterior_grid)
    
#     fig = plt.figure(figsize=(8, 8))
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(alpha_grid, beta_grid, unnormalized_posterior, cmap='viridis')
    
#     ax.set_xlabel(r"$\alpha$", fontsize=12)
#     ax.set_ylabel(r"$\beta$", fontsize=12)
#     ax.set_zlabel('Posterior', fontsize=12)
#     ax.set_title("3D Plot of Posterior Distribution")
    
#     plt.show()

# # Call the function to create the 3D plot
# make_3d_plot()





