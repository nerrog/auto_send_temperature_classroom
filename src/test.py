# -*- coding: utf-8 -*-
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://nerrog.net")
driver.quit()