import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import traceback
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import lib.cdriver
import lib.utils

# LINEに結果を送信せず標準出力でエラーを受け取る用
Debug = False

utils = lib.utils.utils(Debug, config.LINE_API)


def main():
    try:
        start = time.time()
        response = requests.get(config.GAS_API_URL)
        jsonData = response.json()
        CLASSROOM_URL = jsonData["url"]

        driver = lib.cdriver.generate_driver(Debug)

        if type(driver) == Exception:
            mes = f"[ERROR] Chrome準備エラー\n===エラー詳細===\n{driver.args}"
            utils.send_line(mes)
            sys.exit()

        # googleログイン
        try:
            driver.get("https://www.google.com/accounts/Login?hl=ja")
            sleep(3)
            email = driver.find_element(By.XPATH, "//*[@id='identifierId']|//*[@id='Email']")
            email.click()
            email.send_keys(config.GMAIL + Keys.ENTER )
            driver.implicitly_wait(5)
            pass_f = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
            pass_f.click()
            pass_f.send_keys(config.G_PASS + Keys.ENTER )
            sleep(3)
        except Exception as e:
            mes = f"[ERROR] Googleログインエラー\n===エラー詳細===\n{e.args}"
            utils.send_line(mes)
            sys.exit()


        driver.get(CLASSROOM_URL)

        #ブラウザ操作部(ここから必要に応じて変える)
        # Chromeデベロッパーツールからxpathをコピーできる
        driver.implicitly_wait(5)
        #print(driver.page_source)
        #print(driver.current_url)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.AB7Lab.Id5V1')))
        except Exception as e:
            mes = f"[ERROR] タイムアウト\nラジオボタンが見つかりません"
            utils.screenshot(driver)
            utils.send_line(mes,'screenshot.png')
            sys.exit()

        # 質問のラジオボタンをクリック
        try:
            driver.find_element(By.CSS_SELECTOR, ".AB7Lab.Id5V1").click()
        except Exception as e:
            mes = f"[ERROR] 質問のラジオボタン選択エラー\n既に解答済みの可能性があります\n===エラー詳細===\n{e.args}"
            utils.screenshot(driver)
            utils.send_line(mes,'screenshot.png')
            sys.exit()

        sleep(1)
        # 提出ボタンを選択
        submit = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]")
        submit.click()
        sleep(1)

        # 確認画面の提出ボタンを選択
        submit2 = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/div[9]/div/div[2]/div[3]/div[2]")
        submit2.click()

        time.sleep(5)
        elapsed_time = time.time() - start
        utils.screenshot(driver)
        mes = f"[OK]\n健康観察送信完了!\n実行時間:{str(round(elapsed_time, 1))}秒"
        utils.send_line(mes,'screenshot.png')

    except Exception as e:
        mes = f"[ERROR] 不明なエラー\n===エラー詳細===\n{str(traceback.format_exc())}"
        utils.send_line(mes)
        sys.exit()


if __name__ == "__main__":
    main()