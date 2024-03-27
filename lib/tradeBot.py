from place_order import * 
import historical_data

class TradeBot:
    def __init__(self, APIKey):
        self.APIkey=APIKey
        self.watchlist=[]
        self.executedBuy=[]
        self.executedSell=[]
    def addWatchList(self, ticker):
        self.watchlist.append(ticker)
        hist_call=historical_data.Analyse(historical_data.get_hist_data(ticker))
        if (hist_call=="BUY"):
            buyTicket=OrderTickect(ticker)
            buyTicket.buy_order(self.APIkey, 10)
            self.executedBuy.append(buyTicket)
        elif (hist_call=="SELL"):
            sellTicket=OrderTickect(ticker)
            sellTicket.sell_order(self.APIkey, 10)
            self.executedSell.append(sellTicket)           
        return
    def refresh(self):
        for i in self.executedBuy:
            hist_call=historical_data.Analyse(historical_data.get_hist_data(i.ticker))
            if (hist_call=="SELL"):
                i.sell_order(self.APIkey, 10)
                self.executedBuy.remove(i)

        for i in self.executedSell:
            hist_call=historical_data.Analyse(historical_data.get_hist_data(i.ticker))
            if (hist_call=="BUY"):
                i.buy_order(self.APIkey, 10)
                self.executedBuy.remove(i)

        return
    
    def getPL(self):
        return self.APIkey.netIncome