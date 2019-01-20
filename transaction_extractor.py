"""
    File name: transaction_extractor.py
    Author: Eric Parkin
    Date created: 2019-01-19
    Last modified: 2019-01-19
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials

# bank urls
browser = 'Chrome'


def anz_collector():
    driver = webdriver.Chrome()
    driver.get('https://www.anz.com/INETBANK/bankmain.asp')
    driver.switch_to.frame(driver.find_element_by_id('main'))
    driver.find_element_by_name('CorporateSignonCorpId').send_keys(credentials.anz.username)
    driver.find_element_by_name('CorporateSignonPassword').send_keys(credentials.anz.password)
    driver.find_element_by_id('SignonButton').click()
    driver.find_element_by_class_name('listViewAccountWrapperYourAccounts').click()
    driver.find_element_by_class_name('dwnldTransHistoryDiv').click()
    driver.find_element_by_id('extendedTxnDetailsChkBx').click()
    driver.find_element_by_id('ANZSrchDtRng').click()
    driver.find_element_by_xpath('//*[@id="ANZSrchDtRng"]/option[9]').click()
    driver.find_element_by_name('enterYourOwn').send_keys('731')
    driver.find_element_by_name('Action.ANZAccounts.DwnldTransactionsCIS').click()
    driver.close()


anz_collector(anz_url)
