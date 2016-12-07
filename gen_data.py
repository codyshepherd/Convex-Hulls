import matplotlib.pyplot as plt
import numpy as np
import random

def fuzzy_ring(num):
    theta = np.linspace(0, 2*np.pi, num=num)
    a, b = map(lambda x:(10+np.random.rand(1,1))*x, np.cos(theta)), map(lambda x:(10+np.random.rand(1,1))*x, np.sin(theta))

    return zip(a, b)

def circle(num):
    theta = np.linspace(0, 2*np.pi, num=num)
    a, b = 1 * np.cos(theta), 1 * np.sin(theta)
    return zip(a, b)

def fuzzy_linear(num):
    x = np.linspace(0,100, num=num)
    y = np.linspace(0,100, num=num)
    x = map(lambda x: 5*np.random.rand(1)+x, x)
    y = map(lambda x: 5*np.random.rand(1)+x, y)
    return zip(x,y)

def linear(num):
    x = np.linspace(0,100, num=num)
    y = np.linspace(0,100, num=num)
    return zip(x,y)

def fan(num):
    x = np.linspace(0,100, num=num)
    y = np.linspace(0,100, num=num)
    x = map(lambda x: (np.random.rand(1)+1)*x, x)
    y = map(lambda x: (np.random.rand(1)+1)*x, y)
    return zip(x, y)

def backward(num):
    points = fan(num)
    points = sorted(points, reverse=True)
    return points

def normal_nd(num):
    return np.random.rand(num, 2).tolist()

def normal_tuples(num):
    return [(random.randint(-100, 100),random.randint(-100, 100)) for _ in xrange(num)]

def normal_list1(num):
    return[[random.randint(-100,100) for _ in xrange(num)], [random.randint(-100,100) for _ in xrange(num)]]

def normal_list2(num):
    return[[random.randint(-100,100), random.randint(-100,100)] for _ in xrange(num)]
    
