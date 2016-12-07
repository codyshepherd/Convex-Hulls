import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.cm as cm
import json
import numpy as np
import os
import re

files = [x for x in os.listdir('.')]
srch = re.compile('.*json$')
files = filter(srch.match, files)

samples = 'datasize_samples.json'
files.remove(samples)
print "working files"
print files

with open(samples, 'r') as fh:
    sample_range = json.load(fh)
high_point = max(sample_range)
deep_range = xrange(3, high_point, 1)

max_times = {}

for f in files:
    with open(f, 'r') as fh:
        try:
            results = json.load(fh)
        except ValueError as e:
            print e
            print fh
            break
    
    mx = 0
    mx_place = -1
    for i, res in enumerate(results):
        if res > mx:
            mx = res
            mx_place = i
            
    max_result = max(results)
    max_times[f[:-5]+ ' ' +str(sample_range[mx_place])] = mx
    #scale = max_result / high_point
    scale = max_result / (high_point*np.log(high_point))
    print "scale: ", scale

    X = [x for x in xrange(1, len(sample_range)+1)]

    pp = PdfPages(f[:-5] +'.pdf')
    plt.figure()
    plt.clf()
    plt.title(f[:-5])
    plt.ylabel('Seconds')
    plt.xlabel('Input Size (scaled)')
    plt.plot(X, results, label=f[:-5])
    #plt.plot(sample_range, map(lambda z: scale*z*np.log10(z), sample_range), color='red', label=str(scale)+'*n*log_10(n)')
    plt.plot(X, map(lambda z: z*np.log2(z), X), color='red', label='n*log_2(n)')
    #plt.plot(sample_range, map(lambda z: scale*z, sample_range), color='green', label=str(scale)+'*n')
    plt.plot(X, map(lambda z: z, X), color='green', label='n')
    plt.legend()
    pp.savefig()
    pp.close()

#max_times = sorted(max_times)
colors = list(cm.rainbow(np.linspace(0,1,len(max_times.keys()))))
pp = PdfPages('comparative.pdf')
plt.figure()
plt.clf()
plt.title('Comparison of Slowest Cases')
plt.ylabel('seconds')
plt.xlabel('alg/size')
for i, v in enumerate(sorted(max_times.iterkeys())):
    #color += 1024
    plt.scatter(i, max_times[v], color=colors.pop(), label=v)
#plt.legend()
art = []
lgd = plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)
art.append(lgd)
pp.savefig(
    additional_artists=art,
    bbox_inches="tight")
pp.close()
