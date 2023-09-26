#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def helper_function(helper_parameter=None, **args):
    """
    Explain the function briefly.

    Arguments:
        `helper_parameter`: An integer or None. (By default: helper_parameter=None)

    Details:
        Explain the function in more detail.

    Examples:
        ```
        helper_function(1)
        ```

    Output:
        Explain the output.

    """
    # INPUT CHECK
    if not (isinstance(helper_parameter, int) or helper_parameter is None):
        raise Exception(
            "'helper_parameter' must be None or string specifying temporary directory."
            )
    # INPUT CHECK END
    # If the file is not located in the local machine
    if helper_parameter is not None:
        print("This is helper function.")
    return helper_parameter
