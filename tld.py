from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


url = 'https://www.telderi.ru/ru'
login = 'jekeam@ya.ru'
password = '131189_Ak'


def log(message, path):
    print(message)
    with open(path,'a') as l: 
        l.write('{} {}\n'.format(str(datetime.datetime.now()),message))
        l.close()


class sapGUI:
    def __init__(self, login, password, url):
        print('__init__')
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/chromedriver.exe')

        self.login = login
        self.password = password
        self.url = url

        self.delay = 7 #timeout

        #buy site
        self.buy_site = 'buy'

        #list sites on home page

    def get_sites(self):
        print('get_sites')
        try:
            print('get_sites - try')
            log(self.url,'log.txt')
            self.driver.get(self.url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.CLASS_NAME, self.buy_site)))
        finally:
            print('get_sites - finally')
            #click buy site
            self.driver.find_element_by_class_name(self.buy_site).click()

            time.sleep(7)
            #get sites list
            soup = BeautifulSoup(self.driver.page_source,'lxml')
            data = pd.DataFrame()


if __name__ == '__main__':
    sap = sapGUI(login, password, url)
    sites = sap.get_sites()