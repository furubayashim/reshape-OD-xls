#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
import os

if len(sys.argv) >1:
    samplefile = sys.argv[1]
else:
    print("enter file name")

output_folder = 'xlsx/'
if not os.path.exists(output_folder):os.makedirs(output_folder)

df = pd.read_excel(samplefile)

# find "Well" in the sheet and remake data
data_index = (df.iloc[:,0] == 'Well').idxmax()
data_df = df.iloc[data_start+1:-2,1:]
well_label = df.iloc[data_index,1:].values
col_label = df.iloc[data_start+1:-2,0].values
data_df.columns = well_label
data_df.index = col_label
data_df

def convert_to_96_sheet(series):
    outdf = pd.DataFrame()
    for a in ['A','B','C','D','E','F','G','H']:
        d = series.filter(regex=a)
        d.name = a
        d.index = np.arange(1,13,1)
        outdf = outdf.append(d)
    outdf.to_excel('{}OD_{}.xlsx'.format(output_folder,series.name))
    return outdf

for name,series in data_df.iterrows():
    convert_to_96_sheet(series)
