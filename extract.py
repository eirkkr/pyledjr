"""
    File name: extract.py
    Author: Eric Parkin
    Date created: 2019-01-19
    Last modified: 2019-02-10
"""

import config
import credentials
from cryptography.fernet import Fernet
import os
import time
from selenium import webdriver
import shutil


# Create decryption function (maybe this should go in another file??
def decrypt(secret):
    decrypted = Fernet(config.key).decrypt(secret).decode()
    return decrypted


# Set chrome options
chrome_options = webdriver.ChromeOptions()

prefs = {
    'download.default_directory': config.data_folder,
    'profile.default_content_setting_values.automatic_downloads': 1,
}
chrome_options.add_experimental_option('prefs', prefs)

# chrome_options.add_argument('--headless') # Not working with this turned on, need to resolve


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
    driver.find_element_by_name('CorporateSignonCorpId').send_keys(decrypt(credentials.anz.username))
    driver.find_element_by_name('CorporateSignonPassword').send_keys(decrypt(credentials.anz.password))
    driver.find_element_by_id('SignonButton').click()
    driver.find_element_by_class_name('listViewAccountWrapperYourAccounts').click()
    driver.find_element_by_class_name('dwnldTransHistoryDiv').click()
    driver.find_element_by_xpath('//*[@id="ANZSrchDtRng"]/option[9]').click()
    driver.find_element_by_name('enterYourOwn').send_keys('731')
    driver.find_element_by_id('extendedTxnDetailsChkBx').click()

    accounts = driver.find_element_by_name('AccountSummaryInd')
    accounts = [x for x in accounts.find_elements_by_tag_name('option')]

    first = True
    for account in accounts[1:]:

        if first:
            first = False
        else:
            time.sleep(30)  # Need to wait between downloads or it won't work

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

    driver.close()
