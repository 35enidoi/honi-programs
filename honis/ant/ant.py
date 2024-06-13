import random


class Ant:
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

        # 方向を見て足す
        if (direction := self.direction % 4) == 0:
            # 下
            self.position_y -= 1
            if self.position_y == -1:
                # 範囲外出たら逆の場所に戻す
                self.position_y = self.board_size[0] - 1
        elif direction == 1:
            # 左
            self.position_x -= 1
            if self.position_x == -1:
                # 同様
                self.position_x = self.board_size[1] - 1
        elif direction == 2:
            # 上
            self.position_y += 1
            if self.position_y == self.board_size[0]:
                # 同(ry
                self.position_y = 0
        elif direction == 3:
            # 右
            self.position_x += 1
            if self.position_x == self.board_size[1]:
                # (ry
                self.position_x = 0
