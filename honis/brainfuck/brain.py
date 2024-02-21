import time

class BrainException(Exception):
    pass

class OpenBracketError(BrainException):
    pass

class CloseBracketError(BrainException):
    pass

class PointError(BrainException):
    pass

def brain(code:str,
          debug:bool=False,
          ret16:bool=False,
          log:bool=False,
          stepmode:bool=False,
          steptime:int=0,
          sizebit:int=8,
          sizemem:int=0,
          tooinc:bool=False,
          toodec:bool=False):

    coded = tuple(code.strip())
    if sizemem > 0:
        point = [0 for _ in range(sizemem)]
    else:
        point = [0]
    nowpoint = 0
    n = 0
    bit = (2**sizebit)-1
    step = 0

    def bracket_searcher(bracketslike:list[tuple[str, int]], n_:int) -> int:
        "bracketの探索する奴"
        nowchar = coded[n_]
        index = bracketslike.index((nowchar, n_))
        balance = 1

        while balance != 0:
            index += 1
            if bracketslike[index][0] == nowchar:
                balance += 1
            else:
                balance -= 1

        return bracketslike[index][1]

    brackets = [(i, v) for v, i in enumerate(coded) if i == "[" or i == "]"]

    # 角括弧の例外をすべてここでキャッチする
    if len(brackets) != 0:
        # まずブラケットがあるコードなのか(index out of range対策)
        if (brlist := tuple(map(lambda x:str(x[0]), brackets))).count("[") != brlist.count("]"):
            # `[`と`]`の量が違う
            if brlist.count("[")-brlist.count("]") > 0:
                # `]`の量が多い
                raise CloseBracketError("too many ]")
            else:
                # `[`の量が多い
                raise OpenBracketError("too many [")
        elif brlist[0] == "]":
            # 初めに閉じるブラケットのある無効なプログラムである
            raise CloseBracketError("Invalid program")
        elif brlist[-1] == "[":
            # 最後に開くブラケットのある無効なプログラム
            raise OpenBracketError("Invalid program")

    if stepmode or debug:
        print("\n"+code.strip()+"\n")
    if stepmode:
        oulist = []
        output = ""
    if log:
        logs = ""

    try:
        while n < len(coded):
            i = coded[n]
            if i == "]":
                if point[nowpoint] != 0:
                    n = bracket_searcher(list(reversed(brackets)), n)
            elif i == "[":
                if point[nowpoint] == 0:
                    n = bracket_searcher(brackets, n)
            elif i == ">":
                nowpoint += 1
                if len(point) == nowpoint:
                    if sizemem > 0:
                        if tooinc:
                            nowpoint = 0
                        else:
                            raise PointError("Pointer too increment")
                    else:
                        point.append(0)
            elif i == "<":
                nowpoint -= 1
                if nowpoint == -1:
                    if toodec:
                        nowpoint = len(point)-1
                    else:
                        raise PointError("Pointer too decrement")
            elif i == "+":
                if point[nowpoint] == bit:
                    point[nowpoint] = 0
                else:
                    point[nowpoint] += 1
            elif i == "-":
                point[nowpoint] -= 1
                if point[nowpoint] == -1:
                    point[nowpoint] = bit
            elif i == ".":
                if stepmode:
                    oulist.append(chr(point[nowpoint]))
                    output = "".join(oulist)
                else:
                    print(chr(point[nowpoint]),end="")
            elif i == ",":
                point[nowpoint] = ord(list(input())[0])
            n += 1
            step += 1
            if log:
                logs += i
            if stepmode:
                print(f"\rcodeat;{n} codein;{i} step;{step} nowpoint;{nowpoint} point;{point} output;[{output}]",end="")
                time.sleep(steptime)
    except BrainException:
        raise
    finally:
        if debug:
            print("\n\n"+str(nowpoint))
            if ret16:
                print(list(map(lambda x: format(x,"02x"), point)))
            else:
                print(point)
            if log:
                print(logs)