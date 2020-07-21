"""Provides filtration and maximisation functions for accounts.

@author Adrian Parker
"""


def get_accounts_for_institution(accounts, institution):
    """Provides the accounts available from the given institution.

    Args:
        accounts: array of accounts to filter by institution
    Returns:
        array of 0..* accounts provided by given institution
    """

    institution_accounts = []
    for account in accounts:
        if account.institution == institution:
            institution_accounts.append(account)
    return institution_accounts


def get_accounts_with_maximum_nominal(accounts):
    """Provides the accounts that have maximum nominal interest.

    Args:
        accounts: non empty array of accounts to find maximum nominal within
    Returns:
        array of 1..* accounts that have maximum nominal
    Raises:
        Exception if null or empty array of accounts provided
    """

    if not accounts or len(accounts) == 0:
        raise Exception('Must provide array of accounts')
    accounts_having_max_nominal = []
    for account in accounts:
        if len(accounts_having_max_nominal) == 0:
            accounts_having_max_nominal.append(account)
        else:
            if account.nominal > accounts_having_max_nominal[0].nominal:
                accounts_having_max_nominal.clear()
                accounts_having_max_nominal.append(account)
            elif account.nominal == accounts_having_max_nominal[0].nominal:
                accounts_having_max_nominal.append(account)
    return accounts_having_max_nominal


def get_accounts_with_maximum_nominal_for_deposit(accounts, deposit=0):
    """Provides the accounts that have maximum nominal interest that are accessible with given deposit.

    Args:
        accounts: array of accounts to find maximum nominal for given deposit within
        deposit: float of deposit the maximum account must accommodate, Default 0.
    Returns:
        array of 1..* accounts that have maximum nominal and accommodate given deposit amount
    Raises:
        Exception if null or empty array of accounts provided
    """

    if not accounts or len(accounts) == 0:
        raise Exception('Must provide array of accounts')
    accounts_that_accommodate_deposit = []
    for account in accounts:
        if account.min_deposit <= deposit:
            accounts_that_accommodate_deposit.append(account)
    if len(accounts_that_accommodate_deposit) > 0:
        return get_accounts_with_maximum_nominal(accounts_that_accommodate_deposit)
    return accounts_that_accommodate_deposit
