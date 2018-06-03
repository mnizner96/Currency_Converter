#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
# Author: Martin Nizner
# Date: 05/2018
# File: Shared functions for both Cli and Api


import json
import requests

from currencies import symbol_to_currency


def json_output_format(arguments, root_tree):
    arguments.amount = float(arguments.amount)
    if arguments.amount < 0:
        return 3
    namespaces = {'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}  #namespaces of the remote XML file
    input_data_json = {}
    output_data_json = {}
    whole_data_json = {}
    input_symbol = symbol_to_currency(arguments.input_curr)
    output_symbol = symbol_to_currency(arguments.output_curr)
    if input_symbol:  
        arguments.input_curr = input_symbol

    if output_symbol:
        arguments.output_curr = output_symbol

    if arguments.input_curr != "EUR":
        input_curr_data = root_tree.find('.//ex:Cube[@currency="{}"]'.format(arguments.input_curr), namespaces=namespaces)
        if input_curr_data is None:
            return 1
        input_rate = float(input_curr_data.attrib['rate'])
    else:
        input_rate = 1   # because courses in XML file are written against EUR

    if arguments.output_curr == 'EUR':
        output_data_json['EUR'] = "%.2f" % (float(arguments.amount) / input_rate)
    else:
        if not arguments.output_curr:
            output_curr_data = root_tree.findall('.//ex:Cube[@currency]', namespaces=namespaces)  #get all currencies from XML file
            output_data_json['EUR'] = "%.2f" % (arguments.amount / input_rate)
            for currency in output_curr_data:
                output_data_json[currency.attrib['currency']] = "%.2f" % (float(currency.attrib['rate']) / input_rate * arguments.amount)
        else:
            output_curr_data = root_tree.find('.//ex:Cube[@currency="{}"]'.format(arguments.output_curr.upper()), namespaces=namespaces)
            if output_curr_data is None:
                return 2
            output_data_rate = float(output_curr_data.attrib['rate'])
            output_data_json[output_curr_data.attrib['currency']] = "%.2f" %  (output_data_rate / input_rate * arguments.amount)

    input_data_json['amount'] = arguments.amount
    input_data_json['currency'] = arguments.input_curr
    whole_data_json['input'] = input_data_json
    whole_data_json['output'] = output_data_json
    return json.dumps(whole_data_json, sort_keys=False, indent=4)


def get_data():
    from xml.etree import ElementTree as ET
    currency_xml = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(currency_xml.raw)
    return tree.getroot()
