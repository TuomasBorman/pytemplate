#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from os import makedirs
from os.path import exists, dirname, join
import tempfile
from importlib import reload
from datetime import datetime
import warnings


def __start_logging(name, log_file):
    """
    This function creates a logger with logger file.
    """
    # If user specified the path for the file
    if isinstance(log_file, str):
        dir_name = dirname(log_file)
        file_name = log_file
    else:
        # If tmp folder is used
        temp_dir_path = tempfile.gettempdir()
        dir_name = temp_dir_path + "/pytemplate"
        file_name = join(dir_name, "pytemplate.log")
    # Check that paths exist. If not, create them.
    if not exists(dir_name):
        makedirs(dir_name)
    if not exists(file_name):
        open(file_name, "a").close()
    # Configure
    logging.basicConfig(
        filename=file_name,
        format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    # Capture warnings from all function that are used
    logging.captureWarnings(True)
    # Create a logger
    logger = logging.getLogger(name)
    # Get only message from warnings
    warnings.formatwarning = __custom_format_for_warning  # type: ignore
    return logger


def __custom_format_for_warning(msg, *args, **kwargs):
    """
    This function defines a custom format for warnings.
    """
    # Ignore everything except the message
    return str(msg)


def __stop_logging(logger=None):
    """
    This function resets logging;
    warnings are not captured to log file anymore.
    """
    # Do not catch warnings
    logging.captureWarnings(False)
    # Reset warning message formatting
    reload(warnings)
    return None


def __log_to_file(message_df, log_file, file_name, msg):
    """
    This function adds rows that caused an error to a file.
    """
    # If user specified the path for the file
    if isinstance(log_file, str):
        dir_name = dirname(log_file)
    else:
        # If tmp folder is used
        temp_dir_path = tempfile.gettempdir()
        dir_name = temp_dir_path + "/pytemplate"
    # Add subdirectory
    dir_name = dir_name + "/warnings"
    # Get the full filename
    file_name = join(dir_name, file_name)
    # Check that paths exist. If not, create them.
    if not exists(dir_name):
        makedirs(dir_name)
    if not exists(file_name):
        open(file_name, "a").close()
    # Add timestamp
    message_df["time"] = str(datetime.now())
    # Add message
    message_df["message"] = msg
    # Store to file
    message_df.to_csv(file_name, mode="a")
    # Give warning
    warnings.warn(
        message=f"{msg} Check file {file_name}",
        category=Warning
        )
    return None
