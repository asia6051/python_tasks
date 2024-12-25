# ----------------------------- TASK 1 ---------------------------------
"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    calculate_days('2021-10-05')
    1
    calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime, date


class WrongStringPattern(Exception):
    def __init__(self, message):
        self.message = message


def calculate_days(from_date: str):
    try:
        flag = bool(datetime.strptime(from_date, '%Y-%m-%d'))
    except ValueError:
        flag = False

    if flag:
        custom_date = datetime.strptime(from_date, '%Y-%m-%d')
        now = datetime.now()
        diff = now - custom_date
        return diff.days

    else:
        raise WrongStringPattern("String is not in yyyy-mm-dd format")


try:
    print(calculate_days('2024-06-11'))
except WrongStringPattern as e:
    print(f"{e.message}")

try:
    print(calculate_days('2024-06-09'))
except WrongStringPattern as e:
    print(f"{e.message}")

try:
    print(calculate_days('10-06-2024'))
except WrongStringPattern as e:
    print(f"{e.message}")


# --------------------------- TASK 2 ----------------------------------
"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     math_calculate('log', 1024, 2)
     10.0
     math_calculate('ceil', 10.7)
     11
"""
import math


def math_calculate(function: str, *args):
    func = getattr(math, function)
    return func(*args)


print(math_calculate('log', 1024, 2))
print(math_calculate('ceil', 10.7))


# ----------------------------- TASK 3 -----------------------------------
"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    is_http_domain('http://wikipedia.org')
    True
    is_http_domain('https://ru.wikipedia.org/')
    True
    is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    pattern = r"^https?:\/\/[\w.-]+\/?$"
    answer = bool(re.search(pattern, domain))
    return answer


print(is_http_domain('http://wikipedia.org'))
print(is_http_domain('https://ru.wikipedia.org/'))
print(is_http_domain('griddynamics.com'))

# ---------------------- TASK 4 - NIE DZIALA ----------------------------
"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
from faker import Faker


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()

    for _ in range(args.NUMBER):
        record = {}
        for field in args.fields:
            field_name, provider_name = field.split('=')
            provider = getattr(fake, provider_name)
            record[field_name] = provider()
        print(record)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake data.")
    parser.add_argument('NUMBER', type=int, help="Number of instances to generate.")
    parser.add_argument('--fields', nargs='+', required=True,
                        help="Fields and their providers in FIELD=PROVIDER format.")

    args = parser.parse_args()
    print_name_address(args)


# ----------------------------- TASK 5 ------------------------------------
"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
import urllib
from urllib.request import urlopen
import ssl


def make_request(url: str):
    # Ceryfikat SSL, bez niego nie dziala:
    https_tls_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLS))
    opener = urllib.request.build_opener(https_tls_handler)
    urllib.request.install_opener(opener)
    response = urlopen(url)

    status_code = response.getcode()
    decoded_response = response.read().decode('ISO-8859-1')
    return Tuple[status_code,decoded_response]


print(make_request('https://www.google.com'))