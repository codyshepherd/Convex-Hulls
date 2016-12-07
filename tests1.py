import matplotlib.pyplot as plt
import timeit as t
import numpy as np
import multiprocessing as mp
from matplotlib.backends.backend_pdf import PdfPages
from algos import *

def doit(num):
    global results
    ts = circle(num)
    r = t.timeit(lambda: graham_scan(ts), number=10000)
    #print "Number: ", num
    #print r
    print str(num)+" done"
    return r

"""
for i in range(3,101):
    p = mp.Process(target=doit, args=(i,))
    p.start()

p.join()
"""
p = mp.Pool()
results = p.map(doit, xrange(3,101))

print "shape of results"
print len(results)
print "results"
print results

pp = PdfPages('runtime.pdf')
plt.figure()
plt.clf()
plt.plot([x for x in xrange(3,101)],results)
pp.savefig()
pp.close()
