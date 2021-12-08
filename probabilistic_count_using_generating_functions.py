# We can use the numpy package which elegantly supports polynomial artihmetic using the numpy.polynomial package.
# Using this package, a polynomial is represented simply as an array.
# For example, the numpy.polynomial.polynomial.Polynomial([2,5,4]) corresponds to the polynomial 4x^2 + 5x + 2
import numpy as np

# The following function takes a list of probabilities and computes the probability mass function of the probabilistic count of these probabilities. 
# In other words, given a list of Bernoulli random events ("trials") each having a (possibly non-identical) probability of successed, the function below computes the distribution of the number of successful trials.
# In yet other words, the function below computes the proability mass function of a Poisson-Binomial distribution having the specified list of parameters.
# 
# As an example, probabilistic_Counting([0.3,0.2,0.9]) will return the array [0.056,0.542,0.348,0.054] indicating that out of three trials having probabilities of 0.3, 0.2, and 0.9, respectively, the probability of having exactly zero successful trials is 0.056, the probability of having exactly one successful trial is 0.542, the probability of having exactly two successful trials is 0.348, and the probability of all four trials succeeding is 0.054.
def probabilistic_Counting(probabilities):
    # The initial polynomial 1 corresponds to zero successful trials with a probability of 100%
    result_polynomial = np.polynomial.polynomial.Polynomial([1])
    for p in probabilities:
        #For each probability p create the generating polynomial px + (1-p), which is represented as np.polynomial.polynomial.Polynomial([1-p,p])
        new_generating_polynomial = np.polynomial.polynomial.Polynomial([1-p,p])
        #Multiply this new polynomial to the current result
        result_polynomial = result_polynomial * new_generating_polynomial
    return(result_polynomial)                                                         

# Example using probabilities 0.2, 0.3, and 0.9.
poly = probabilistic_Counting([0.2,0.9,0.3])
print(poly.coef)


# The following variant truncates, in each iteration of polynomial expansion, any monomials having an exponent greater than K. This variant is useful for computing the probability of having a probabilistic count of at least (at most) K without expanding the full probabilistic count.
def probabilistic_Counting_Truncated(probabilities,K):
    # The initial polynomial 1 corresponds to zero successful trials with a probability of 100%
    result_polynomial = np.polynomial.polynomial.Polynomial([1])
    for p in probabilities:
        #For each probability p create the generating polynomial px + (1-p), which is represented as np.polynomial.polynomial.Polynomial([1-p,p])
        new_generating_polynomial = np.polynomial.polynomial.Polynomial([1-p,p])
        #Multiply this new polynomial to the current result
        result_polynomial = result_polynomial * new_generating_polynomial
        result_polynomial = result_polynomial.cutdeg(K)
    return(result_polynomial)                                                         


# The same example using probabilities 0.2, 0.3, and 0.9, truncated to a degree of K=2
poly = probabilistic_Counting_Truncated([0.2,0.9,0.3],2)
print(poly.coef)

