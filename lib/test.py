import historical_data
from place_order import *
import yfinance as yf

ticker=input("Ticker: ")

tsla=yf.Ticker(ticker)

key=APIKey()
tsla_data=historical_data.get_hist_data(tsla, 2)
historical_data.plot_hist_data(tsla_data)
res=historical_data.Analyse(tsla_data)

order1=OrderTickect(tsla)
if (res > 0):
    print("trying to execute buy order")
    order1.buy_order(key, res*10)
elif (res < 0):
    print("trying to execute sell order")
    order1.sell_order(key, res*10)

for i in range(len(key.orders)):
    print(f"order call : {key.orders[i].call}")
    print(f"price at: {key.orders[i].price}")

