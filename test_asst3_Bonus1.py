__author__ = 'jodiechurch'

#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import asst3_Bonus1


def test_class():
    google = asst3_Bonus1.StockMiner("GOOG", "GOOG.json")
    google.month_averages()
    assert google.six_best_months() == []


