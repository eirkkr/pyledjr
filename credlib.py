"""
Universal library to handle credentials
"""


class Credential:
    def __init__(self, bank: object, username: object,
                 password: object) -> None:
        self.bank = bank
        self.username = username
        self.password = password
