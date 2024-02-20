def asciibrain(txts:str):
    beforecode = "++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>"
    code = []
    texts = list(txts.upper())
    for i in texts:
        x = int(ord(i)-65)
        if (x < 5) and (x >= 0):
            code.append("<<{}.{}>>".format("+"*x,"-"*x))
        elif (x < 0) and ((-1*x) <= 15):
            code.append("<<{}.{}>>".format("-"*(-1*(x)),"+"*(-1*(x))))
        elif x < 0:
            x += 35
            code.append(">>>{}.{}<<<".format("+"*x,"-"*x))
        elif x < 10:
            code.append("<{}.{}>".format("+"*(x-5),"-"*(x-5)))
        elif x < 15:
            code.append("{}.{}".format("+"*(x-10),"-"*(x-10)))
        elif x < 20:
            code.append(">{}.{}<".format("+"*(x-15),"-"*(x-15)))
        else:
            code.append(">>{}.{}<<".format("+"*(x-20),"-"*(x-20)))
    for i in code:
        beforecode += i
    while True:
        stscode = beforecode
        beforecode = beforecode.replace("><","").replace("<>","").replace("+-","").replace("-+","")
        if beforecode == stscode:
            break
    return beforecode

def hiraganabrain(txts:str):
    beforecode = ">>++++++++[>++++++++[<<++++>>-]<-]<[>++++[>++++++++[<<<++++>>>-]<-]<-]+<[+>-<[>+<---]>>>++++++++++++[<+++++++++++[<+++++++++++>-]>-]<+++++[<----->-]<++>>"
    aftercode = "<[<]>[[<+<+>>-]<<.>[<->-]>>[[<+>-]>]<<[<]>]<]>[[-]<++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>>>.<<+++.---<<+++.+.---->>>++.-->>++.+++++++++++++++++.-------------------<<<<<-----------.+++++++++++>>>>>++.--<<<<<+.->+++.--->>++++.---->>++.--<<<<<+++.+.---->>>++++.----<<<++++.--.-->>>++++.----[<]]"
    code = []
    texts = list(txts)
    for i in texts:
        x = int(ord(i)-12352)
        if x < 0:
            pass
        elif x < 7:
            code.append("{}>".format("+"*x))
        elif x <= 10:
            code.append(">+++++[<++>-]<{}>".format("-"*(10-x)))
        elif x <= 15:
            code.append(">+++++[<+++>-]<{}>".format("-"*(15-x)))
        elif x <= 20:
            code.append(">+++++[<++++>-]<{}>".format("-"*(20-x)))
        elif x <= 25:
            code.append(">+++++[<+++++>-]<{}>".format("-"*(25-x)))
        elif x <= 30:
            code.append(">+++++[<++++++>-]<{}>".format("-"*(30-x)))
        elif x <= 35:
            code.append(">+++++[<+++++++>-]<{}>".format("-"*(35-x)))
        elif x <= 40:
            code.append(">+++++[<++++++>-]+++++[<++>-]<{}>".format("-"*(40-x)))
        elif x <= 45:
            code.append(">+++++[<++++++>-]+++++[<+++>-]<{}>".format("-"*(45-x)))
        elif x <= 50:
            code.append(">+++++[<++++++>-]+++++[<++++>-]<{}>".format("-"*(50-x)))
        elif x <= 55:
            code.append(">+++++[<++++++>-]+++++[<+++++>-]<{}>".format("-"*(55-x)))
        elif x <= 60:
            code.append(">+++++[<++++++>-]+++++[<++++++>-]<{}>".format("-"*(60-x)))
        elif x <= 65:
            code.append(">+++++[<++++++>-]+++++[<+++++++>-]<{}>".format("-"*(65-x)))
        elif x <= 70:
            code.append(">+++++[<++++++>-]+++++[<++++++++>-]<{}>".format("-"*(70-x)))
        elif x <= 75:
            code.append(">+++++[<++++++>-]+++++[<+++++++++>-]<{}>".format("-"*(75-x)))
        elif x <= 80:
            code.append(">+++++[<++++++>-]+++++[<++++++++++>-]<{}>".format("-"*(80-x)))
        elif x <= 85:
            code.append(">+++++[<++++++>-]+++++[<+++++++++++>-]<{}>".format("-"*(85-x)))
        elif x == 86:
            # ゖの場合を忘れていた
            code.append(">+++++[<++++++>-]+++++[<+++++++++++>-]<+>")
    for i in code:
        beforecode += i
    beforecode += aftercode
    while True:
        stscode = beforecode
        beforecode = beforecode.replace("><","").replace("<>","").replace("+-","").replace("-+","")
        if beforecode == stscode:
            break
    return beforecode