PyLineNotify
====

If you have confidence in English Skills, Plz read this page and send pull request,take it easy.

A Library that manipulates LineNotify easily in Python.

あなたが日本語話者の場合、こちらの方が快適に読み進める事が出来るでしょう ->
 [README_JP.md](https://github.com/reud/PyLineNotify/blob/master/README_JP.md) 

## Description

It can easily use LINENotify

## Requirement

Python 3.5+

If you want to know what it need, see
[requirements.txt](https://github.com/reud/PyLineNotify/blob/master/requirements.txt)

## Usage

Cation: If you dont have LINENotify Access Token,You can get from
[this](https://notify-bot.line.me/ja/)

Below code is send 'Hello World' to LINENotify.

```Python
import PyLineNotify

TOKEN = 'YOUR_ACCESS_TOKEN'

PyLineNotify.send_message(token=TOKEN,message='Hello World!')

# same as PyLineNotify.send_sticker(TOKEN, 'Hello World!')

```

below screenshot is the result.


![messageサンプル](https://github.com/reud/PyLineNotify/blob/master/samples/message.PNG)

We can send a photo.(But a message need)

Below code is send miku.jpg in same directory to LINENotify.


```python
import PyLineNotify

TOKEN = 'YOUR_ACCESS_TOKEN'

PyLineNotify.send_photo_with_message(token=TOKEN, message='Hatune Miku', path='miku.jpg')

# same as PyLineNotify.send_photo_with_message(TOKEN,'Hatune Miku','miku.jpg')

```

below screenshot is the result.


![photoサンプル](https://github.com/reud/PyLineNotify/blob/master/samples/photo.PNG)

We also can send a sticker.(But a message need)


[This](https://devdocs.line.me/files/sticker_list.pdf) is stickers which we can use.

STKID　correspond to　sticker_id,
STKPKGID correspond to sticker_package_id.

Below code is send a sticker to LINENotify.


```python
import PyLineNotify

TOKEN = 'YOUR_ACCESS_TOKEN'

PyLineNotify.send_sticker_with_message(token=TOKEN, message='Hello World', sticker_package_id='1', sticker_id='1')

# same as PyLineNotify.send_sticker(TOKEN, 'Hello World', 1, 1)

```

below screenshot is the result.


![stickerサンプル](https://github.com/reud/PyLineNotify/blob/master/samples/sticker.PNG)


####For those who find it difficult to specify TOKEN as an argument one by one, I have also created our own classes

The following code creates a Notifer type object and executes the same operation as the above three codes at the same time.

```python
import PyLineNotify

TOKEN = 'YOUR_ACCESS_TOKEN'

notifer=PyLineNotify.Notifer(TOKEN)

notifer.send_message('Hello World!')

notifer.send_photo_with_message('Hello Hatune Miku!','miku.jpg')

notifer.send_sticker_with_message('Hello World', 1, 1)
```

When creating such an object, you do not need to put  access_token in the argument.

## Install

```Terminal
$ pip install pylinenotify
```


## Licence

[MIT](https://github.com/reud/MIT_LICENSE/blob/master/LICENSE)

## Author

[reud](https://github.com/reud)