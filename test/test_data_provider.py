"""Tests data_provider.py. """
from src.data_provider import get_call_accounts
from src.data_provider import get_call_accounts_from_html
from src.data_provider import get_call_account_institution_names


def test_get_call_accounts():
    accounts = get_call_accounts()
    assert(len(accounts) == 116)


def test_get_call_accounts_from_html():
    html = """
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
    accounts = get_call_accounts_from_html(html)
    assert(len(accounts) == 3)


def test_get_call_account_institution_names():
    assert(len(get_call_account_institution_names()) == 31)
