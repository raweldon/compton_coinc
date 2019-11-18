import numpy as np 
import os
import lmfit
import matplotlib.pyplot as plt

def gauss_line(x, a, mu, sig, m, b):
    gaus = a*np.exp( -(x - mu)**2.0/(2.0*sig**2.0) )
    line = m*x + b
    return gaus + line

def fit_coinc_data(coinc_data, show_plot):
    ql, tof = coinc_data
    ql = ql[np.where(ql > 5000)]
    ql_hist, bins = np.histogram(ql, bins=100, range=(ql.min(), 19000))
    bin_centers = (bins[:-1] + bins[1:])/2

    # fit histogram 
    gmodel = lmfit.Model(gauss_line)
    params = gmodel.make_params(a=10, mu=13500, sig=400, m=-1, b=1)
    params['mu'].max = 13700
    params['mu'].min = 13200
    #params['b'].min = 1
    #params['m'].max = 0
    params['sig'].max = 800
    res = gmodel.fit(ql_hist, params=params, x=bin_centers, nan_policy='omit')#, method='nelder')
    print '\n', lmfit.fit_report(res)

    # get number of counts under gaussian (estimate of uncert on mean)
    mu = res.params['mu'].value
    sigma = res.params['sig'].value
    counts = len(ql[np.where((ql < mu + 3*sigma ) & (ql > mu - 3*sigma))])

    if show_plot:
        plt.figure(100)
        plt.plot(bin_centers, ql_hist)
        plt.plot(bin_centers, gauss_line(bin_centers, res.params['a'], res.params['mu'], res.params['sig'], res.params['m'], res.params['b']))
        plt.plot([mu - 3*sigma]*100, np.linspace(0, 20, 100), '--r')
        plt.plot([mu + 3*sigma]*100, np.linspace(0, 20, 100), '--r')

    return res.params['mu'].value, res.params['sig'].value, counts


if __name__ == '__main__':

    cwd = os.getcwd()
    directory = cwd + '/plots/' 
    filename = 'coinc_data_10ns.npy'

    coinc_data = np.load(directory + filename)
    mu, sigma = fit_coinc_data(coinc_data, show_plot=True)
    print '\n mu =', round(mu, 3), '\n sigma =', round(sigma, 3)
    plt.show()