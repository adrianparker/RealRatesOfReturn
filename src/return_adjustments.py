"""
A collection of return adjustment calculation functions.

@author Adrian Parker
"""

from decimal import getcontext

getcontext().prec = 4


def after_tax_return(nominal, tax_rate):
    """Returns after tax return rate for given nominal and tax rate.

    Args:
        nominal (float): the nominal rate of return
        tax_rate (float): the tax rate to adjust nominal for
    Returns:
      float: after tax rate of return, to 4 decimal places
    """

    return float(getcontext().create_decimal_from_float(
        nominal * (1 - tax_rate)))


def real_return(after_tax_return, inflation):
    """Returns real return for given after tax return and inflation rate.

    Args:
        after_tax_return (float): the after tax rate of return
        inflation (float): the inflation rate to adjust by
    Returns:
        float: real rate of return, to 4 decimal places
    """

    real_rate = ((1 + after_tax_return) / (1 + inflation)) - 1
    return float(getcontext().create_decimal_from_float(real_rate))


def real_return_from_nominal(nominal, tax_rate, inflation):
    """Returns real return for given nominal rate, tax rate and inflation rate.

    Args:
        nominal (float): the nominal rate of return
        tax_rate (float): the tax rate to adjust nominal for
        inflation (float): the inflation rate to adjust by
    Returns:
        float: real rate of return, to 4 decimal places
    """

    return real_return(after_tax_return(nominal, tax_rate), inflation)
