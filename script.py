# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:44:22 2017

@author: dulrich@kargo.com
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# graphing tools
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

# plotly
import plotly
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go
from plotly.graph_objs import *

# dont truncate text
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv("littlethings.csv")

print(df.describe())

max_imps = df.max()["IMPRESSIONS"]
# mean is commented out because it eats up CPU time for whatever reason
#mean_imps = df.mean()["IMPRESSIONS"]
std_imps = df.std()["IMPRESSIONS"]

print("\nMost popular article:")
print(df.iloc[[df['IMPRESSIONS'].argmax()]])

# display histogram in buckets based off of max, mean or std of impressions
num_buckets = 10

# this is a custom offset to see other ranges outside the center of the data
start = 0
step = max_imps / num_buckets

bin_range = np.arange(start, max_imps+step + 1, step)
out, bins  = pd.cut(df['IMPRESSIONS'], bins=bin_range, include_lowest=True, right=False, retbins=True)
print(out.value_counts(sort=False))
out.value_counts(sort=False).plot.bar(title="Normalized Distribution").set(xlabel="Impressions", ylabel="Count")