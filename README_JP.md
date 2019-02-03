PyLineNotify
====

Pythonで簡単にLineNotifyを操作するライブラリ。
if you want to see README in English,  Click it !

## Description

LINENotifyでLINEに通知を送る際に必要なリクエストを簡略化し、簡単にLINENotifyを使いこなす事が出来る様になります。

## Demo



## Requirement

Python 3.5~

使用している他ライブラリについては
[requirements.txt](https://github.com/reud/PyLineNotify/blob/master/requirements.txt) を確認してください。

## Usage
LINENotifyを簡単に使う事が出来るようになります！

LINENotifyを使用する際、アクセストークンが必要なのですが、

[こちら](https://notify-bot.line.me/ja/)から取得できます。

以下のコードは'Hello World!'とLINENotifyで通知させるコードです。


```Python
import PyLineNotify

TOKEN = 'YOUR_ACCESS_TOKEN'

PyLineNotify.send_message(token=TOKEN,message='Hello World!')

# same as PyLineNotify.send_sticker(TOKEN, 'Hello World!')

```

これを実行すると以下のようにLINENotifyから通知が来ます。

## Install

```Terminal
$ pip install pylinenotify
```

## Contribution

## Licence

[reud](https://github.com/reud/MIT_LICENSE)

## Author

[reud](https://github.com/reud)