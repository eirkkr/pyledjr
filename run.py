import accounts
import os
import pandas as pd
import shutil
import json

with open("./accounts.json") as file:
    ACCOUNTS = json.load(file)


def _clean_account(account: str):
    files = [f for f in os.listdir("./data/" + account)]
    file_list = list()
    for filename in files:
        kwargs = ACCOUNTS[account]
        kwargs["path"] = (
            "./data/" + kwargs["bank"] + "_" + kwargs["account"] + "/" + filename
        )

        file_list.append(accounts.BankAccount(**kwargs))

    [f.clean() for f in file_list]


[_clean_account(a) for a in ACCOUNTS]


cleaned_files = ["./data/.temp/" + f for f in os.listdir("./data/.temp/")]

data = list()
data.append(pd.read_parquet("./data/transactions.parquet"))
[data.append(pd.read_parquet(f)) for f in cleaned_files]

df = (
    pd.concat(data)
    .drop_duplicates()
    .sort_values(
        by=[
            "Date",
            "Bank",
            "Account",
            "Transaction",
            "Description",
            "From",
            "To",
            "Notes",
        ],
        ascending=False,
    )
)

df.to_parquet("./data/transactions.parquet", compression=None, index=False)
shutil.rmtree("./data/.temp/")

if not os.path.exists("./data/.temp"):
    os.makedirs("./data/.temp")
