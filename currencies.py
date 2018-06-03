#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
# Author: Martin Nizner
# Date: 05/2018
# File: currencies for mapping symbol to 3 letter currency code


def symbol_to_currency(currency):
    return {
        '€': 'EUR',
        '$': 'USD',
        'AU$': 'AUD',
        '¥': 'JPY',
        'лs': 'BGN',
        'Kč': 'CZK',
        'kr': 'DKK',
        '£': 'GBP',
        'Ft': 'HUF',
        'zł': 'PLN',
        'lei': 'RON',
        'CHF': 'CHF',
        'kn': 'HRK',
        '₽': 'RUB',
        '₺': 'TRY',
        'R$': 'BRL',
        'Rp': 'IDR',
        '₪': 'ILS',
        '₹': 'INR',
        '₩': 'KRW',
        'RM': 'MYR',
        '₱': 'PHP',
        '฿': 'THB',
        'R': 'ZAR'
    }.get(currency)
