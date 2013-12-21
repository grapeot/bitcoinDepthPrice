import numpy as np
import matplotlib.pyplot as pp
import os
import sys

# Parse parameters
if len(sys.argv) != 2:
    print 'Usage: visualize <filename>'
    exit(-1)
fn = sys.argv[1]
basefn = os.path.basename(fn)
dirfn = os.path.dirname(fn)
askfn = os.path.join(dirfn, 'asks_' + basefn)
bidfn = os.path.join(dirfn, 'bids_' + basefn)

# Preprocess
os.system('coffee preprocess.coffee ' + fn);
ask = np.loadtxt(askfn)
idx = ask[:, 0] < np.min(ask[:, 0]) * 1.2
pp.plot(ask[idx, 0], np.cumsum(ask[:, 1])[idx], 'r')

bid = np.loadtxt(bidfn)
idx = bid[:, 0] > np.max(bid[:, 0]) * 0.8
pp.plot(bid[idx, 0], np.flipud(np.cumsum(np.flipud(bid[:, 1])))[idx])

pp.xlabel('Price (USD)')
pp.ylabel('Amount (BTC)')
pp.legend(['Ask', 'Bid'])
pp.show()

os.system('rm ' + askfn)
os.system('rm ' + bidfn)
