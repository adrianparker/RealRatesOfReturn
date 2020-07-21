"""Encapsulates a specific instance of a Call Account.

@author Adrian Parker
"""


class CallAccount:

    def __init__(self, data):
        self.institution = data[0]
        self.credit_rating = data[1]
        self.name = data[2]
        self.min_deposit = data[3]
        self.nominal = data[4]
