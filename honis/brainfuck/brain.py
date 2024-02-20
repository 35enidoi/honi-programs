import time

class BrainException(Exception):
    pass

class OpenBracketError(BrainException):
    pass

class CloseBracketError(BrainException):
    pass

class PointError(BrainException):
    pass

def brain(code:str,debug=False,ret16=False,log=False,stepmode=False,steptime=0,sizebit=8):
    coded = list(code.strip())
    point = [0]
    nowpoint = 0
    n = 0
    stack = []
    bit = (2**sizebit)-1
    step = 0
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
                    n = stack[-1]
                else:
                    try:
                        stack.pop()
                    except IndexError:
                        raise CloseBracketError("not detect [")
            elif i == "[":
                if point[nowpoint] == 0:
                    balance = 1
                    try:
                        while balance != 0:
                            n += 1
                            if coded[n] == "[":
                                balance += 1
                            elif coded[n] == "]":
                                balance -= 1
                    except IndexError:
                        raise OpenBracketError("not detect ]")
                else:
                    stack.append(n)
            elif i == ">":
                nowpoint += 1
                try:
                    point[nowpoint]
                except IndexError:
                    point.append(0)
            elif i == "<":
                nowpoint -= 1
                if nowpoint == -1:
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