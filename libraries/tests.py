# -------------------------- TESTS TASK 1 -------------------------------------
"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""

from tasks import calculate_days, WrongStringPattern
import pytest


def test_date_future():
    assert calculate_days('2024-06-11') == -1


def test_date_past():
    assert calculate_days('2024-06-09') == 1


def test_date_error():
    with pytest.raises(WrongStringPattern, match="String is not in yyyy-mm-dd format"):
        calculate_days('09-06-2024')


# --------------------------- TESTS TASK 2 ----------------------------------
"""
Write tests for math_calculate function
"""
from tasks import math_calculate

one_param = [
    ('ceil', 10.7, 11),
    ('log2', 8, 3),
    ('floor', 5.6, 5.0),
    ('fabs', -4.76, 4.76)
]

two_param = [
    ('log', 1024, 2, 10.0),
    ('ldexp', 3, 2, 12),
    ('comb', 5, 2, 10),
    ('copysign', 1.0, -0.0, -1.0)
]


@pytest.mark.parametrize('function_name, arg, result', one_param)
def test_math_one_param(function_name, arg, result):
    assert math_calculate(function_name, arg) == result


@pytest.mark.parametrize('function_name, arg1, arg2, result', two_param)
def test_math_two_param(function_name, arg1, arg2, result):
    assert math_calculate(function_name, arg1, arg2) == result

# ----------------------------- TESTS TASK 3 -----------------------------------
"""
write tests for is_http_domain function
"""
from tasks import is_http_domain

domains = [
    ('http://wikipedia.org', True),
    ('https://ru.wikipedia.org/', True),
    ('griddynamics.com', False)
]

@pytest.mark.parametrize('domain, result', domains)
def test_is_http_domain(domain, result):
    assert is_http_domain(domain) is result

# --------------------------- TESTS TASK 5 -------------------------------------
import unittest
from unittest.mock import Mock, patch
from tasks import make_request

class TestMakeRequest(unittest.TestCase):

    @patch('tasks.urllib.request.urlopen')
    def test_make_request_success(self, mock_urlopen):
        # Configure mock_urlopen
        mock_response = Mock()
        mock_response.getcode.return_value = 200
        mock_response.read.return_value = b'some text'
        mock_urlopen.return_value = mock_response

        # Call the function
        status_code, decoded_response = make_request('https://example.com')

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(decoded_response, 'some text')

    @patch('tasks.urllib.request.urlopen')
    def test_make_request_error(self, mock_urlopen):
        # Configure mock_urlopen for error case
        mock_response = Mock()
        mock_response.getcode.return_value = 404
        mock_urlopen.return_value = mock_response

        # Call the function
        status_code, decoded_response = make_request('https://example.com')

        # Assertions
        self.assertEqual(status_code, 404)
        self.assertEqual(decoded_response, '')

if __name__ == '__main__':
    unittest.main()