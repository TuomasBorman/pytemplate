#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import pytemplate.__utils as utils
from pytemplate.__utils_module1 import helper_function


def mainFunction1(x, log_file=False, **args):
    """
    Explain the function briefly.

    Arguments:
        `x`: Explain the parameter.

        `log_file`: Explain the parameter. (By default: log_file=False)

        `**args`: Additional arguments passes into other functions:

        'helper_parameter': Explain helper parameter here (By default: helper_parameter=None)

    Details:
        Explain the function in more detail.

    Examples:
        ```
        mainFunction(x, log_file=True, helper_parameter=1)
        ```

    Output:
        Explain the output type

    """
    # INPUT CHECK
    if not (isinstance(x, list) or isinstance(x, pd.Series)
            or isinstance(x, str)):
        raise Exception(
            "'x' must be a list of strings."
            )
    if not (isinstance(log_file, str) or isinstance(log_file, bool)):
        raise Exception(
            "'log_file' must be a boolean value or a string specifying a path."
            )
    # INPUT CHECK END
    # If user wants to create a logger file
    if log_file:
        # Create a logger with file
        logger = utils.__start_logging(__name__, log_file)
        path_temp = "temporary_path"
        logger.info(f'File: {path_temp}')
    # Use helper function
    res = helper_function(x, **args)
    # Reset logging; do not capture warnings anymore
    if log_file:
        utils.__stop_logging()
    return res
