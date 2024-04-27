import pandas as pd
import numpy as np
import yfinance as yf
from prophet import Prophet
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import datetime
from datetime import date,timedelta




stocks = {"ONGC":"ONGC.NS","OIL":"OIL.NS","HPCL":"HINDPETRO.NS","BPCL":"BPCL.NS","SLB":"SLB","Weatherford":"WFRD","Halliburton":"HAL","Baker Hughes":"BKR","Exxon Mobil":"XOM","Shell":"SHEL"}
keys = list(stocks.keys())
demo_name = st.selectbox("Choose company",keys)

today = date.today()
yesterday = today-timedelta(days=1)
yesterday_date = yesterday.strftime("%Y-%m-%d")

stock_ONGC = yf.download(stocks['ONGC'],start="2014-01-01",end=yesterday_date)
stock_OIL = yf.download(stocks['OIL'],start="2014-01-01",end=yesterday_date)
stock_HINDPETRO = yf.download(stocks['HPCL'],start="2014-01-01",end=yesterday_date)
stock_BPCL = yf.download(stocks['BPCL'],start="2014-01-01",end=yesterday_date)
stock_SLB = yf.download(stocks['SLB'],start="2014-01-01",end=yesterday_date)
stock_WFD = yf.download(stocks['Weatherford'],start="2014-01-01",end=yesterday_date)
stock_HLB = yf.download(stocks['Halliburton'],start="2014-01-01",end=yesterday_date)
stock_BKR = yf.download(stocks['Baker Hughes'],start="2014-01-01",end=yesterday_date)
stock_XOM = yf.download(stocks['Exxon Mobil'],start="2014-01-01",end=yesterday_date)
stock_Shell = yf.download(stocks['Shell'],start="2014-01-01",end=yesterday_date)


stock_ONGC.reset_index(inplace=True)
stock_OIL.reset_index(inplace=True)
stock_HINDPETRO.reset_index(inplace=True)
stock_BPCL.reset_index(inplace=True)
stock_SLB.reset_index(inplace=True)
stock_WFD.reset_index(inplace = True)
stock_HLB.reset_index(inplace = True)
stock_BKR.reset_index(inplace = True)
stock_XOM.reset_index(inplace = True)
stock_Shell.reset_index(inplace = True)

def forecast_func(input,col):
  input = input.rename(columns={'Date':'ds',col:'y'})
  model = Prophet()
  model.fit(input)
  forecast = model.predict(model.make_future_dataframe(periods=30))
  future = pd.DataFrame(forecast[['ds','yhat']])
  future = future.rename(columns={'ds':'Date','yhat':col})
  return future

ONGC_Open = forecast_func(stock_ONGC[['Date','Open']],'Open')
ONGC_Close = forecast_func(stock_ONGC[['Date','Close']],'Close')
ONGC_High = forecast_func(stock_ONGC[['Date','High']],'High')
ONGC_Low = forecast_func(stock_ONGC[['Date','Low']],'Low')


OIL_Open = forecast_func(stock_OIL[['Date','Open']],'Open')
OIL_Close = forecast_func(stock_OIL[['Date','Close']],'Close')
OIL_High = forecast_func(stock_OIL[['Date','High']],'High')
OIL_Low = forecast_func(stock_OIL[['Date','Low']],'Low')

HINDPETRO_Open = forecast_func(stock_HINDPETRO[['Date','Open']],'Open')
HINDPETRO_Close = forecast_func(stock_HINDPETRO[['Date','Close']],'Close')
HINDPETRO_High = forecast_func(stock_HINDPETRO[['Date','High']],'High')
HINDPETRO_Low = forecast_func(stock_HINDPETRO[['Date','Low']],'Low')

BPCL_Open = forecast_func(stock_BPCL[['Date','Open']],'Open')
BPCL_Close = forecast_func(stock_BPCL[['Date','Close']],'Close')
BPCL_High = forecast_func(stock_BPCL[['Date','High']],'High')
BPCL_Low = forecast_func(stock_BPCL[['Date','Low']],'Low')

SLB_Open = forecast_func(stock_SLB[['Date','Open']],'Open')
SLB_Close = forecast_func(stock_SLB[['Date','Close']],'Close')
SLB_High = forecast_func(stock_SLB[['Date','High']],'High')
SLB_Low = forecast_func(stock_SLB[['Date','Low']],'Low')

WFD_Open = forecast_func(stock_WFD[['Date','Open']],'Open')
WFD_Close = forecast_func(stock_WFD[['Date','Close']],'Close')
WFD_High = forecast_func(stock_WFD[['Date','High']],'High')
WFD_Low = forecast_func(stock_WFD[['Date','Low']],'Low')

