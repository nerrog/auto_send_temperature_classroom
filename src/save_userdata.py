# ユーザーデータ保存用のスクリプト
import os
from selenium import webdriver
import chromedriver_binary 

options = webdriver.chrome.options.Options()
profile_path = r"D:\コード\auto_send_temperature_classroom\src\UserData"
options.add_argument('--user-data-dir=' + profile_path)
driver = webdriver.Chrome(options=options)


# すぐ終了してしまうので無駄な処理する
while True:
    a =1
