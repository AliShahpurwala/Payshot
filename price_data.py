from pandas_datareader import data as wb
import numpy as np
ticker1 = 'WMT'
ticker1_price_list = wb.DataReader(ticker1, data_source = 'yahoo', start = '2020-01-01')['Adj Close']