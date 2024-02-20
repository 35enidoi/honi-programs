# これなに
https://misskey.io/notes/9klwx3efx3  
このノートで使っている`ogocode`の変換機です。  
`ogocode`ってなんやねんって話ですが、`brainfuck`の命令をしゅいろさんの鳴き声に変換した所謂クソ言語です。
# どうやって使うの
```py
from ogoconv import brain_to_ogocode, ogocode_to_brain

braincode = "++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>++++.----<+.->++++.----<+.->++++.----<+.->++++.----"

# ogocodeに変換され、返される。
ogocode = brain_to_ogocode(braincode)

# brainfuckに変換され、返される
braincode_from_ogo = ogocode_to_brain(ogocode)

print(braincode == braincode_from_ogo)
# True
``` 
# 気を付けること
`ogocode`は自分含めて多分だれもインタプリンタ(あるいはコンパイラ)作ってないので実行できません。  
つまりこのプログラムの意味は...:thinking:  

一応`ogocode`の仕様乗せときます  
- 命令は`フンギャロ`、`ふぬんも`、`おなかぺこい`、`ピザ食べたい`、`うね`、`ぐ`、`ご`、`ぶえ`があり、それぞれ`brainfuck`の`[`、`]`、`,`、`.`、`>`、`<`、`+`、`-`に対応している。
- 命令と命令の間は空白を付ける  
    但し、`うね`、`ぐ`、`ご`、`ぶえ`は連続することができるが、`うね`を除いて最初は`ぐ`の場合`うぐ`。`ご`の場合`おご`、`ぶえ`の場合`あぶえ`で始まらなければならない。(例：`おごごごごごご　あぶえぶえぶえぶえ　うぐぐぐぐぐ　うねうねうねうねうね`)

example ogocode:  
https://misskey.io/notes/9k8g7gvj4f  
https://misskey.io/notes/9klwx3efx3  

昔言った仕様  
https://misskey.io/notes/9k8h1mdgv6