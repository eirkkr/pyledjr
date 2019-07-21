"""
Read, interpret and clean up bank transaction data, then save output as
a parquet file.

TODO: might be better to allow users to define bank parameters in a file
"""

import pandas as pd
import time


class BankAccount:
    def __init__(self, bank: str, account: str):
        self.bank = bank
        self.account = account

    def clean_file(self, path: str):
        if self.bank == 'ANZ':
            df = pd.read_csv(
                filepath_or_buffer=path,
                names=['Date', 'Description', 'Debits and credits', 'Balance'],
                dtype={'Description': str, 'Debits and credits': str,
                       'Balance': str
                       },
                parse_dates=['Date'],
                dayfirst=True,
                header=0
            )
            df = df.assign(Bank=self.bank, Account=self.account)

            df = df[[
                'Bank',
                'Account',
                'Date',
                'Debits and credits',
                'Balance',
                'Description'
            ]]

            df = df.rename(columns={
                'Debits and credits': 'Transaction',
            })

        else:
            raise Exception('ERROR: Unrecognised bank.')

        out_path = './data/{time}_{bank}_{account}.parquet'.format(
            time=time.strftime("%Y-%m-%d_%H:%M:%S"),
            bank=self.bank,
            account=self.account
        )

        df.to_parquet(out_path, index=False, compression=None)
