"""
Read, interpret and clean up raw bank transaction data, then save output
as a an intermediate parquet file.
"""

import pandas as pd
import time


class BankAccount:
    def __init__(self, path: str, bank: str, account: str, column_date: int,
                 column_desc: int, column_transaction: int):

        self.path = path
        self.bank = bank
        self.account = account
        self.column_date = column_date
        self.column_desc = column_desc
        self.column_transaction = column_transaction

    def clean(self):
        df = pd.read_csv(
            filepath_or_buffer=self.path,
            usecols=[
                self.column_date,
                self.column_desc,
                self.column_transaction
            ],
            dtype={
                self.column_desc: str,
                self.column_transaction: float
            },
            parse_dates=[self.column_date],
            dayfirst=True,
            header=None,
        )

        df = df.assign(Bank=self.bank, Account=self.account)

        df = df.rename(
            columns={
                self.column_date: 'Date',
                self.column_desc: 'Description',
                self.column_transaction: 'Transaction'
            }
        )

        df = df[['Bank', 'Account', 'Date', 'Description', 'Transaction']]

        out_path = (
            './data/{time}_{bank}_{account}.parquet'
            .format(
                time=time.strftime("%Y-%m-%d_%H:%M:%S"),
                bank=self.bank,
                account=self.account
            )
        )

        df.to_parquet(out_path, index=False, compression=None)
