import argparse
from time import sleep

from ant import Ant


def print_board(board_: list[list[int]]):
    for i in board_:
        for r in i:
            print("□" if r else "■", end=" ")
        print()
    print(f"\r\033[{len(board_)+1}A")


def main():
    parser = argparse.ArgumentParser(description="ラングトンのアリ実行するやつ\n止め方はキーボードによる介入")

    parser.add_argument("-H", help="マスの高さ デフォルト25", default=25, type=int)
    parser.add_argument("-W", help="マスの幅 デフォルト25", default=25, type=int)
    parser.add_argument("-N", help="アリの量 デフォルト1", default=1, type=int)
    parser.add_argument("-E", help="実行する回数、-1以下で無限 デフォルト5000", default=5000, type=int)
    parser.add_argument("-T", help="実行時の遅延、0以下で無し デフォルト0.01", default=0.01, type=float)
    parser.add_argument("-R", "--random", help="アリの場所をランダムにするか、フラッグ、無い場合すべて真ん中に出現", action='store_true')

    args = parser.parse_args()

    board = [[False for _ in range(args.W)] for __ in range(args.H)]

    ants = [Ant(board, args.random) for _ in range(args.N)]

    n = 0
    try:
        while n != args.E:
            for i in ants:
                i.walk()
            print_board(board)
            if args.T > 0:
                sleep(args.T)
            n += 1
    except KeyboardInterrupt:
        pass
    finally:
        print("\n"*(len(board)+1))


if __name__ == "__main__":
    main()
