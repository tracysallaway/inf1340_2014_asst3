#!/usr/bin/env python3

""" Docstring """

__author__ = 'Jodie Church, Tania Misquitta, Tracy Sallaway'
__email__ = "jodie.church@mail.utoronto.ca, tania.misquitta@mail.utoronto.ca, tracy.armstrong@mail.utoronto.ca"

__copyright__ = "2014 JodieChurch_TaniaMisquitta_TracySallaway"
__license__ = "Jodie_Tania_Tracy License"

__status__ = "Prototype"

# imports one per line
from mining import *


def test_goog():
    read_stock_data(read_json_from_file(file_name))
    assert six_best_months(six_best_months(results_list)) == [('2007-12', 693.76), ('2007-11', 676.55), ('2007-10', 637.38), ('2008-01', 599.42),
                                 ('2008-05', 576.29), ('2008-06', 555.34)]

    assert six_worst_months(six_worst_months(results_list)) == [('2004-08', 104.66), ('2004-09', 116.38), ('2004-10', 164.52), ('2004-11', 177.09), ('2004-12', 181.01),
                                  ('2005-03', 181.18)]

