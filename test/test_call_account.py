"""Tests call_account.py. """

from src.call_account import CallAccount


def test_call_account_constructor():
    x = CallAccount(['a', 'b', 'c', 1, 2])
    assert(x.institution == 'a')
    assert(x.credit_rating == 'b')
    assert(x.name == 'c')
    assert(x.min_deposit == 1)
    assert(x.nominal == 2)
