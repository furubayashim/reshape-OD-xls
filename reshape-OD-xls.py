#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys

if len(sys.argv) >1:
    samplefile = sys.argv[1]
else:
    print("enter file name")

df = pd.read_excel(samplefile,skiprows=35)
mean = df.iloc[0,1:]
stdev = df.iloc[1,1:]

mean_op = pd.DataFrame()
stdev_op = pd.DataFrame()

for a in ['A','B','C','D','E','F','G','H']:
    d = mean.filter(regex=a)
    d.name = a
    d.index = np.arange(1,13,1)
    mean_op = mean_op.append(d)

for a in ['A','B','C','D','E','F','G','H']:
    d = stdev.filter(regex=a)
    d.name = a
    d.index = np.arange(1,13,1)
    stdev_op = stdev_op.append(d)

mean_op.to_excel('OD.xlsx')
stdev_op.to_excel('OD_stdev.xlsx')
