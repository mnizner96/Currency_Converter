#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
# Author: Martin Nizner
# Date: 05/2018
# File: CLI using Flask


import argparse
import sys

from shared_functions import get_data, json_output_format

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--amount', type=float, required=True, help="amount to convert", dest="amount")
    parser.add_argument('--input_currency', type=str, required=True, help="input currency to convert", dest="input_curr")
    parser.add_argument('--output_currency', type=str, required=False, help="converted currency from input", dest="output_curr")
    args = parser.parse_args()
    all_curr_xml = get_data()
    cli_output = json_output_format(args, all_curr_xml)
    if cli_output == 1:
        sys.stderr.write("Error, wrong input currency")
        sys.exit(1)
    elif cli_output == 2:
        sys.stderr.write("Error, wrong output currency")
        sys.exit(2)
    elif cli_output == 3:
        sys.stderr.write("Error, amount has a negative value")
        sys.exit(3)
    print(cli_output)
    sys.exit(0)
