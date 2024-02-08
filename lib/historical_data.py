import yfinance as yf
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

def plot_hist_data(hist_data):
    mpf.plot(hist_data[['Open','High','Low','Close']],
             addplot=mpf.make_addplot(hist_data[['MACD', 'SGN']],panel=1,title='MACD'),
             type='candle',
             style='yahoo',
             tight_layout=True)

def get_hist_data(ticker, months):
    hist_data=ticker.history(period=f'{months}mo')
    hist_data['EMA12']=hist_data['Close'].ewm(span=12, adjust=False).mean()
    hist_data['EMA26']=hist_data['Close'].ewm(span=26, adjust=False).mean()
    hist_data['MACD']=hist_data['EMA12']-hist_data['EMA26']
    hist_data['SGN']=hist_data['MACD'].ewm(span=9, adjust=False).mean()
    return hist_data

def Analyse(hist_data):
    hist_data['MACDSGN']=hist_data['MACD']-hist_data['SGN']
    if (hist_data['MACDSGN'].iloc[-1] > 0):
        return 1
    if (hist_data['MACDSGN'].iloc[-1] < 0):
        return -1
    if (hist_data['MACDSNG'].iloc[-1] ==0):
        if (hist_data['MACDSGN'].iloc[-2] > 0):
            return 2
        if (hist_data['MACDSGN'].iloc[-2] < 0):
            return -2
        else:
            return 0

