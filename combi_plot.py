'''
Combined plotting of one or more series with pyplot

Copyright (C) 2015-17 Niels Wadsholt
'''

import itertools
import math
import matplotlib.pyplot as plt

def combi_plot(y_vals, lbls, x_vals = None, logplot = False, y_lbl = '', x_lbl = '', ttl = '', ln_styles = None):
    """
    Plots one or more series of y-values against a corresponding series of x-values.

    If no x-values are given, they default to a list of integers
    ranging from 0 to the size of the first y-list.
    
    Pyplot must be imported like so:
    import matplotlib.pyplot as plt
    """
    
    colors = itertools.cycle('rbmcgyk')
    
    num_curves = len(y_vals)
    assert num_curves == len(lbls), 'ERROR: The number of curves and labels must match.'
    
    if not x_vals:
        x_vals = range(len(y_vals[0]))
    
    if not ln_styles:
        ln_styles = ['-' for i in range(num_curves)]
    
    assert num_curves == len(ln_styles), 'ERROR: The number of defined line styles and curves must match.'
    
    for i in range(num_curves):
        plt.plot(x_vals, y_vals[i], next(colors) + ln_styles[i], label = lbls[i])
    
    if logplot:
        plt.xscale('log')
        plt.yscale('log')
    
    plt.xlabel(x_lbl)
    plt.ylabel(y_lbl)
    plt.legend(loc='best')
    
    plt.title(ttl)
    plt.grid()
    
    plt.show()
