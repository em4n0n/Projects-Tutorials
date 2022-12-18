# Import necessary libraries
import numpy as np

# Define the probability function
def naive_bayes(priors, likelihoods, evidence):
  # Calculate the product of the priors and likelihoods
  unnormalized_posteriors = [prior * likelihood for prior, likelihood in zip(priors, likelihoods)]

  # Normalize the posteriors
  posteriors = unnormalized_posteriors / np.sum(unnormalized_posteriors)

  return posteriors

# Define the priors
priors = [0.1, 0.5, 0.4]

# Define the likelihoods
likelihoods = [0.6, 0.8, 0.5]

# Define the evidence
evidence = [1, 1, 0]

# Calculate the posteriors
posteriors = naive_bayes(priors, likelihoods, evidence)

# Print the posteriors
print(posteriors)
        