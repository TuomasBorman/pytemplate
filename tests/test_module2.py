#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytemplate.module2 as res
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest
import pkg_resources


def test_mainFunction2():
    with pytest.raises(Exception):
        df = res.mainFunction2(123)
    with pytest.raises(Exception):
        df = res.mainFunction2(True)
    with pytest.raises(Exception):
        df = res.mainFunction2("test")
    df = res.mainFunction2()
    path = pkg_resources.resource_filename(
        "pytemplate", "resources/" + "data.csv")
    df_ref = pd.read_csv(path, index_col=0, dtype=str)
    assert_frame_equal(df, df_ref)


def test_mainFunction3():
    # Do some tests
    print(2)
