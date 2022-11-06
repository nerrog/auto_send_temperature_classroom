import os
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def generate_driver(Debug):
    # Chrome

    if os.environ["IS_REMOTE_DRIVER"] == "True":
        
        # Docker環境なら
        driver = webdriver.Remote(
            command_executor=os.environ['SELENIUM_URL'],
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        return driver
        
    else:
        
        options = webdriver.ChromeOptions()
        # デプロイ時にはヘッドレスモードを推奨
        if config.IS_HEADLESS:
            options.add_argument('--headless')

        options.add_argument('--lang=ja-JP')
        options.add_argument('--disable-gpu')
        options.add_argument("--start-maximized")
        options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"')

        driverpass = config.CHROME_DRIVER

        # Debug
        if Debug:
            driverpass = os.path.join(os.getcwd(), "chromedriver.exe")

        """
        if Debug:
            # 帯域制限用
            driver.set_network_conditions(
                offline=False,
                latency=200,  # 200ms
                download_throughput=500 / 8 * 1024,  # 500kbps
                upload_throughput=200 / 8 * 1024)  # 200kbps
        """

        try:
            driver = webdriver.Chrome(driverpass, options=options)
        except Exception as ex:
            return ex

        driver.set_window_size('1920', '1080')

        return driver