#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:28:44 2021

@author: vrushali
"""


#Plan of action - 
#-get the symbols by data scraping
#-get data from yfiannce
#-get highly correlated pairs
#-find highly cointegrated pairs from high correlation pairs

import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.tsa.stattools

#this the url on yahoo finance which has all the pharma stocks listed 25 at a time
#hence we will have to loop through all the pages to get the symbol of all the pharma stocks
url ='https://finance.yahoo.com/screener/unsaved/bc105bad-a0a2-4e16-bd3e-884c0b2771ad?count=25&dependentField=sector&dependentValues=Healthcare&offset=50'

l=np.arange(0,226,25)
list_webpages = []
for i in range(len(l)):
    url = 'https://finance.yahoo.com/screener/unsaved/bc105bad-a0a2-4e16-bd3e-884c0b2771ad?count=25&dependentField=sector&dependentValues=Healthcare&offset=' + str(l[i])
    list_webpages.append(url)


symbol = pd.Series([1])
for i in range(len(list_webpages)):
    df_list = pd.read_html(list_webpages[i])
    symbol = pd.concat([symbol, df_list[0]["Symbol"]], ignore_index = True)

symbol = pd.DataFrame(symbol)
symbol = symbol.drop(0)
symbol = symbol.rename(columns={0: "Symbol"})
