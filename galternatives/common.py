#!/usr/bin/python3

PACKAGE='galternatives'
VERSION='0.88.0'

'Set logger here'
import logging
logger = logging.getLogger(PACKAGE)

def set_logger(verbose=False, full=False):
    """Set up current logger according to parameters.

    NOTE: A logger must exists in local var before calling the function.
    """
    if verbose:
        logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    if full:
        formatter = logging.Formatter(
                '$(asctime)s - %(levelname)s: %(message)s')
        ch.setFormatter(formatter)
        logging.getLogger(PACKAGE).addHandler(ch)
    logger.addHandler(ch)

'set default logger info here'
set_logger(False, True)
