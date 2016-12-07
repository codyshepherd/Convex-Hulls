import matplotlib.pyplot as plt
import timeit as t
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from algos import *
import json

def g_s(ts):
    r = t.timeit(lambda: graham_scan(ts), number=100)
    print 'graham'
    print len(ts)
    print r
    return r

def q_h(ts):
    r = t.timeit(lambda: quick_hull(ts), number=100)
    print 'qhull'
    print len(ts)
    print r
    return r

def chns(ts):
    r = t.timeit(lambda: chans(ts), number=100)
    print 'chans'
    print len(ts)
    print r
    return r

min_datasize = 3
max_datasize = 10000
num_samples = 10

N = np.linspace(min_datasize, max_datasize, num_samples).astype(int).tolist()
with open('datasize_samples.json', 'w') as fname:
    json.dump(N, fname)


normal_data = []
ring_data = []
fring_data = []
linear_data = []
flinear_data = []
backward_data = []

for i in N:
    normal_data.append(normal_nd(i))
    ring_data.append(circle(i))
    fring_data.append(fuzzy_ring(i))
    linear_data.append(linear(i))
    flinear_data.append(fuzzy_linear(i))
    backward_data.append(backward(i))

grahams = []
qhull = []
chs = []
print "######################## starting normal #########################"
print
for A in normal_data:
    grahams.append(g_s(A))
    qhull.append(q_h(A))
    chs.append(chns(A))
with open('grahams_normal.json', 'w') as fname:
    json.dump(grahams,fname)
with open('qhull_normal.json', 'w') as fname:
    json.dump(qhull,fname)
with open('chans_normal.json', 'w') as fname:
    json.dump(chs,fname)

print "normal done!"

grahams = []
qhull = []
chs = []
print "######################## starting ring ##########################"
print
for A in ring_data:
    grahams.append(g_s(A))
    qhull.append(q_h(A))
    chs.append(chns(A))
with open('grahams_ring.json', 'w') as fname:
    json.dump(grahams,fname)
with open('qhull_ring.json', 'w') as fname:
    json.dump(qhull,fname)
with open('chans_ring.json', 'w') as fname:
    json.dump(chs,fname)

print "ring done!"

grahams = []
qhull = []
chs = []
print "###################### starting fuzzy ring ######################"
print
for A in fring_data:
    grahams.append(g_s(A))
    qhull.append(q_h(A))
    chs.append(chns(A))
with open('grahams_fring.json', 'w') as fname:
    json.dump(grahams,fname)
with open('qhull_fring.json', 'w') as fname:
    json.dump(qhull,fname)
with open('chans_fring.json', 'w') as fname:
    json.dump(chs,fname)

print "fuzzy ring done!"

grahams = []
qhull = []
chs = []
print "######################## starting linear #########################"
print
for A in linear_data:
    grahams.append(g_s(A))
    qhull.append(q_h(A))
    chs.append(chns(A))
with open('grahams_linear.json', 'w') as fname:
    json.dump(grahams,fname)
with open('qhull_linear.json', 'w') as fname:
    json.dump(qhull,fname)
with open('chans_linear.json', 'w') as fname:
    json.dump(chs,fname)

print "linear done!"


grahams = []
qhull = []
chs = []
print "######################### starting fuzzy linear ######################"
print
for A in flinear_data:
    grahams.append(g_s(A))
    qhull.append(q_h(A))
    chs.append(chns(A))
with open('grahams_flinear.json', 'w') as fname:
    json.dump(grahams,fname)
with open('qhull_flinear.json', 'w') as fname:
    json.dump(qhull,fname)
with open('chans_flinear.json', 'w') as fname:
    json.dump(chs,fname)

print "fuzzy ring done!"

grahams = []
qhull = []
chs = []
print "######################## starting backward #########################"
print
for A in backward_data:
    grahams.append(g_s(A))
    qhull.append(q_h(A))
    chs.append(chns(A))
with open('grahams_backward.json', 'w') as fname:
    json.dump(grahams,fname)
with open('qhull_backward.json', 'w') as fname:
    json.dump(qhull,fname)
with open('chans_backward.json', 'w') as fname:
    json.dump(chs,fname)

print "backward done!"


print
print "test program done!"

