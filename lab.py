import numpy as np
import pandas as pd
import math

from scipy.optimize import curve_fit
from scipy.stats import norm
from IPython.display import display, Math

import matplotlib.pyplot as plt

def create_plot(ttl='', s1='', s2='', size='M', fsize=(15, 12)):
    ttl_s = {'S': 15, 'M': 20, 'L': 25}
    lbl_s = {'S': 10, 'M': 15, 'L': 20}
    tck_s = {'S': 10, 'M': 12, 'L': 16}
    plt.figure(figsize=fsize)
    plt.title(ttl, fontsize=ttl_s[size])
    plt.minorticks_on()
    plt.grid(which='major')
    plt.grid(which='minor', linewidth=0.2)
    plt.tick_params(axis='both', which='major', labelsize=tck_s[size])
    plt.xlabel(s1, fontsize=lbl_s[size])
    plt.ylabel(s2, fontsize=lbl_s[size])