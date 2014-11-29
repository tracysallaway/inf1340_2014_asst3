""" Docstring """

__author__ = 'Jodie Church, Tania Misquitta, Tracy Sallaway '
__email__ = "jodie.church@mail.utoronto.ca, tania.misquitta@mail.utoronto.ca, tracy.armstrong@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

class StockMiner:

    def __init__(self, name, data_file_name):
        self.name = name
        self.data_file_name = data_file_name

    def month_averages(self):
        #calculate monthly
        pass

    def six_best_months(self):
        pass

    def __eq__(self, other):
        isinstance(other, Book)


google = StockMiner("GOOG", "GOOG.json")
google.month_averages()
google.six_best_months()

apple = StockMiner("APPL", "apple.json")
apple.month_averages()
apple.six_best_months()

apple == google
# apple.__eq__(self, google)