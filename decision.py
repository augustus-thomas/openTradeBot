class Decision:
    def __init__(self):
        self.list = {
            "ticker" : "TEST",
            "entry-price" : 0,
            "exit-price" : 0,
            "certainty" : 0,
        }

        self.test_var = "test_var"

    def rating(self, ticker="", historical_data={}, **entry_params):
        certainty = "0"
        return certainty

    def buy_condition():
        pass

    def sell_condition():
        pass
    
    def __name__(self):
        return self.test_var