# TODO: these objects should be generated from user input
import accounts
from os import listdir

anz_online_saver_files = [f for f in listdir("./data/ANZ_OnlineSaver/")]

anz_online_saver = list()

for filename in anz_online_saver_files:
    anz_online_saver.append(
        accounts.BankAccount(
            path="./data/ANZ_OnlineSaver/" + filename,
            bank='ANZ',
            account='OnlineSaver',
            column_date=0,
            column_transaction=1,
            column_desc=2,
            column_from=3,
            column_to=4,
            column_notes=7,
        )
    )

[f.clean() for f in anz_online_saver]
