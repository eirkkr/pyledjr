# TODO: these objects should be generated from user input
import accounts
from os import listdir
import pandas as pd
import shutil

ACCOUNTS = {
    "ANZ_AccessAdvantage": {
        "bank": "ANZ",
        "account": "AccessAdvantage",
        "column_date": 0,
        "column_transaction": 1,
        "column_desc": 2,
        "column_from": 3,
        "column_to": 4,
        "column_notes": 7,
    },
    "ANZ_CashInvestment": {
        "bank": "ANZ",
        "account": "CashInvestment",
        "column_date": 0,
        "column_transaction": 1,
        "column_desc": 2,
        "column_from": 3,
        "column_to": 4,
        "column_notes": 7,
    },
    "ANZ_OnlineSaver": {
        "bank": "ANZ",
        "account": "OnlineSaver",
        "column_date": 0,
        "column_transaction": 1,
        "column_desc": 2,
        "column_from": 3,
        "column_to": 4,
        "column_notes": 7,
        },
}


def _clean_account(account: str):
    files = [f for f in listdir("./data/" + account)]
    file_list = list()
    for filename in files:

        kwargs = ACCOUNTS[account]
        kwargs["path"] = (
                "./data/"
                + kwargs["bank"]
                + "_"
                + kwargs["account"]
                + "/"
                + filename
        )

        file_list.append(accounts.BankAccount(**kwargs))

    [f.clean() for f in file_list]


[_clean_account(a) for a in ACCOUNTS]


cleaned_files = ["./data/.temp/" + f for f in listdir("./data/.temp/")]

data = list()
data.append(pd.read_parquet("./data/transactions.parquet"))
[data.append(pd.read_parquet(f)) for f in cleaned_files]

df = (
    pd.concat(data)
    .drop_duplicates()
    .sort_values(by=[
        "Date",
        "Bank",
        "Account",
        "Transaction",
        "Description",
        "From",
        "To",
        "Notes",
    ],
        ascending=False
    )
)

df.to_parquet("./data/transactions.parquet", compression=None, index=False)
shutil.rmtree("./data/.temp/")
