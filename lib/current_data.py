import yfinance as yf

def get_curr_price(ticker):
    return ticker.history(period='1d', interval='1m').tail().iloc[0]['Close']
