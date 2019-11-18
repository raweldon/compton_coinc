from coinc_analysis import fit_coinc_data
from edge_analysis import single
import os
import numpy as np
import time
import matplotlib.pyplot as plt

def main():

    # compton coinc
    cwd = os.getcwd()
    directory = cwd + '/plots/' 
    filename = 'coinc_data_10ns.npy'
    coinc_data = np.load(directory + filename)
    mu, sigma, counts = fit_coinc_data(coinc_data, show_plot=True)

    # compton edge fit
    det_no = 0  # 0 stilbene, 1 ej309
    spread = 28000 # initial guess for spread
    min_range = 8000
    e0, c = single(det_no, spread, min_range, lin_scaling=True)

    return mu, sigma, counts, e0, c

if __name__ == '__main__':
    mu, sigma, counts, e0, c = main()
    print '\n------------------------------------------'
    print '               Full results '
    print '------------------------------------------'
    print '\nCompton coincidence results:'
    print '\n    mu =', round(mu, 3), '\n    sigma =', round(sigma, 3)
    print '\n    uncert =', sigma/np.sqrt(counts), 'ADC unit'
    print '\n    rel_uncert =', sigma/mu/np.sqrt(counts)*100, '%'
    print '\nCompton edge results:'
    val = c*(0.477 + e0/c)
    print '\n    477 keV ADC value =', round(val, 3)

    print '\n\nprecent diff =', round(abs(val - mu)/mu*100, 2), '%'
    plt.show()

