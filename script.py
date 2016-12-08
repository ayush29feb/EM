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

# LogLikelihood Calculator
def loglikelyhood(x, mu):
    c = (len(x) * math.log(len(mu))) + (len(x) * math.log(2 * math.pi) / 2)
    return -c - (sum(sum(expectation_zij(mu, x_i, mu_k) * math.pow(x_i - mu_k, 2) for mu_k in mu) for x_i in x) / 2)

# EM Step
def maximize_mus(x, mu):
    return [sum(expectation_zij(mu, x_i, mu_k) * x_i for x_i in x) / sum(expectation_zij(mu, x_i, mu_k) for x_i in x) for mu_k in mu]

# Initialization Step
def initialize_mu(x):
    return [np.min(x), np.median(x), np.max(x)]

# Termination Check: epsilon value for means
def terminate_mu(mu_t1, mu_t2, e):
    return all([abs(mu_t1_j - mu_t2_j) < e for mu_t1_j, mu_t2_j in zip(mu_t1, mu_t2)])

# Termination Check: epsilon value for loglikelyhood
def terminate_loglikelyhood(ll1, ll2, e):
    return abs(ll1 - ll2) < e

# Load Data
def format_data(filepath):
    f = open(filepath, "r")
    return [float(string) for string in f.read().split()]
    
# The Algorithm
def em(x):
    mu = initialize_mu(x)
    ll = loglikelyhood(x, mu)
    i = 1
    print str(i) + '] ' + str(mu) + ' ' + str(ll)
    while True:
        mu = maximize_mus(x, mu)
        ll_2 = loglikelyhood(x, mu)
        i += 1
        print str(i) + '] ' + str(mu) + ' ' + str(ll_2)
        if terminate_loglikelyhood(ll, ll_2, 0.001):
            break
        ll = ll_2
    print '\n'
    
    for i in range(len(x)):
        exps = [expectation_zij(mu, x[i], mu_j) for mu_j in mu]
        print '[' + str(i + 1) + ',]' + str(x[i]) + ' ' + str(exps)


# Main
def main():
    em(format_data('data/dataset1.txt'))
    em(format_data('data/dataset2.txt'))
    em(format_data('data/unknown.txt'))

if __name__ == "__main__":
    main()