HLB_Open = forecast_func(stock_HLB[['Date','Open']],'Open')
HLB_Close = forecast_func(stock_HLB[['Date','Close']],'Close')
HLB_High = forecast_func(stock_HLB[['Date','High']],'High')
HLB_Low = forecast_func(stock_HLB[['Date','Low']],'Low')

BKR_Open = forecast_func(stock_BKR[['Date','Open']],'Open')
BKR_Close = forecast_func(stock_BKR[['Date','Close']],'Close')
BKR_High = forecast_func(stock_BKR[['Date','High']],'High')
BKR_Low = forecast_func(stock_BKR[['Date','Low']],'Low')

XOM_Open = forecast_func(stock_XOM[['Date','Open']],'Open')
XOM_Close = forecast_func(stock_XOM[['Date','Close']],'Close')
XOM_High = forecast_func(stock_XOM[['Date','High']],'High')
XOM_Low = forecast_func(stock_XOM[['Date','Low']],'Low')

Shell_Open = forecast_func(stock_Shell[['Date','Open']],'Open')
Shell_Close = forecast_func(stock_Shell[['Date','Close']],'Close')
Shell_High = forecast_func(stock_Shell[['Date','High']],'High')
Shell_Low = forecast_func(stock_Shell[['Date','Low']],'Low')


forecast_table_ONGC = pd.merge((pd.merge((pd.merge(ONGC_Open,ONGC_Close,on='Date')),ONGC_Low,on='Date')),ONGC_High,on='Date')
forecast_table_ONGC['Company'] = 'ONGC'
forecast_table_OIL = pd.merge((pd.merge((pd.merge(OIL_Open,OIL_Close,on='Date')),OIL_Low,on='Date')),OIL_High,on='Date')
forecast_table_OIL['Company'] = 'OIL'
forecast_table_HINDPETRO = pd.merge((pd.merge((pd.merge(HINDPETRO_Open,HINDPETRO_Close,on='Date')),HINDPETRO_Low,on='Date')),HINDPETRO_High,on='Date')
forecast_table_HINDPETRO['Company'] = 'HPCL'
forecast_table_BPCL = pd.merge((pd.merge((pd.merge(BPCL_Open,BPCL_Close,on='Date')),BPCL_Low,on='Date')),BPCL_High,on='Date')
forecast_table_BPCL['Company'] = 'BPCL'
forecast_table_SLB = pd.merge((pd.merge((pd.merge(SLB_Open,SLB_Close,on='Date')),SLB_Low,on='Date')),SLB_High,on='Date')
forecast_table_SLB['Company'] = 'SLB'
forecast_table_WFD = pd.merge((pd.merge((pd.merge(WFD_Open,WFD_Close,on='Date')),WFD_Low,on='Date')),WFD_High,on='Date')
forecast_table_WFD['Company'] = 'Weatherford'
forecast_table_HLB = pd.merge((pd.merge((pd.merge(HLB_Open,HLB_Close,on='Date')),HLB_Low,on='Date')),HLB_High,on='Date')
forecast_table_HLB['Company'] = 'Halliburton'
forecast_table_BKR = pd.merge((pd.merge((pd.merge(BKR_Open,BKR_Close,on='Date')),BKR_Low,on='Date')),BKR_High,on='Date')
forecast_table_BKR['Company'] = 'Baker Hughes'
forecast_table_XOM = pd.merge((pd.merge((pd.merge(XOM_Open,XOM_Close,on='Date')),XOM_Low,on='Date')),XOM_High,on='Date')
forecast_table_XOM['Company'] = 'Exxon Mobil'
forecast_table_Shell = pd.merge((pd.merge((pd.merge(Shell_Open,Shell_Close,on='Date')),Shell_Low,on='Date')),Shell_High,on='Date')
forecast_table_Shell['Company'] = 'Shell'



combined_table = pd.concat([forecast_table_ONGC,forecast_table_OIL,forecast_table_HINDPETRO,forecast_table_BPCL,forecast_table_SLB,forecast_table_WFD,forecast_table_HLB,forecast_table_BKR,forecast_table_XOM,forecast_table_Shell])


selected_table=combined_table[combined_table['Company']==demo_name]

fig = go.Figure((go.Candlestick(x=selected_table['Date'],
              open = selected_table['Open'], high=selected_table['High'],
              low=selected_table['Low'],
              close=selected_table['Close'])))
st.plotly_chart(fig)
