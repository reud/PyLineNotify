pylinenotify
====

Pythonで簡単にLineNotifyを操作するライブラリ。

if you want to see README in English,  Check [README.md](https://github.com/reud/pylinenotify/blob/master/README.md) !

## Description

LINENotifyでLINEに通知を送る際に必要なリクエストを簡略化し、簡単にLINENotifyを使いこなす事が出来る様になります。


## Requirement

Python 3.5~

使用している他ライブラリについては
[requirements.txt](https://github.com/reud/pylinenotify/blob/master/requirements.txt) を確認してください。

## Usage

注意:LINENotifyを使用する際、アクセストークンが必要なのですが、

[こちら](https://notify-bot.line.me/ja/)から取得できます。

右上のログインからLINEにログインした後、再度右上をクリックしMy Pageを選択、ページ下部の
Generate access token (For developers)　の　Generate tokenをクリック、あとはアプリ名を付けて、
LINENotifyを使用するルームを選んでGenerate tokenで表示されます。

以下のコードは'Hello World!'とLINENotifyで通知させるコードです。


```Python
import pylinenotify

TOKEN = 'YOUR_ACCESS_TOKEN'

pylinenotify.send_message(token=TOKEN,message='Hello World!')

# same as pylinenotify.send_sticker(TOKEN, 'Hello World!')

```

これを実行すると以下のようにLINENotifyから通知が来ます。


![messageサンプル](https://github.com/reud/pylinenotify/blob/master/samples/message.PNG)

画像を送信することもできます。(LINENotifyの仕様上、メッセージを同梱して送信する必要があります)

以下のコードは同ディレクトリにあるmiku.jpgを送信するコードです。

```python
import pylinenotify

TOKEN = 'YOUR_ACCESS_TOKEN'

pylinenotify.send_photo_with_message(token=TOKEN, message='Hatune Miku', path='miku.jpg')

# same as pylinenotify.send_photo_with_message(TOKEN,'Hatune Miku','miku.jpg')

```

これを実行すると以下のようにLINENotifyから通知が来ます。

![photoサンプル](https://github.com/reud/pylinenotify/blob/master/samples/photo.PNG)

スタンプも送信する事ができます。(LINENotifyの仕様上、メッセージを同梱して送信する必要があります)

[ここ](https://devdocs.line.me/files/sticker_list.pdf) にあるスタンプを使用する事ができます。
上記のPDFのSTKIDがsticker_id、STKPKGIDがsticker_package_idに対応します。

以下はスタンプを送るサンプルコードです。

```python
import pylinenotify

TOKEN = 'YOUR_ACCESS_TOKEN'

pylinenotify.send_sticker_with_message(token=TOKEN, message='Hello World', sticker_package_id='1', sticker_id='1')

# same as pylinenotify.send_sticker(TOKEN, 'Hello World', 1, 1)

```

これを実行すると以下のようにLINENotifyから通知が来ます。

![stickerサンプル](https://github.com/reud/pylinenotify/blob/master/samples/sticker.PNG)


####一々引数にTOKENを指定するのがめんどくさい人のために、独自クラスも作成してあります。

以下のコードはNotifer型オブジェクトを作成して上記の三つのコードと同じ動作をまとめて実行しています。

```python
import pylinenotify

TOKEN = 'YOUR_ACCESS_TOKEN'

notifer=pylinenotify.Notifer(TOKEN)

notifer.send_message('Hello World!')

notifer.send_photo_with_message('Hello Hatune Miku!','miku.jpg')

notifer.send_sticker_with_message('Hello World', 1, 1)
```
このようにオブジェクトを作成すれば一々引数にaccess_tokenを入れる必要がなくなります。

## Install

```Terminal
$ pip install pylinenotify
```


## Licence

[MIT](https://github.com/reud/MIT_LICENSE/blob/master/LICENSE)

## Author

[reud](https://github.com/reud)