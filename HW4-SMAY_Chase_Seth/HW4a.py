import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the standard normal distribution N(0,1)
mu, sigma = 0, 1
x_values = np.linspace(-4, 4, 1000)

# Calculate the PDF and CDF
pdf_values = norm.pdf(x_values, mu, sigma)
cdf_values = norm.cdf(x_values, mu, sigma)

# Probability of interest
prob = norm.cdf(-0.5, mu, sigma)

# Create the plot
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plot the PDF
ax[0].plot(x_values, pdf_values, label='N(0,1)')
ax[0].fill_between(x_values, pdf_values, where=(x_values <= -0.5), color='blue', alpha=0.3)
ax[0].annotate(f'P(X<=-0.5|N(0,1))={prob:.2f}', xy=(-0.5, norm.pdf(-0.5, mu, sigma)),
               xytext=(-2, 0.2), arrowprops=dict(arrowstyle='->', lw=1.5), ha='center')

# Plot the CDF
ax[1].plot(x_values, cdf_values, label='CDF of N(0,1)')
ax[1].scatter(-0.5, prob, color='red')
ax[1].axhline(y=prob, color='black', linestyle='--')
ax[1].axvline(x=-0.5, color='black', linestyle='--')

# Set titles and labels
ax[0].set_title('PDF of N(0,1)')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Probability Density')
ax[0].legend()

ax[1].set_title('CDF of N(0,1)')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Cumulative Probability')
ax[1].legend()

plt.tight_layout()
plt.show()

# Parameters for the normal distribution N(175, 3)
mu, sigma = 175, 3
x_values = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Calculate the PDF and CDF
pdf_values = norm.pdf(x_values, mu, sigma)
cdf_values = norm.cdf(x_values, mu, sigma)

# Probability of interest
p_value = 1 - norm.cdf(181, mu, sigma)

# Create the plot
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plot the PDF
ax[0].plot(x_values, pdf_values, label=f'N({mu},{sigma})')
ax[0].fill_between(x_values, pdf_values, where=(x_values > 181), color='blue', alpha=0.3)
ax[0].annotate(f'P(X>181|N({mu},{sigma}))={p_value:.2f}', xy=(181, norm.pdf(181, mu, sigma)),
               xytext=(mu + 1.5*sigma, 0.02), arrowprops=dict(arrowstyle='->', lw=1.5), ha='center')

# Plot the CDF
ax[1].plot(x_values, cdf_values, label=f'CDF of N({mu},{sigma})')
ax[1].scatter(181, norm.cdf(181, mu, sigma), color='red')
ax[1].axhline(y=norm.cdf(181, mu, sigma), color='black', linestyle='--')
ax[1].axvline(x=181, color='black', linestyle='--')

# Set titles and labels
ax[0].set_title(f'PDF of N({mu},{sigma})')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Probability Density')
ax[0].legend()

ax[1].set_title(f'CDF of N({mu},{sigma})')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Cumulative Probability')
ax[1].legend()

plt.tight_layout()
plt.show()
