# Transacter (working title)

The aim of this project is to be able to automatically download bank transaction data via the web where so the data can
be cleaned and analysed

## Requirements

* Should handle bank credentials securely
* Should prompt the user to enter bank credentials which is stored securely
* Should ask where the user wants to store the data
* Should have urls stored separately, which are called in the program
* User should input the bank of their choice, which determines the browser procedure and data cleaning
* Should give a choice of browser
* Credentials.py should not exist in git, it should be created at setup, should probably have a setup script for this,
perhaps based on a template file?

## Dependencies

* ChromeDriver, available at https://sites.google.com/a/chromium.org/chromedriver/downloads 