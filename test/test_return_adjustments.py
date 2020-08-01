"""Tests return_adjustments.py functions """

from src.return_adjustments import after_tax_return
from src.return_adjustments import real_return
from src.return_adjustments import real_return_from_nominal


def test_after_tax_return():
    assert after_tax_return(0.17, 0.15) == 0.1445


def test_real_return():
    assert real_return(0.1445, 0.025) == 0.1166


def test_real_return_from_nominal():
    assert real_return_from_nominal(0.17, 0.15, 0.025) == 0.1166
