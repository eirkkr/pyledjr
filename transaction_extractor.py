"""
    File name: transaction_extractor.py
    Author: Eric Parkin
    Date created: 2019-01-19
    Last modified: 2019-01-27
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials
import config
import shutil
import os
import time

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': config.data_folder}
chrome_options.add_experimental_option('prefs', prefs)

# When complete, put inside a function


def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds


def anz_extractor():
    # Extracts ANZ bank transactions using the users credentials, and saves them in the specified folder
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.anz.com/INETBANK/bankmain.asp')
    driver.switch_to.frame(driver.find_element_by_id('main'))
    driver.find_element_by_name('CorporateSignonCorpId').send_keys(credentials.anz.username)
    driver.find_element_by_name('CorporateSignonPassword').send_keys(credentials.anz.password)
    driver.find_element_by_id('SignonButton').click()
    driver.find_element_by_class_name('listViewAccountWrapperYourAccounts').click()
    driver.find_element_by_class_name('dwnldTransHistoryDiv').click()
    driver.find_element_by_xpath('//*[@id="ANZSrchDtRng"]/option[9]').click()
    driver.find_element_by_name('enterYourOwn').send_keys('731')
    driver.find_element_by_id('extendedTxnDetailsChkBx').click()

    accounts = driver.find_element_by_name('AccountSummaryInd')
    accounts = [x for x in accounts.find_elements_by_tag_name('option')]

    for account in accounts[1:]:
        account_text = account.text
        print('account = ', account_text)
        account.click()
        driver.find_element_by_id('ANZSrchDtRng').click()

        driver.find_element_by_name('Action.ANZAccounts.DwnldTransactionsCIS').click()
        download_wait(config.data_folder)
        filename = max([config.data_folder+'/'+f for f in os.listdir(config.data_folder)], key=os.path.getctime)
        print('filename = ', filename)
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S_")
        shutil.move(os.path.join(config.data_folder, filename), config.data_folder+'/'+timestr+account_text+'.csv')

        time.sleep(30)  # find how to not do this on the last account

    driver.close()


anz_extractor()
