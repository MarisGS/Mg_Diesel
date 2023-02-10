# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:34:09 2020

@author: Lietotajs
"""
def SimD (p, T, CR):
    import numpy as np

    #import matplotlib.pyplot as plt
    #from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


    # Initial parameters
    #Choose compression ratio according to data: 14 or 19

    #CR=14 # compression ratio, other option CR=19


    from fc_volume import volume #call function to calculate volume
    Vd, Vc, Vth, dVth, cad =volume (CR)

    p_i=p*10**5
    T_i=T+273.15
    Gamma=1.3

 
    p_cyl=np.zeros(3600) # create empty array
    T_cyl=np.zeros(3600)
    p_cyl=np.asfarray(p_cyl,float) # change data type to float
    T_cyl=np.asfarray(T_cyl,float)

    p_cyl[0]=p_i
    T_cyl[0]=T_i

    
    zz=1   
    for ii in range(1801,5400):

        p_cyl[zz]=((Vth[ii-1]/Vth[ii])**Gamma)*p_cyl[zz-1] 
        T_cyl[zz]=((Vth[ii-1]/Vth[ii])**(Gamma-1))*T_cyl[zz-1] 
        #T_cyl[zz]= ((p_cyl[zz-1]*Vth[ii-1])/T_cyl[zz-1])*(p_cyl[zz]*Vth[ii])
    
    
        zz=zz+1

    p_cyl_b=p_cyl/10**5      
    cad_360=cad[1800:5400]
    return (p_cyl_b, T_cyl, cad_360)
