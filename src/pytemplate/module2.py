#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pkg_resources
import pandas as pd


def mainFunction2():
    """
    Get data.

    Arguments:

    Details:
        Get data that package is utilizing as a resource.

    Examples:
        ```
        df = mainFunction2()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "pytemplate", "resources/" + "data.csv")
    df = pd.read_csv(path, index_col=0, dtype=str)
    return df


def mainFunction3():
    """
    Explain

    Arguments:

    Details:
        Explain in more detail.

    Examples:
        ```
        mainFunction3()
        ```

    Output:
        pandas.DataFrame.

    """
    print(2)
    return None
