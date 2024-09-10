from functools import lru_cache


class MaruBatuGame:
    MOVE = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))

    def __init__(self) -> None:
        self.__banmen: list[int] = [0]*9
        self.__valid_positions: set[int] = set(range(9))
        self.reach_count: tuple[int, int] = ()
        self.winner: None | bool = None

    @property
    def valid_positions(self) -> tuple[int, ...]:
        return tuple(self.__valid_positions)

    @property
    def is_end(self) -> bool:
        return self.winner is not None or len(self.__valid_positions) == 0

    def return_cache_info(self):
        return self.__winner_reach_wrap.cache_info()

    def set(self, player: bool, pos: int) -> None:
        if pos in self.__valid_positions:
            self.__valid_positions.remove(pos)
            self.__banmen[pos] = player + 1  # boolはintのサブクラスで0と1
            self.winner, self.reach_count = self.__winner_reach_wrap(tuple(self.__banmen))
        else:
            raise ValueError("もうすでに使われています。")

    @staticmethod
    @lru_cache(4096)
    def __winner_reach_wrap(state: tuple[int, ...]):
        def winner_search_static(state: tuple[int, ...]) -> None | bool:
            for a, b, c in MaruBatuGame.MOVE:
                if state[a] != 0 and state[a] == state[b] == state[c]:
                    return bool(state[a] - 1)

        def reach_count_static(state: tuple[int, ...]) -> tuple[int, int]:
            player1_reachcount = 0
            player2_reachcount = 0

            for i in MaruBatuGame.MOVE:
                count0 = count1 = count2 = 0
                for r in i:
                    if (banmennum := state[r]) == 0:
                        count0 += 1
                    elif banmennum == 1:
                        count1 += 1
                    else:
                        count2 += 1

                if count0 == 1:
                    if count1 == 2:
                        player1_reachcount += 1
                    elif count2 == 2:
                        player2_reachcount += 1

            return (player1_reachcount, player2_reachcount)

        return winner_search_static(state), reach_count_static(state)

    def show_game(self) -> str:
        game = ""
        for i in self.__banmen:
            game += "-" if i == 0 else "m" if i == 1 else "b"
        return game
