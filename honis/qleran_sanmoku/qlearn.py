from random import uniform, randint
from copy import deepcopy


class QLearn:
    def __init__(self, sabori: float = 0.1, waribiki: float = 0.9, gakusyuu: float = 0.1) -> None:
        self.__Q: dict[str, list[float]] = {}
        self.n = 0

        self.__sabori = sabori
        self.__waribiki = waribiki
        self.__gakusyuu = gakusyuu

    @property
    def Q(self) -> dict[str, list[float]]:
        return deepcopy(self.__Q)

    def action_selector(self, state: str, actions: tuple[int, ...]) -> tuple[int, float]:
        if state not in self.__Q:
            # Qに状態がないとき
            self.__Q[state] = [0.0]*len(actions)
            return randint(0, len(actions)-1), 0.0

        if uniform(0, 1) < self.__sabori:
            # さぼるとき
            action = randint(0, len(actions)-1)
            return action, self.__Q[state][action]
        else:
            # Qから最適解を使うとき
            return self.action_selector_qmax(state, actions)

    def action_selector_qmax(self, state: str, actions: tuple[int, ...]) -> tuple[int, float]:
        if state not in self.__Q:
            # Qに状態がないとき
            return randint(0, len(actions)-1), 0.0
        else:
            # Qから最適解を出す
            max_num = max((self.__Q[state][i] for i in range(len(actions))))
            return self.__Q[state].index(max_num), max_num

    def update_q(self,
                 state: str,
                 action: int,
                 qnum: float,
                 reward: float,
                 next_states: str,
                 next_actions: tuple[int, ...]) -> None:
        td_error = reward + self.__waribiki*self.action_selector_qmax(next_states, next_actions)[1] - qnum
        self.__Q[state][action] += self.__gakusyuu * td_error

    def update_q_on_end(self, state: str, qnum: float, reward: float) -> None:
        if state not in self.__Q:
            self.__Q[state] = [0.0]

        td_error = reward - qnum
        self.__Q[state][0] += self.__gakusyuu * td_error

        self.n += 1
