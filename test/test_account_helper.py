"""Tests nominal_rate_extractor.py functions. """

from src import account_helper
from src import data_provider


def _get_sample_call_accounts():
    return data_provider.get_call_accounts()


def test_get_account_with_maximum_nominal():
    accounts = _get_sample_call_accounts()
    maximum_rate_accounts = account_helper.get_accounts_with_maximum_nominal(
        accounts)
    assert(len(maximum_rate_accounts) == 1)
    maximum_rate = maximum_rate_accounts[0]
    assert(maximum_rate.institution == 'NZCU Employees')
    assert(maximum_rate.name == 'Christmas Club')
    assert(maximum_rate.nominal == 3)


def test_get_two_accounts_when_two_with_same_max_nominal():
    # has two instruments with rate 0.05 and one with lower rate
    two_maximums = """
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;">
        <td width="210px" class="inst-name" valign="top">
            <a class="interest_financial_link" href="https://www.interest.co.nz/directory#anz" title="ANZ">ANZ</a>
        </td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Online savings </td>
        <td width="55px" class="right" valign="middle">$1</td>
        <td width="55px" class="right" valign="middle">0.05</td>
    </tr>
    <tr class="interest_financial_row_0" style="">
        <td width="210px" class="inst-name" valign="top"></td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Select</td>
        <td width="55px" class="right" valign="middle">$5,000</td>
        <td width="55px" class="right" valign="middle">0.04999999</td>
    </tr>
    <tr class="interest_financial_row_0" style="">
        <td width="210px" class="inst-name" valign="top"></td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Select</td>
        <td width="55px" class="right" valign="middle">$5,000</td>
        <td width="55px" class="right" valign="middle">0.05</td>
    </tr>"""
    accounts = data_provider.get_call_accounts_from_html(two_maximums)
    max_accounts = account_helper.get_accounts_with_maximum_nominal(accounts)
    assert(len(max_accounts) == 2)
    for account in max_accounts:
        assert(account.nominal == 0.05)


def test_get_one_account_when_two_with_same_but_lower():
    # has two instruments with rate 0.05 and one with higher rate
    one_maximum = """
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;">
        <td width="210px" class="inst-name" valign="top">
            <a class="interest_financial_link" href="https://www.interest.co.nz/directory#anz" title="ANZ">ANZ</a>
        </td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Online savings </td>
        <td width="55px" class="right" valign="middle">$1</td>
        <td width="55px" class="right" valign="middle">0.05</td>
    </tr>
    <tr class="interest_financial_row_0" style="">
        <td width="210px" class="inst-name" valign="top"></td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Select</td>
        <td width="55px" class="right" valign="middle">$5,000</td>
        <td width="55px" class="right" valign="middle">0.0500000001</td>
    </tr>
    <tr class="interest_financial_row_0" style="">
        <td width="210px" class="inst-name" valign="top"></td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Select</td>
        <td width="55px" class="right" valign="middle">$5,000</td>
        <td width="55px" class="right" valign="middle">0.05</td>
    </tr>"""
    accounts = data_provider.get_call_accounts_from_html(one_maximum)
    max_accounts = account_helper.get_accounts_with_maximum_nominal(accounts)
    assert(len(max_accounts) == 1)
    assert(max_accounts[0].nominal == 0.0500000001)


def test_sample_call_accounts_BNZ_correct_length():
    bnz_accounts = account_helper.get_accounts_for_institution(
        _get_sample_call_accounts(), 'BNZ')
    assert(len(bnz_accounts) == 3)


def test_sample_call_accounts_HSBC_correct_rating():
    hsbc_accounts = account_helper.get_accounts_for_institution(
        _get_sample_call_accounts(), 'HSBC')
    assert(len(hsbc_accounts) == 2)
    for account in hsbc_accounts:
        assert(account.institution == 'HSBC')
        assert(account.credit_rating == 'AA-')


def test_sample_call_accounts_kookmin_correct_names():
    kookmin_accounts = account_helper.get_accounts_for_institution(
        _get_sample_call_accounts(), 'Kookmin')
    assert(len(kookmin_accounts) == 2)
    for account in kookmin_accounts:
        assert(account.institution == 'Kookmin')
        assert(account.credit_rating == 'A')
        assert(account.name == 'Personal Cheque')


def test_extracted_call_accounts_westpac_correct_min_deposits():
    westpac_accounts = account_helper.get_accounts_for_institution(
        _get_sample_call_accounts(), 'Westpac')
    assert(len(westpac_accounts) == 2)
    for account in westpac_accounts:
        assert(account.institution == 'Westpac')
        assert(account.credit_rating == 'AA-')
        assert('Saver' in account.name)
        assert(account.min_deposit == 1)


def test_extracted_call_accounts_icbc_correct_nominal_rate():
    icbc_accounts = account_helper.get_accounts_for_institution(
        _get_sample_call_accounts(), 'ICBC')
    assert(len(icbc_accounts) == 1)
    account = icbc_accounts[0]
    assert(account.institution == 'ICBC')
    assert(account.credit_rating == 'A')
    assert(account.name == 'Smart Saver')
    assert(account.min_deposit == 1)
    assert(account.nominal == 0.8)


def test_get_accounts_with_maximum_nominal_for_deposit():
    three_different_deposits = """
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;">
        <td width="210px" class="inst-name" valign="top">
            <a class="interest_financial_link" href="https://www.interest.co.nz/directory#anz" title="ANZ">ANZ</a>
        </td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Online savings </td>
        <td width="55px" class="right" valign="middle">$10000</td>
        <td width="55px" class="right" valign="middle">0.05</td>
    </tr>
    <tr class="interest_financial_row_0" style="">
        <td width="210px" class="inst-name" valign="top"></td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Select</td>
        <td width="55px" class="right" valign="middle">$15,000</td>
        <td width="55px" class="right" valign="middle">0.0500000001</td>
    </tr>
    <tr class="interest_financial_row_0" style="">
        <td width="210px" class="inst-name" valign="top"></td>
        <td width="12px" class="right" valign="top">AA-</td>
        <td width="150px" class="left-align" valign="middle">Select</td>
        <td width="55px" class="right" valign="middle">$25,000</td>
        <td width="55px" class="right" valign="middle">0.05</td>
    </tr>"""
    accounts = data_provider.get_call_accounts_from_html(
        three_different_deposits)
    assert(len(account_helper.get_accounts_with_maximum_nominal_for_deposit(
        accounts, 9999.99)) == 0)
    assert(len(account_helper.get_accounts_with_maximum_nominal_for_deposit(
        accounts, 10000.00)) == 1)
    max_accounts = account_helper.get_accounts_with_maximum_nominal_for_deposit(
        accounts, 25000)
    assert(len(max_accounts) == 1)
    assert(max_accounts[0].nominal == 0.0500000001)
