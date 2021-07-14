# -*- coding: utf-8 -*-
"""
Created on Thurs Apr 20 17:52:31 2020

@author: Debopriya Bhattacharya, Parth Shah
"""

#Here is a Function which creates graph for Number of Talks Vs the Published_Year.

import matplotlib.pyplot as plt
import seaborn as sns

def pubYearPlot(dataset):
    plt.figure(figsize=(15,5))
    sns.countplot(dataset["published_year"])
    plt.savefig("pyp.png")
#%%