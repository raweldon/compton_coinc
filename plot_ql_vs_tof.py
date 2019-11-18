#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import directories
import os
import glob

def single():
    directory = '/home/radians/raweldon/compton_coinc/results/plots/' 
    filenames = ('coinc_data_10ns.npy', 'coinc_data_20ns.npy')#, 'coinc_data_50ns.npy', 'coinc_data_100ns.npy') 
    det_angles = [70, 60, 50, 40, 30, 20, 20, 30, 40, 50, 60, 70] #BL to BR
    det_no = range(4,16) #corresponds to struck channel no (stil det 0)

    for i,filename in enumerate(filenames):
        print filename

        ql_vs_tof = np.load(directory + filename)
        print ql_vs_tof
        ql = ql_vs_tof[0]
        print max(ql)
        tof = ql_vs_tof[1]

        '''Plots'''    
    #    save_dir = '/home/raweldon/tunl/6_2016_experiment/Edep_vs_timing/'+str(angle)+'_deg_plots'
    #    if not os.path.exists(save_dir):
    #        os.makedirs(save_dir)        
        
        fig = plt.figure()
        plt.plot(tof, ql, 'o', alpha=0.5)
        plt.xlabel(r'$\Delta$t (ns)',fontsize=18)
        plt.ylabel('Light Output (MeVee)',fontsize=18)
        plt.title(os.path.basename(filename),fontsize=20)
        #plt.title(filename,fontsize=20)
        #plt.ylim(-0.2,6.0)
        #fig.savefig(save_dir + '/b_det'+str(det)+'.png', dpi=400)  

        plt.figure()
        plt.hist(ql, bins=50)
        plt.title(os.path.basename(filename),fontsize=20)
        
    plt.show()

if __name__ == '__main__':
    single()
