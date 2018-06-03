#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
# Author: Martin Nizner
# Date: 05/2018
# File: API using Flask


from flask import Flask
from flask import Response
from flask import request
from shared_functions import get_data, json_output_format, json
app = Flask(__name__)


class Arguments(object):
    def __init__(self, amount, output_curr, input_curr):
        self.amount = amount
        self.output_curr = output_curr
        self.input_curr = input_curr


@app.route("/currency_converter")
def convert_currency():
    arguments = Arguments(request.args.get('amount'), request.args.get('output_currency'), request.args.get('input_currency'))
    all_curr_xml = get_data()
    api_output = json_output_format(arguments, all_curr_xml)
    if api_output == 1:
        status_code = 201
        err_msg = 'Error, wrong input currency'
    elif api_output == 2:
        status_code = 202
        err_msg = 'Error, wrong output currency'
    elif api_output == 3:
        status_code = 203
        err_msg = 'Error, amount has a negative value'
    else:
        return Response(response=api_output, status=200, mimetype='application/json') #no error 
    return Response(response=json.dumps({'error': {'message': err_msg, 'status_code': status_code}}, sort_keys=False, indent=4), status=status_code, mimetype='application/json')
    

if __name__ == '__main__':
    app.run()
