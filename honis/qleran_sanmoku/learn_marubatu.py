from random import choice
from typing import Callable

from matplotlib import pyplot

from qlearn import QLearn
from marubatugame import MaruBatuGame


def learn_marubatu(Q: QLearn, enemy: Callable[[str, tuple[int, ...]], int], num: int = 100) -> QLearn:
    player = True
    for _ in range(num):
        marubatu = MaruBatuGame()

        if not player:
            # 敵に打たせる
            marubatu.set(not player, enemy(marubatu.show_game(), marubatu.valid_positions))

        state = marubatu.show_game()

        while not marubatu.is_end:
            pos, qnum = Q.action_selector(state, marubatu.valid_positions)
            marubatu.set(player, marubatu.valid_positions[pos])

            if marubatu.is_end:
                # 終わっちゃったとき
                break

            marubatu.set(not player, enemy(marubatu.show_game(), marubatu.valid_positions))

            if marubatu.is_end:
                # 同文
                break

            new_state = marubatu.show_game()
            new_valid_positions = marubatu.valid_positions

            reward = 0
            if marubatu.reach_count[int(player)] != 0:
                # もし自分のリーチがあれば
                reward += 0.1
            if marubatu.reach_count[int(not player)] != 0:
                # もし相手がリーチしてたら
                reward -= 0.3

            Q.update_q(state, pos, qnum, reward, new_state, new_valid_positions)

            state = new_state

        if marubatu.winner is None:
            # 引き分け
            gameend_reward = 0.8
        elif marubatu.winner == player:
            # 自分の勝ち
            gameend_reward = 1.0
        else:
            # 自分の負け
            gameend_reward = -1.0

        Q.update_q_on_end(state, qnum, gameend_reward)

        player = not player  # プレーヤーの交代

    return Q


def battle_marubatu(Q: QLearn, enemy: Callable[[str, tuple[int, ...]], int], num: int = 100) -> tuple[int, int, int]:
    kati = 0
    hikiwake = 0
    make = 0

    player = True

    for _ in range(num):

        marubatu = MaruBatuGame()

        if not player:
            # 敵に打たせる
            marubatu.set(not player, enemy(marubatu.show_game(), marubatu.valid_positions))

        state = marubatu.show_game()

        while not marubatu.is_end:
            pos, _ = Q.action_selector_qmax(state, marubatu.valid_positions)
            marubatu.set(player, marubatu.valid_positions[pos])

            if marubatu.is_end:
                # 終わっちゃったとき
                break

            marubatu.set(not player, enemy(marubatu.show_game(), marubatu.valid_positions))

            if marubatu.is_end:
                # 同文
                break

            new_state = marubatu.show_game()
            state = new_state
        if marubatu.winner is None:
            # 引き分け
            hikiwake += 1
        elif marubatu.winner == player:
            # 自分の勝ち
            kati += 1
        else:
            # 自分の負け
            make += 1

        player = not player  # プレーヤーの交代

    return (kati, hikiwake, make)


def random_selector(state: str, valid_action: tuple[int, ...]) -> int:
    return choice(valid_action)


def main() -> None:
    qlearn = QLearn(sabori=0.1, waribiki=0.9, gakusyuu=0.05)

    katis = []
    hikiwakes = []
    makes = []

    for _ in range(100):
        qlearn = learn_marubatu(qlearn, random_selector, 1000)
        kati, hikiwake, make = battle_marubatu(qlearn, random_selector, num=1000)
        print(f"kati: {kati}, hikiwake: {hikiwake}, make: {make}")
        katis.append(kati)
        hikiwakes.append(hikiwake)
        makes.append(make)

    print(qlearn.n)

    pyplot.plot(katis, label="Win")
    pyplot.plot(hikiwakes, label="Draw")
    pyplot.plot(makes, label="Lose")
    pyplot.ylim(0, 1000)

    pyplot.ylabel("num")

    pyplot.legend()

    pyplot.show()


if __name__ == "__main__":
    main()
