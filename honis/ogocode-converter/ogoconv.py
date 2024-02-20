def brain_to_ogocode(code:str):
    braincodelist = list(code)
    ogocode = ""
    for i in range(len(braincodelist)):
        if braincodelist[i] == "[":
            ogocode += " フンギャロ"
        elif braincodelist[i] == "]":
            ogocode += " ふぬんも"
        elif braincodelist[i] == ",":
            ogocode += " おなかぺこい"
        elif braincodelist[i] == ".":
            ogocode += " ピザ食べたい"
        elif braincodelist[i] == "<":
            if braincodelist[i-1] == "<":
                ogocode += "うね"
            else:
                ogocode += " うね"
        elif braincodelist[i] == ">":
            if braincodelist[i-1] == ">":
                ogocode += "ぐ"
            else:
                ogocode += " うぐ"
        elif braincodelist[i] == "+":
            if i-1 < 0:
                ogocode += " おご"
            else:
                if braincodelist[i-1] == "+":
                    ogocode += "ご"
                else:
                    ogocode += " おご"
        elif braincodelist[i] == "-":
            if braincodelist[i-1] == "-":
                ogocode += "ぶえ"
            else:
                ogocode += " あぶえ"
    return ogocode

def ogocode_to_brain(code:str):
    ogocodelist = code.split()
    braincode = ""
    for i in ogocodelist:
        if i == "フンギャロ":
            braincode += "["
        elif i == "ふぬんも":
            braincode += "]"
        elif i == "おなかぺこい":
            braincode += ","
        elif i == "ピザ食べたい":
            braincode += "."
        elif "うぐ" in i:
            braincode += ">"*i.count("ぐ")
        elif "うね" in i:
            braincode += "<"*i.count("うね")
        elif "おご" in i:
            braincode += "+"*i.count("ご")
        elif "あぶえ" in i:
            braincode += "-"*i.count("ぶえ")
    return braincode