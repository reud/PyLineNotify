PyLineNotify
====

Pythonで簡単にLineNotifyを操作するライブラリ。
if you want to see README in English,  Click it !

## Description

LineNotifyでのPOSTをアシストします。

## Demo



## VS. 

## Requirement
Python 3.5~
使用している他ライブラリについては
requirements.txt を確認してください。

## Usage
LINENotifyを簡単に使う事が出来るようになります！

LINENotifyを使用する際、アクセストークンが必要なのですが、こちらから取得できます。

以下のコードはHello WorldとLINENotifyで通知させるコードです。
```python
import pylinenotify

pylinenotify.send_message(token='YOUR_LINENOTIFY_TOKEN',message='Hello World!')

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