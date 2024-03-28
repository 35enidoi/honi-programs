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
                   insert_quicksort,
                   stalin_mergesort
                   )

order_n__2 = (bubblesort, shakersort, oddevensort, insertsort, insertsort_optimized, gnomesort, selectionsort)
order_nlogn = (combsort, quicksort, mergesort)
order_tokusyu = (stoogesort,)
order_baka = (bogosort, )

sort_kumiawase = (insert_quicksort, comb_merge_quicksort)
sort_kumiawase_baka = (bogo_mergesort, )

mitisuu = (stalin_mergesort, )

def sortstress(mn_:int, mx_:int, haba_:int, samplenum:int, targets:list):
    from timeit import timeit
    def random_list_gen(num:int, maxnum:int = 9) -> list:
        import random
        return [random.randint(0, maxnum) for _ in range(num)]

    timedict_ = {i.__name__:{} for i in targets}
    print(f"sort test : min;{mn_} max;{mx_}, haba;{haba_}")
    X=[i for i in range(mn_, mx_+1, haba_)]
    print(X)
    for i in targets:
        print(f"current running:{i.__name__}")
        for z in X:
            print(f"start sort values:{z}")
            timedict_[i.__name__][z] = timeit("i(a)", "a=random_list_gen(z, 10000000)", number=samplenum, globals=locals())/samplenum
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
    # プロファイル
    # 要素数の下限、要素数の上限、増加の大きさ、サンプル数、使う関数の順。
    # int, int, int, int, tuple[function]

    # ソートできているかは見ないので注意。
    # 一々やってたら時間かかるし、そもそもtimeitがそういう事後にやるみたいなの対応してない。
    profiles = ((100, 1000, 100, 1000, order_n__2 + order_nlogn),# 0
                (100, 1000, 100, 1000, order_n__2[:6] + order_nlogn),# 1
                (1000, 5000, 500, 300, order_n__2[:6] + order_nlogn),# 2
                (5000, 10000, 500, 200, order_n__2[:6] + order_nlogn),# 3
                (10000, 20000, 2000, 100, order_n__2[:5] + order_nlogn),# 4
                (20000, 50000, 5000, 50, order_n__2[3:5] + order_nlogn),# 5
                (50000, 100000, 10000, 25, order_n__2[4:5] + order_nlogn),# 6

                (100, 1000, 100, 1000, order_n__2 + order_nlogn + mitisuu),# スターリン・マージソートの測定 7
                )
    target = profiles[1] # プロファイルをここで選ぶ
    showplots(*sortstress(*target), target[-1])