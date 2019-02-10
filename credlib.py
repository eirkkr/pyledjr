# Universal library to handle credentials


class Credential:
    def __init__(self, bank: object, username: object, password: object) -> object:
        self.bank = bank
        self.username = username
        self.password = password
