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


def read_stock_data(file_name):
    """
    Reads stock data from a JSON formatted file and computes the average stock value for each month
    :param file_name: The name of a JSON formatted file that contains stock data for analysis
    :return: A list of tuples containing dates (month-year) and corresponding monthly stock averages
    """

    monthly_volumes = []
    monthly_sales = []

    try:
        with open(file_name, "r") as file_reader:
            input_file = file_reader.read()
            input_file = json.loads(input_file)
    except FileNotFoundError:
        raise FileNotFoundError
    except ValueError:
        raise ValueError("File content is invalid")

    for i in range(len(input_file)):
        date = input_file[i]["Date"][:7]
        volume = input_file[i]["Volume"]
        close = input_file[i]["Close"]
        sales = volume * close
        volume_tuple = (date, volume)
        sales_tuple = (date, sales)
        monthly_volumes.append(volume_tuple)
        monthly_sales.append(sales_tuple)

    averages_dict = defaultdict(float)  # to hold monthly averages
    sales_dict = defaultdict(float)  # to hold monthly sales

    # add volume and sales values to corresponding months in averages and sales dictionaries
    for month, volume in monthly_volumes:
        averages_dict[month] += volume  # iterate and sum the volumes
    for month, sales in monthly_sales:
        sales_dict[month] += sales  # iterate and sum the sales
    for month, average in averages_dict.items():
        try:  # check for months where the sum of all volumes is zero
            averages_dict[month] = float("{0:.2f}".format(sales_dict[month] / averages_dict[month]))  # compute average
        except ZeroDivisionError:
            averages_dict[month] = 0  # if division by zero occurs, set monthly average to 0 and continue
    results_list = averages_dict.items()  # add dictionary items to results list
    return results_list  # return results as a list of tuples


def six_best_months(results_list):
    """
    Receives a list of tuples containing dates and monthly stock averages, sorts in descending order and returns the
    first six results in the list
    :param results_list: list of tuples containing dates (month-year) and corresponding monthly stock averages
    :return: results_list_best: list containing the top six results from the results list
    """
    results_list_best = sorted(results_list, key=itemgetter(1), reverse=True)[0:6]  # sort averages in descending order
    return results_list_best


def six_worst_months(results_list):
    """
    Receives a list of tuples containing dates and monthly stock averages, sorts in ascending order and returns the
    first six results in the list
    :param results_list: list of tuples containing dates (month-year) and corresponding monthly stock averages
    :return: results_list_worst: list containing the top six results from the results list
    """
    results_list_worst = sorted(results_list, key=itemgetter(1))[0:6]  # sort averages in ascending order
    return results_list_worst
