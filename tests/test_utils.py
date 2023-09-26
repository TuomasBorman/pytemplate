#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


def test_utils():
    data = {"test1": ["test", "testi", "test"],
            "test2": [1, 2, 3],
            "test3": [True, False, False]
            }
    df = pd.DataFrame(data)
    assert isinstance(df, pd.DataFrame)
    assert "a" != "b"
