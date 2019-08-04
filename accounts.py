"""
Read, interpret and clean up raw bank transaction data, then save output
as a temporary parquet file to be combined afterwards.
"""

import pandas as pd
import time


class BankAccount:
    def __init__(
        self, path: str, bank: str, account: str, column_date: int,
        column_transaction: int, column_desc: int,  column_from=None,
        column_to=None, column_notes=None
    ):

        self.path = path
        self.bank = bank
        self.account = account
        self.column_date = column_date
        self.column_desc = column_desc
        self.column_transaction = column_transaction
        self.column_from = column_from
        self.column_to = column_to
        self.column_notes = column_notes

    def clean(self):
        df = pd.read_csv(
            filepath_or_buffer=self.path,
            usecols=[
                self.column_date,
                self.column_transaction,
                self.column_desc,
                self.column_from,
                self.column_to,
                self.column_notes
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
                self.column_date: "Date",
                self.column_transaction: "Transaction",
                self.column_desc: "Description",
                self.column_from: "From",
                self.column_to: "To",
                self.column_notes: "Notes"
            })

        out_path = (
            "./data/temp/{time}_{bank}_{account}_{path}.parquet"
            .format(
                time=time.strftime("%Y-%m-%d_%H:%M:%S"),
                bank=self.bank,
                account=self.account,
                path=self.path.replace("/", "."),
            )
        )

        df.to_parquet(out_path, index=False, compression=None)
