import copy
import random as rand
import typing as T
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#deprecated
'''
def get_mean(pop):
    sum = 0
    for p in pop:
        sum += p
    return sum/len(pop)

def get_sd(pop):
    mean = get_mean(pop)
    sum = 0
    for p in pop:
        sum += ((p-mean)**2)
    return (sum/len(pop))**0.5
'''

def get_random_samples(n, m, p):    
    '''
    Parameters
        n: number of samples
        m: number of values in each sample
        p: population array: Python list
        
    Returns
        2d array
    '''
    
    q = []
    for i in range(n):
        population = copy.deepcopy(p)
        r = []
        for j in range(m):
            r.append(population.pop(rand.randrange(0, len(population))))
        q.append(r)
    return np.array(q)

def generate_population(minimum, maximum, n):
    '''
    Parameters
        minimum: minimum range value
        maximum: maximum range value
        n: number of values in population
    
    Returns
        1d np array of population values
    '''
    p = np.empty(0)
    for i in range(n):
        p = np.append(p, rand.randrange(minimum,maximum))
    return p

#generate randoms sets of means
def get_means(samples):
    '''
    Parameters
        samples: 2d array of samples
        
    Returns
        1d array of means
    '''
    means = np.empty(0)
    for s in samples:
        means = np.append(means, np.mean(s))
    return means

'''
Abstract function to generate histogram from following parameters:
    Minimum Value
    Maximum Value
    Population Size
    Sample Size
    Number of Samples
'''
def plot_clt(mn, mx, ps, ss, sc):
    p = generate_population(mn, mx, ps)
    s = get_random_samples(sc, ss, list(p))
    means = get_means(s)
    sns.displot(means)
    
'''
Abstract function to get means:

Parameters
    Minimum Value
    Maximum Value
    Population Size
    Sample Size
    Number of Samples
'''
def clt_means(mn, mx, ps, ss, sc):
    p = generate_population(mn, mx, ps)
    s = get_random_samples(sc, ss, list(p))
    return get_means(s)
