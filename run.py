# TODO: these objects should be generated from user input
import accounts

anz = accounts.BankAccount(
    path='./data/ANZ_OnlineSaver/ANZ.csv',
    bank='ANZ',
    account='OnlineSaver',
    column_date=0,
    column_desc=2,
    column_transaction=1
)

anz.clean()
