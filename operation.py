def calculate_profit_loss_eurusd(entry_price, exit_price, pip_value, lot_size, leverage):
    pips_difference = (exit_price - entry_price) / pip_value
    profit_loss = (pips_difference*lot_size*pip_value) * leverage

    return profit_loss

class Operation:

    def __init__(self,price,type_of_operation, pip_value, lot_size, leverage):
        self.price = price
        self.type_of_operation = type_of_operation
        self.pip_value = pip_value
        self.lot_size = lot_size
        self.leverage = leverage
    
    def stop_loss(self):
        if (self.type_of_operation=="buy"):
            stop_loss = self.price*0.97

        else:
            stop_loss = self.price*1.03

        return stop_loss
    
    def stop_gain(self):
        if (self.type_of_operation=="buy"):
            stop_gain = self.price*1.03

        else:
            stop_gain = self.price*0.97

        return stop_gain
    
    def reached_stop_gain(self,actual_price):
        if ((self.stop_gain == actual_price) or (self.stop_gain == actual_price)):
            return calculate_profit_loss_eurusd(self.price,actual_price,self.pip_value,self.lot_size,self.leverage)
        
        else:
            pass