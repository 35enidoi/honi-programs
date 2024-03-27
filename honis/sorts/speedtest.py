"""
速度検証ファイル

下にあるプロファイルから選んでも良いし、新しくプロファイルを作ってもいい

matplotlibが必要。(Arch linuxは標準で入ってなかった)"""

from sorts import (bubblesort,
                   shakersort,
                   oddevensort,
                   combsort,
                   quicksort,
                   insertsort,
                   insertsort_optimized,
                   bogosort,
                   selectionsort,
                   gnomesort,
                   stoogesort,
                   mergesort,
                   bogo_mergesort,
                   comb_merge_quicksort,
                   insert_quicksort
                   )

from timeit import timeit

order_n__2 = (bubblesort, shakersort, oddevensort, insertsort, gnomesort, insertsort_optimized, selectionsort)
order_nlogn = (combsort, quicksort, mergesort)
order_tokusyu = (stoogesort,)
order_baka = (bogosort, )

sort_kumiawase = (insert_quicksort, comb_merge_quicksort)
sort_kumiawase_baka = (bogo_mergesort, )

def sortstress(mn_:int, mx_:int, haba_:int, samplenum:int, targets:list):
    def random_list_gen(num:int, maxnum:int = 9) -> list:
        import random
        return [random.randint(0, maxnum) for _ in range(num)]

    timedict_ = {i.__name__:{} for i in targets}
    print(f"stress test : min;{mn_} max;{mx_}, haba;{haba_}")
    X=[i for i in range(mn_, mx_+1, haba_)]
    print(X)
    for i in targets:
        print(f"currently running : {i.__name__}")
        for z in X:
            print(f"start stress : {z}")
            timedict_[i.__name__][z] = timeit("i(a)", "a=random_list_gen(z, 10000)", number=samplenum, globals=locals())/samplenum
    return X, timedict_

def showplots(X_:list, timedict_:dict, sortfunclist_:list):
    import matplotlib.pyplot as plt

    plt.title("sort graph", {"fontsize":25})
    plt.xlabel("values", {"fontsize":15})
    plt.ylabel("time", {"fontsize":15})
    for i in sortfunclist_:
        plt.plot(X_, [i for i in timedict_[i.__name__].values()], label=i.__name__)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    target = order_nlogn + sort_kumiawase
    showplots(*sortstress(1000, 10000, 1000, 100, target), target)