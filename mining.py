#!/usr/bin/env python3

""" Docstring """

__author__ = 'Jodie Church, Tania Misquitta, Tracy Sallaway '
__email__ = "jodie.church@mail.utoronto.ca, tania.misquitta@mail.utoronto.ca, tracy.armstrong@mail.utoronto.ca"

__copyright__ = "2014 JodieChurch_TaniaMisquitta_TracySallaway"
__license__ = "Jodie_Tania_Tracy License"

__status__ = "Prototype"

# imports one per line
import json
from collections import defaultdict
from operator import itemgetter


monthly_volumes = []
monthly_sales = []
file_name = "data/GOOG.json"


def read_json_from_file(file_name):
    with open(file_name, "r") as file_reader:
        file_contents = file_reader.read()
        input_file = json.loads(file_contents)

    return input_file


def read_stock_data(input_file):

    for i in range(len(input_file)):
        date = input_file[i]["Date"][:7]
        volume = input_file[i]["Volume"]
        close = input_file[i]["Close"]
        sales = volume * close
        volume_tuple = (date, volume)
        sales_tuple = (date, sales)
        monthly_volumes.append(volume_tuple)
        monthly_sales.append(sales_tuple)
        averages_dict = defaultdict(float)  # to hold the running sum per date
        sales_dict = defaultdict(float)


#add values to 'yyyy/mm' formatted month to get monthly volumes
    for month, value in monthly_volumes:
        averages_dict[month] += value

 #add values to 'yyyy/mm' formatted month to get monthly sales
    for month, value in monthly_sales:
        sales_dict[month] += value  


 #to calculate monthly averages for  'yyyy/mm' formatted month
    for month, value in averages_dict.items():
        averages_dict[month] = float("{0:.2f}".format(sales_dict[month] / averages_dict[month]))
        results_list = averages_dict.items()
        return sorted(results_list, key=itemgetter(1))


def six_best_months(results_list):
    results_list_best = sorted(results_list, key=itemgetter(1), reverse=True)[0:6]
    return results_list_best


def six_worst_months(results_list):
    results_list_worst = sorted(results_list, key=itemgetter(1))[0:6]
    return results_list_worst

input_file = read_json_from_file(file_name)
results_list = read_stock_data(input_file)
results_list_worst = six_worst_months(results_list)
results_list_best = six_best_months(results_list)

