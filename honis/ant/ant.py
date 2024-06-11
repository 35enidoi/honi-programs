import random


class Ant:
    #             左        下      右      上
    DIRECTIONS = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def __init__(self, board: list[list[bool]], random_pos: bool = False) -> None:
        r"""
\ __/
 |---|-[] << アリだよ～
/ ￣\
        """
        self.board = board
        self.board_size = (len(board), len(board[0]))
        self.direction = 0
        if random_pos:
            self.position_y = random.randint(0, self.board_size[0]-1)
            self.position_x = random.randint(0, self.board_size[1]-1)
        else:
            self.position_y = self.board_size[0] // 2
            self.position_x = self.board_size[1] // 2

    def walk(self) -> None:
        # 自分の場所見て向き変える
        if self.board[self.position_y][self.position_x]:
            self.direction += 1
        else:
            self.direction -= 1

        # 色変える
        self.board[self.position_y][self.position_x] = not self.board[self.position_y][self.position_x]

        # 場所の増分について取得
        y_add, x_add = self.DIRECTIONS[self.direction % 4]

        # ぶち込む
        self.position_y += y_add
        self.position_x += x_add

        # yについてマスの範囲超えてないか見る
        if self.position_y == -1:
            self.position_y = self.board_size[0] - 1
        elif self.position_y == self.board_size[0]:
            self.position_y = 0

        # xも同様
        if self.position_x == -1:
            self.position_x = self.board_size[1] - 1
        elif self.position_x == self.board_size[1]:
            self.position_x = 0
