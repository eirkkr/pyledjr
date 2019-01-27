# Universal library to handle credentials


class Credential:
    def __init__(self, bank, username, password):
        self.bank = bank
        self.username = username
        self.password = password
