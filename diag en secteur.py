# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:33:33 2024

@author: mayar
"""

import matplotlib.pyplot as plt

import numpy as np
import statistics as st
labels = 'bleu', 'orangé', 'vert', 'rouge'

sizes = [15, 30, 45, 10]
explode = (0.2, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs') #0.2
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90,shadow=True)
#shadow=True,
ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()