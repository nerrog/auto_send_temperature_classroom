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
3. `template.yaml`をコピーして`key.yaml`に変更する
    ```
    .
    ├── key.yaml
    └── src
        ├── main.py
        └── ...

    ```
4. `key.yaml`にGASのAPIのURL(`api`)、LINE NotifyのAPIキー(`line`)、Googleアカウントのメールアドレス(`gmail`)、Googleアカウントのパスワード(`pass`)をそれぞれ書き込んで保存
5. 先生によって質問の送信方法が違うと思うので`main.py`のブラウザ操作部のソースコードを書き換える(主にxpath等の要素取得部分)
6. `pip install -r requirements.txt`を実行する
7. crontabやタスクスケジューラで`main.py`を任意の時間にセットする
8. ｵﾜﾘ