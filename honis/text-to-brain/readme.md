# これなに
入力された文字を出力するbrainfuckのプログラム生成器です。
# どうやって使うの
```py
from brain_input import asciibrain, hiraganabrain

# 実行するとコードが返される。
print(asciibrain("hello world!"))

print(hiraganabrain("はろおわあるど))
```
# 気を付けること
asciibrainにおいて、文字はすべて大文字になります。  
これはASCII文字コードで小文字と大文字の場所がすごい違うので、めんどくさくなってこうなりました。  

hiraganabrainにおいて、ひらがな以外は受け付けません。
また、実行するbrainfuckの実装において、メモリの値のbit数が16Bit未満の場合、出力が`UNDER 16 BIT DETECT`になります。