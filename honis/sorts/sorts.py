def bubblesort(target:list):
    # バブルソート
    for targetrange in reversed(range(1, len(target))):
        for r in range(targetrange-1):
            if target[r] > target[r+1]:
                target[r], target[r+1] = target[r+1], target[r]
            # print(" ".join(map(str, target)))
            # print("  "*(r) + "^ ^")
    return target

def shakersort(target:list):
    # シェーカーソート
    midnum = int(len(target)/2)
    for i in range(midnum):
        for r in range(i, len(target)-i-1):
            if target[r] > target[r+1]:
                target[r], target[r+1] = target[r+1], target[r]
        for r in reversed(range(i+1, len(target)-i)):
            if target[r] < target[r-1]:
                target[r], target[r-1] = target[r-1], target[r]
        # print(" ".join(map(str, target[:i+1])), "|", " ".join(map(str, target[i+1:-i-1])), "|", " ".join(map(str, target[-i-1:])))
    return target

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
    for i in range(len(target)):
        min_index = i
        for index in range(i, len(target)):
            if target[min_index] > target[index]:
                min_index = index
        target[i], target[min_index] = target[min_index], target[i]
    return target

def gnomesort(target:list):
    # ノームソート
    index = 0
    while index != len(target)-1:
        # print(index, target)
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
        kirutoko = int(((listrange-1)*(2/3))) + (1 if str((listrange-1)*(2/3)).split(".")[1] != 0 else 0) # 切り上げ
        target[:kirutoko] = stoogesort(target[:kirutoko])
        target[-kirutoko:] = stoogesort(target[-kirutoko:])
        target[:kirutoko] = stoogesort(target[:kirutoko])
    return target

def mergesort(target:list):
    def merge(rlist:list, llist:list) -> list:
        if rlist == []:
            returnlist = llist
        elif llist == []:
            returnlist = rlist
        else:
            returnlist = []
            while rlist != [] and llist != []:
                if rlist[-1] <= llist[-1]:
                    returnlist.append(llist.pop())
                else:
                    returnlist.append(rlist.pop())
            returnlist.extend(rlist)
            returnlist.extend(llist)
            returnlist.reverse()
        return returnlist

    if len(target) <= 1:
        return target
    else:
        kirutoko = len(target)//2
        return merge(mergesort(target[:kirutoko]), mergesort(target[kirutoko:]))