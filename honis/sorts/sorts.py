def bubblesort(target:list):
    # バブルソート
    for targetrange in reversed(range(1, len(target))):
        isnotswap = True
        for r in range(targetrange):
            if target[r] > target[r+1]:
                target[r], target[r+1] = target[r+1], target[r]
                isnotswap = False
            # print(" ".join(map(str, target)))
            # print("  "*(r) + "^ ^")
        if isnotswap:
            break
    return target

def shakersort(target:list):
    # シェーカーソート
    midnum = int(len(target)/2)
    for i in range(midnum):
        isnotswap = True
        for r in range(i, len(target)-i-1):
            if target[r] > target[r+1]:
                target[r], target[r+1] = target[r+1], target[r]
                isnotswap = False
        for r in reversed(range(i+1, len(target)-i)):
            if target[r] < target[r-1]:
                target[r], target[r-1] = target[r-1], target[r]
                isnotswap = False
        # print(" ".join(map(str, target[:i+1])), "|", " ".join(map(str, target[i+1:-i-1])), "|", " ".join(map(str, target[-i-1:])))
        if isnotswap:
            break
    return target

def oddevensort(target:list):
    # 寄偶転置ソート
    isnotswap = False
    while not isnotswap:
        isnotswap = True
        for i in range(0, len(target)-1, 2):
            if target[i] > target[i+1]:
                target[i], target[i+1] = target[i+1], target[i]
                isnotswap = False
        for i in range(1, len(target)-1, 2):
            if target[i] > target[i+1]:
                target[i], target[i+1] = target[i+1], target[i]
                isnotswap = False
    return target

def combsort(target:list):
    # コムソート
    h = int(len(target)/1.3)
    if h < 1:
        h = 1
    while True:
        # print(h, target)
        i = 0
        swap = False
        while i + h < len(target):
            if target[i] > target[i+h]:
                target[i], target[i+h] = target[i+h], target[i]
                swap = True
            # print(" ".join(map(str, target)))
            # print("  "*i + "^ " + "  "*(h-1) + "^")
            i += 1
        if h == 1 and not swap:
            break
        h = int(h/1.3)
        if h < 1:
            h = 1
    return target

def quicksort(target:list):
    # クイックソート
    if len(target) <= 1:
        return target
    else:
        pipot = target[len(target)//2]
        rindex = len(target)-1
        lindex = 0
        # print(target, pipot)
        while True:
            while not target[rindex] <= pipot:
                rindex -= 1
            # print(target[rindex], rindex)
            while not target[lindex] >= pipot:
                lindex += 1
            # print(target[lindex], lindex)
            if rindex > lindex:
                if target[rindex] != target[lindex]:
                    # print(target[rindex], target[lindex], rindex, lindex)
                    target[rindex], target[lindex] = target[lindex], target[rindex]
                    # print(target)
                rindex -= 1
                lindex += 1
            else:
                break
        # print(target[:lindex], target[lindex:])
        return quicksort(target[:lindex]) + quicksort(target[lindex:])

def insertsort(target:list):
    # 挿入ソート
    returnlist = []
    for i in target:
        if len(returnlist) == 0:
            returnlist.append(i)
        else:
            for index, val in enumerate(returnlist):
                if val > i:
                    returnlist.insert(index, i)
                    break
            else:
                returnlist.append(i)
    return returnlist

def insertsort_recreate(target:list):
    # 挿入ソート作り直し
    for i in range(1, len(target)):
        val = target[i]
        changeindex = 0
        for r in reversed(range(i)):
            changeindex = r
            if val >= target[r]:
                changeindex += 1
                break
        target[changeindex+1:i+1] = target[changeindex:i]
        target[changeindex] = val
    return target

def insertsort_optimized(target: list): # chatgptに上のやつを改良してもらったやつ
    for i in range(1, len(target)):
        key = target[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if target[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        target[left+1:i+1] = target[left:i]
        target[left] = key
        # print(" ".join(map(str, target[:i])), "|", " ".join(map(str, target[i:])))
    return target

def bogosort(target:list):
    # ボゴソート
    import random
    while True:
        random.shuffle(target)
        for i in range(len(target)-1):
            if target[i] > target[i+1]:
                break
        else:
            break
    return target

def selectionsort(target:list):
    # 選択ソート
    # print(" ".join(map(str, target)), "\n")
    for i in range(len(target)):
        min_index = i
        for index in range(i, len(target)):
            if target[min_index] > target[index]:
                min_index = index
        target[i], target[min_index] = target[min_index], target[i]
        # print(" ".join(map(str, target)))
        # print(("  "*i)+"^")
    return target

def gnomesort(target:list):
    # ノームソート
    index = 0
    while index != len(target)-1:
        # print("  "+" ".join(map(str, target)))
        # print(("  "*(index+1))+"^ ^")
        if index == -1:
            index += 1
        elif target[index] <= target[index+1]:
            index += 1
        else:
            target[index], target[index + 1] = target[index + 1], target[index]
            index -= 1
    return target

def stoogesort(target:list):
    # ストゥージソート
    if target[0] > target[-1]:
        target[0], target[-1] = target[-1], target[0]
    if (listrange := len(target)) >= 3:
        kirutoko = int((listrange-1)*(2/3)) + (1 if str((listrange-1)*(2/3)).split(".")[1] != 0 else 0) # 切り上げ
        target[:kirutoko] = stoogesort(target[:kirutoko])
        target[-kirutoko:] = stoogesort(target[-kirutoko:])
        target[:kirutoko] = stoogesort(target[:kirutoko])
    return target

def mergesort(target:list):
    # マージソート
    def merge(rlist:list, llist:list) -> list:
        if rlist == []:
            returnlist = llist
        elif llist == []:
            returnlist = rlist
        else:
            returnlist = []
            rindex = 0
            lindex = 0
            while rindex != len(rlist) and lindex != len(llist):
                if rlist[rindex] >= llist[lindex]:
                    returnlist.append(llist[lindex])
                    lindex += 1
                else:
                    returnlist.append(rlist[rindex])
                    rindex += 1
            returnlist.extend(rlist[rindex:])
            returnlist.extend(llist[lindex:])
        return returnlist

    if len(target) <= 1:
        return target
    else:
        kirutoko = len(target)//2
        return merge(mergesort(target[:kirutoko]), mergesort(target[kirutoko:]))


def target_list():
    return [3, 1, 2, 1, 6, 0, 3, 9, 8]

def issorted(target:list) -> bool:
    for i in range(len(target)-1):
        if target[i] > target[i+1]:
            return False
    else:
        return True

def random_list_gen(num:int, maxnum:int = 9) -> list:
    import random
    return [random.randint(0, maxnum) for _ in range(num)]