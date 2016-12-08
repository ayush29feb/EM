# EM Alorithm Implementation
# Estimating means given the distributions are the normal distributions with variance 1
# and the hursitic is that all distributions are equally likely

import math
import numpy as np

# Expectation Calculator
def expectation_zij(mu, x_i, mu_j):
    f_j = math.exp(-0.5 * math.pow(x_i - mu_j, 2))
    f_sum = sum(math.exp(-0.5 * math.pow(x_i - mu_k, 2)) for mu_k in mu)
    return f_j / f_sum

# EM Step
def maximize_mus(x, mu):
    return [sum(expectation_zij(mu, x_i, mu_k) * x_i for x_i in x) / sum(expectation_zij(mu, x_i, mu_k) for x_i in x) for mu_k in mu]

# Initialization Step
def initialize_mu(x):
    return [np.min(x), np.median(x), np.max(x)]

# Termination Check: epsilon value for means
def terminate(mu_t1, mu_t2, e):
    return all([abs(mu_t1_j - mu_t2_j) < e for mu_t1_j, mu_t2_j in zip(mu_t1, mu_t2)])

# Load Data
def format_data(filepath):
    f = open(filepath, "r")
    return [float(string) for string in f.read().split()]
    
# The Algorithm
def em(x):
    mu = initialize_mu(x)
    i = 1
    print str(i) + '] ' + str(mu)
    while True:
        mu_2 = maximize_mus(x, mu)
        if terminate(mu, mu_2, 0.001):
            break
        mu = mu_2
        i += 1
        print str(i) + '] ' + str(mu)

# Main
def main():
    em(format_data('data/dataset1.txt'))
    em(format_data('data/dataset2.txt'))
    em(format_data('data/unknown.txt'))

if __name__ == "__main__":
    main()