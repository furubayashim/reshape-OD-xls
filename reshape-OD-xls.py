#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
import os

if len(sys.argv) >1:
    samplefile = sys.argv[1]
else:
    print("enter file name")

df = pd.read_excel(samplefile)

# find "Well" in the sheet; store OD data in data_df
data_index = (df.iloc[:,0] == 'Well').idxmax()
data_df = df.iloc[data_index+1:-2,1:]
well_label = df.iloc[data_index,1:].values
col_label = df.iloc[data_index+1:-2,0].values
data_df.columns = well_label
data_df.index = col_label

def convert_to_96_sheet(series):
    outdf = pd.DataFrame()
    for a in ['A','B','C','D','E','F','G','H']:
        d = series.filter(regex=a)
        d.name = a
        d.index = np.arange(1,13,1)
        outdf = outdf.append(d)
    return outdf

def save_xls(dict):
    for key,df in dict.items():
        df.to_excel('OD_{}.xlsx'.format(key))

dict_df = {} # store df of each items (mean, stdev etc) in this dict
for name,series in data_df.iterrows():
    dict_df[name] = convert_to_96_sheet(series)

dict_df['CV'] = dict_df['StDev'] / dict_df['Mean']

save_xls(dict_df)
