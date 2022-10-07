# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:10:05 2019

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
ages = [10, 12, 15, 16, 18, 21, 22, 22, 25, 26, 27, 27, 30, 32, 37, 47, 55, 66, 69, 71, 73, 81, 95]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
media=mean(ages)


plt.axvline(media,color="red",linewidth=2)






plt.hist(ages, bins=bins, edgecolor="pink")
plt.show()