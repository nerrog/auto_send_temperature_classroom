import requests
import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import sys
import os

# LINEに結果を送信せず標準出力でエラーを受け取る用
Debug = False

# 設定ファイルオープン
with open(os.path.dirname(os.path.abspath(__file__))+'/../key.yaml') as file:
    obj = yaml.safe_load(file)
    API_URL = obj["api"]
    LINE_API = obj["line"]
    GMAIL = obj["gmail"]
    G_PASS = obj["pass"]
    driverpass = obj["driver"]

# LINE通知用メソッド
def send_line(message, *args):
    if Debug:
        print(message)
    else:
        line_notify_api = 'https://notify-api.line.me/api/notify'
        line_notify_token = LINE_API
        headers = {'Authorization': 'Bearer ' + line_notify_token}
        payload = {'message': message}
        if len(args) == 0:
            requests.post(line_notify_api, data=payload, headers=headers)
        else:
            files = {"imageFile": open(args[0], "rb")}
            requests.post(line_notify_api, data=payload, headers=headers, files=files)

try:
    start = time.time()
    response = requests.get(API_URL)
    jsonData = response.json()
    CLASSROOM_URL = jsonData["url"]
    # p = pathlib.Path('UserData')
    print(CLASSROOM_URL)

    # Chrome
    options = webdriver.ChromeOptions()
    # options.add_argument(f'--user-data-dir={p.resolve()}')
    # デプロイ時にはヘッドレスモードを推奨
    options.add_argument('--headless')
    options.add_argument('--lang=ja-JP')
    options.add_argument('--disable-gpu')
    options.add_argument("--start-maximized")
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"')

    driver = webdriver.Chrome(driverpass, options=options)

    driver.set_window_size('1920', '1080')

    # googleログイン
    try:
        driver.get("https://www.google.com/accounts/Login?hl=ja")
        sleep(3)
        email = driver.find_element_by_xpath("//*[@id='identifierId']|//*[@id='Email']")
        email.click()
        email.send_keys(GMAIL + Keys.ENTER )
        sleep(2)
        pass_f = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        pass_f.click()
        pass_f.send_keys(G_PASS + Keys.ENTER )
        sleep(3)
    except Exception as e:
        mes = f"[ERROR] Googleログインエラー\n===エラー詳細===\n{e.args}"
        send_line(mes)
        sys.exit()


    driver.get(CLASSROOM_URL)

    #ブラウザ操作部(ここから必要に応じて変える)
    # Chromeデベロッパーツールからxpathをコピーできる
    sleep(3)
    print(driver.page_source)
    print(driver.current_url)
    # 質問のラジオボタンを選択
    select = driver.find_element_by_css_selector(".AB7Lab.Id5V1")
    select.click()
    sleep(1)
    # 提出ボタンを選択
    submit = driver.find_element_by_xpath("//*[@id='yDmH0d']/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]")
    print(submit.is_displayed())
    submit.click()
    sleep(1)
    # 確認画面の提出ボタンを選択
    submit2 = driver.find_element_by_xpath("//*[@id='yDmH0d']/div[10]/div/div[2]/div[3]/div[2]")
    print(submit2.is_displayed())
    submit2.click()
    sleep(3)
    elapsed_time = time.time() - start
    width = driver.execute_script("return document.body.scrollWidth;")
    height = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(width, height)
    driver.save_screenshot('screenshot.png')
    mes = f"[OK]\n健康観察送信完了！\n実行時間:{round(elapsed_time, 1)}秒"
    send_line(mes,'screenshot.png')
except Exception as e:
    mes = f"[ERROR] 不明なエラー\n===エラー詳細===\n{e.args}"
    send_line(mes)
    print(mes)
    sys.exit()