import historical_data
import yfinance as yf

tsla=yf.Ticker("INFY")
data=historical_data.get_hist_data(tsla, 12)
historical_data.plot_hist_data(data)
print(historical_data.Analyse(data))
