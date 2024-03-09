import yfinance as yf
import current_data

class APIKey:
    def __init__(self):
        self.isValid=True
        self.netIncome=None
        self.orders=[]
    def placeOrder(self, OrderTickect):
        self.orders.append(OrderTickect)

class OrderTickect:
    def __init__(self, ticker):
        self.ticker=ticker
        self.call=None
        self.price=None
        self.volume=None
        self.isOpen=False
    def sell_order(self, APIKey, volume):
        if (self.call == None):
            self.price=current_data.get_curr_price(self.ticker)
            self.volume=volume
            self.call="SELL"
            APIKey.placeOrder(self)
            self.isOpen=True
            return
        elif (self.call == "BUY"):
            if (self.isOpen):
                if (APIKey.netIncome == None):
                    APIKey.netIncome=self.price-current_data.get_curr_price(self.ticker)
                    self.volume = 0
                    self.isOpen=False
                    return
                else:
                    APIKey.netIncome+=self.price-current_data.get_curr_price(self.ticker)
                    self.isOpen=False
                    return
            else:
                return
        elif (self.call=="SELL"):
            if (self.isOpen):
                self.volume += volume
                return
            else:
                return
        return
    def buy_order(self, APIKey, volume):
        if (self.call == None):
            self.price=current_data.get_curr_price(self.ticker)
            self.volume=volume
            self.call="BUY"
            APIKey.placeOrder(self)
            self.isOpen=True
            return
        elif (self.call == "SELL"):
            if (self.isOpen):
                if (APIKey.netIncome == None):
                    APIKey.netIncome=current_data.get_curr_price(self.ticker)-self.price
                    self.volume = 0
                    self.isOpen=False
                    return
                else:
                    APIKey.netIncome+=current_data.get_curr_price(self.ticker)-self.price
                    self.isOpen=False
                    return
            else:
                return
        elif (self.call=="BUY"):
            if (self.isOpen):
                self.volume += volume
                return
            else:
                return
        return
