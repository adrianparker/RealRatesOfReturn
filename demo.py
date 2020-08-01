"""Not strictly unit tests, more like demonstrations of how to use the program.

@author Adrian Parker
"""

from src.account_helper import get_accounts_with_maximum_nominal_for_deposit
from src.data_provider import get_call_accounts
from src.return_adjustments import real_return_from_nominal

deposit = 10000
rwt_rate = 0.33
inflation = 0.015

accounts = get_accounts_with_maximum_nominal_for_deposit(
    get_call_accounts(), deposit)
print('For a deposit of', deposit,
      'the maximum return is available from')
if accounts and len(accounts) > 0:
    for account in accounts:
        print('\t', account.institution, account.name,
              'with real after tax interest rate of: ', real_return_from_nominal(account.nominal, rwt_rate, inflation), '%')
else:
    print('No accounts found')
