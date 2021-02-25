#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:14:31 2021

@author: vrushali
"""


import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.tsa.stattools

#getting the stock symbols for all pharma stocks 
st_symbols = pd.read_csv("/home/vrushali/Documents/PCA/Pharma Stock Symbols from NSE and BSE.csv")

l=[]
for i in range(len(st_symbols)):
    l.append(st_symbols["Symbol"][i])

data = yf.download(l, start = '2018-01-01', end = '2018-12-31')

close = data["Adj Close"]

correlation = []
for i in range(close.shape[1]):
    for j in range(i+1, close.shape[1]):
        c = np.corrcoef(close[close.columns[i]], close[close.columns[j]])[0,1]
        correlation.append(c)
        
stock1 = []
stock2 = []
for i in range(close.shape[1]):
    for j in range(i+1,close.shape[1]):
        stock1.append(close.columns[i])
        stock2.append(close.columns[j])
        
corr_mat = pd.DataFrame({"Stock1":stock1, "Stock2":stock2, "Correlation":correlation})

corr_8 = corr_mat[corr_mat["Correlation"]>0.8].reset_index()
del corr_8["index"]

Cointegration = []
for i in range(corr_8.shape[0]):
    k = statsmodels.tsa.stattools.coint(close[corr_8["Stock1"][i]], close[corr_8["Stock2"][i]])[1]
    Cointegration.append(k)

corr_8["Cointegration"] = Cointegration

high_coin = corr_8[corr_8["Cointegration"]<0.05]
high_coin.reset_index()

high_coin["Correlation"].nlargest()

high_coin.sort_values(by=["Correlation"])














