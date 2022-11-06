import requests

class utils:

    isDebug = False
    line_api_key = ""

    def __init__(self, isDebug, line_api_key):
        self.isDebug = isDebug
        self.line_api_key = line_api_key

    def send_line(self, message, *args):
        if self.isDebug:
            print(message)
        else:
            line_notify_api = 'https://notify-api.line.me/api/notify'
            line_notify_token = self.line_api_key
            headers = {'Authorization': 'Bearer ' + line_notify_token}
            payload = {'message': message}
            if len(args) == 0:
                requests.post(line_notify_api, data=payload, headers=headers)
            else:
                files = {"imageFile": open(args[0], "rb")}
                requests.post(line_notify_api, data=payload, headers=headers, files=files)

    def screenshot(self, driver):
        # 画面キャプチャ
        width = driver.execute_script("return document.body.scrollWidth;")
        height = driver.execute_script("return document.body.scrollHeight;")
        driver.set_window_size(width, height)
        driver.save_screenshot('screenshot.png')
        return 'screenshot.png'