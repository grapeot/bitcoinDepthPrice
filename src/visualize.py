import numpy as np
import matplotlib.pyplot as pp
from pylab import Line2D, arrow
import os
import sys

def visualize(fn, p1, p2):
    basefn = os.path.basename(fn)
    dirfn = os.path.dirname(fn)
    askfn = os.path.join(dirfn, 'asks_' + basefn)
    bidfn = os.path.join(dirfn, 'bids_' + basefn)
    noextFn, ext = os.path.splitext(fn)

    # Preprocess
    os.system('coffee preprocess.coffee ' + fn);
    pp.figure(1)
    pp.clf()

    # draw ask
    ask = np.loadtxt(askfn)
    idx = ask[:, 0] < np.min(ask[:, 0]) * 1.2
    pp.plot(ask[idx, 0], np.cumsum(ask[:, 1])[idx], 'r')
    askMax = max(np.cumsum(ask[:, 1])[idx])

    # draw bid
    bid = np.loadtxt(bidfn)
    idx = bid[:, 0] > np.max(bid[:, 0]) * 0.8
    pp.plot(bid[idx, 0], np.flipud(np.cumsum(np.flipud(bid[:, 1])))[idx])
    bidMax = max(np.cumsum(bid[:, 1])[idx])

    # draw the price change
    lineHeight = max(bidMax, askMax) * 0.6
    title = os.path.basename(noextFn)
    pp.xlim((500, 850))
    pp.ylim((0, 10000))
    pp.title(title)
    ax = pp.gca()
    ax.add_line(Line2D([p1, p1], [0, lineHeight], linewidth=2, color='black'))
    ax.add_line(Line2D([p2, p2], [0, lineHeight], linewidth=2, color='blue'))
    arrow(p1, 500, (p2 - p1) * 0.7, 0, fc="k", ec="k", head_width=200, head_length=abs(p2-p1)*0.3)

    # axes and legends
    pp.xlabel('Price (USD)')
    pp.ylabel('Amount (BTC)')
    pp.legend(['Ask', 'Bid'])
    # pp.show()
    pp.savefig(noextFn + '.png')

    os.system('rm ' + askfn)
    os.system('rm ' + bidfn)

if __name__ == '__main__':
    for line in file('../dat/p_price.txt').readlines():
        fn, p1, p2 = line.split(' ')
        visualize(fn, float(p1), float(p2))
