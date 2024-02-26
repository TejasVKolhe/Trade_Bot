import yfinance as yf
import historical_data

def get_curr_price(ticker):
    return ticker.history(period='1d', interval='1m').tail().iloc[0]['Close']

def get_curr_price_data(ticker, curr_interval):    
    curr_data=ticker.history(period='1d', interval=f"{curr_interval}")
    curr_data['EMA12']=hist_data['Close'].ewm(span=12, adjust=False).mean()
    curr_data['EMA26']=hist_data['Close'].ewm(span=26, adjust=False).mean()
    curr_data['MACD']=hist_data['EMA12']-hist_data['EMA26']
    curr_data['SGN']=hist_data['MACD'].ewm(span=9, adjust=False).mean()
    return curr_data


def plot_curr_data(hist_data):
    mpf.plot(curr_data[['Open','High','Low','Close']],
             addplot=mpf.make_addplot(curr_data[['MACD', 'SGN']],panel=1,title='MACD'),
             type='candle',
             style='yahoo',
             tight_layout=True)

def Analyse(hist_data):
    curr_data['MACDSGN']=curr_data['MACD']-curr_data['SGN']
    if (curr_data['MACDSGN'].iloc[-1] > 0):
        return 1
    if (curr_data['MACDSGN'].iloc[-1] < 0):
        return -1
    if (curr_data['MACDSNG'].iloc[-1] ==0):
        if (curr_data['MACDSGN'].iloc[-2] > 0):
            return 2
        if (curr_data['MACDSGN'].iloc[-2] < 0):
            return -2
        else:
            return 0

