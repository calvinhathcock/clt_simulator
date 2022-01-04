import copy
import random as rand

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

def get_random_samples(n, m, p):    
    '''
    Parameters
        n: number of samples
        m: number of values in each sample
        p: population array
        
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
    return q

def generate_population(minimum, maximum, n):
    p = []
    for i in range(n):
        p.append(rand.randrange(minimum,maximum))
    return p