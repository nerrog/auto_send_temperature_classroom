# Auto_Send_Temperature_Classroom

Google Classroomの質問機能を使用して健康観察を行ってる場合に使えるスクリプトです。
尚、Classroomの「質問」のみ対応しています

# 仕組み

```
GAS
↓
Classroom API
↓
WebAPI
↓
Pythonスクリプト
↓
GoogleChrome(Selenium自動操作)
```

もっと良い方法がありそうですが面倒くさいのでこの方法を使っています。

# 必要な物

- 学校が発行したGoogleアカウント
    - GASやClassroomAPIが使えること
- スクリプト実行用サーバー
    - 自宅鯖やVPS
- LINEアカウント
    - 実行状況をお知らせするため
    - LINE NotifyのAPIキー
- やる気(大事)

# 使い方

1. `./api/code.gs`をGASでウェブアプリケーションとしてデプロイする
2. LINE NotifyからAPIキーを取得する
3. `main.py`の1つ上のディレクトリに`key.yaml`を作成。
    ```
    .
    ├── key.yaml
    └── src
        ├── main.py
        └── ...

    ```
4. `key.yaml`にGASのAPIのURL(`api`)、LINE NotifyのAPIキー(`line`)、Googleアカウントのメールアドレス(`gmail`)、Googleアカウントのパスワード(`pass`)、chromedriverの場所(`driver`)をそれぞれ書き込んで保存(`template.yamlを書き換えて作ると楽です`)
5. 先生によって質問の送信方法が違うと思うので`main.py`のブラウザ操作部のソースコードを書き換える(主にxpath等の要素取得部分)
6. `pip install -r requirements.txt`を実行する
7. crontabやタスクスケジューラで`main.py`(`run.sh`)を任意の時間にセットする
8. ｵﾜﾘ

# さいごに

自動化してても体調が優れないときはきちんと連絡を入れよう