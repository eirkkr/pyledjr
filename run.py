# TODO: these objects should be generated from user input
import accounts
from os import listdir

anz_access_advantage = [f for f in listdir("./data/ANZ_AccessAdvantage/")]
anz_cash_investment = [f for f in listdir("./data/ANZ_CashInvestment/")]
anz_online_saver_files = [f for f in listdir("./data/ANZ_OnlineSaver/")]
mebank_transaction = [f for f in listdir("./data/MEBank_EverydayTransaction/")]
mebank_online_savings = [f for f in listdir("./data/MEBank_OnlineSavings/")]
ubank_usaver = [f for f in listdir("./data/UBank_USaver/")]
ubank_usaver_ultra = [f for f in listdir("./data/UBank_USaverUltra/")]

account_settings = {
    "ANZ_CashInvestment": {
        "bank": "ANZ",
        "account": "ANZ_CashInvestment",
        "column_date": 0,
        "column_transaction": 1,
        "column_desc": 2,
        "column_from": 3,
        "column_to": 4,
        "column_notes": 7,
    },
    "ANZ_EverydayTransaction": {
        "bank": "ANZ",
        "account": "EverydayTransaction",
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

anz_online_saver = list()
for filename in anz_online_saver_files:

    kwargs = account_settings["ANZ_OnlineSaver"]
    kwargs["path"] = (
            "./data/"
            + kwargs["bank"]
            + "_"
            + kwargs["account"]
            + "/"
            + filename
    )

    anz_online_saver.append(accounts.BankAccount(**kwargs))

[f.clean() for f in anz_online_saver]
