import pandas as pd
import numpy as np
import yfinance as yf
from prophet import Prophet
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

option = st.selectbox("Pick one", ["ONGC", "Vedanta Limited","OIL","HPCL","BPCL"])

stocks = ["VEDL.NS","ONGC.NS","OIL.NS","HINDPETRO.NS","BPCL.NS"]
stock_ONGC = yf.download(stocks[0],start="2014-01-01",end="2024-01-01")
stock_VEDL = yf.download(stocks[1],start="2014-01-01",end="2024-01-01")
stock_OIL = yf.download(stocks[2],start="2014-01-01",end="2024-01-01")
stock_HINDPETRO = yf.download(stocks[3],start="2014-01-01",end="2024-01-01")
stock_BPCL = yf.download(stocks[4],start="2014-01-01",end="2024-01-01")

stock_ONGC.reset_index(inplace=True)
stock_VEDL.reset_index(inplace=True)
stock_OIL.reset_index(inplace=True)
stock_HINDPETRO.reset_index(inplace=True)
stock_BPCL.reset_index(inplace=True)

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

VEDL_Open = forecast_func(stock_VEDL[['Date','Open']],'Open')
VEDL_Close = forecast_func(stock_VEDL[['Date','Close']],'Close')
VEDL_High = forecast_func(stock_VEDL[['Date','High']],'High')
VEDL_Low = forecast_func(stock_VEDL[['Date','Low']],'Low')

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

forecast_table_ONGC = pd.merge((pd.merge((pd.merge(ONGC_Open,ONGC_Close,on='Date')),ONGC_Low,on='Date')),ONGC_High,on='Date')
forecast_table_ONGC['Company'] = 'ONGC'
forecast_table_Vedanta = pd.merge((pd.merge((pd.merge(VEDL_Open,VEDL_Close,on='Date')),VEDL_Low,on='Date')),VEDL_High,on='Date')
forecast_table_Vedanta['Company'] = 'Vedanta Limited'
forecast_table_OIL = pd.merge((pd.merge((pd.merge(OIL_Open,OIL_Close,on='Date')),OIL_Low,on='Date')),OIL_High,on='Date')
forecast_table_OIL['Company'] = 'OIL'
forecast_table_HINDPETRO = pd.merge((pd.merge((pd.merge(HINDPETRO_Open,HINDPETRO_Close,on='Date')),HINDPETRO_Low,on='Date')),HINDPETRO_High,on='Date')
forecast_table_HINDPETRO['Company'] = 'HPCL'
forecast_table_BPCL = pd.merge((pd.merge((pd.merge(BPCL_Open,BPCL_Close,on='Date')),BPCL_Low,on='Date')),BPCL_High,on='Date')
forecast_table_BPCL['Company'] = 'BPCL'

combined_table = forecast_table_ONGC.append(forecast_table_Vedanta)
combined_table = combined_table.append(forecast_table_OIL)
combined_table = combined_table.append(forecast_table_HINDPETRO)
combined_table = combined_table.append(forecast_table_BPCL)
stock_price_data = combined_table

filtered_data = stock_price_data[stock_price_data['Company']==option]

fig = go.Figure()
fig.add_trace(go.Candlestick(x=filtered_data['Date'],
              open = filtered_data['Open'], high=filtered_data['High'],
              low=filtered_data['Low'],
              close=filtered_data['Close']))

st.plotly_chart(fig)
