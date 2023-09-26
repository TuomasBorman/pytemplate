# -*- coding: utf-8 -*-
from pytemplate.module1 import mainFunction1
import pytest
import requests


def test_module1_wrong_arguments():
    with pytest.raises(Exception):
        mainFunction1(None)
    with pytest.raises(Exception):
        mainFunction1(True)


def internet_connection_ok(url, timeout=5):
    try:
        request = requests.get(url, timeout=timeout)
        res = request.ok
    except Exception:
        res = False
    return res


@pytest.mark.skipif(not internet_connection_ok("https://www.google.com/"),
                    reason="No internet access")
def test_module1():
    # Test the function if there is internet connection.
    print(1)
