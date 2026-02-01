from os import path
from random import choice


class Box:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.expects = set(range(1, 10))
        self.value: int | None = None

    def initialize(self) -> None:
        if self.value:
            self.expects = {self.value}
        else:
            self.expects = set(range(1, 10))


class Suudoku:
    def __init__(self, state: list[tuple[int, int, int]] | None = None) -> None:
        self.boxes = [[Box(row, col) for col in range(9)] for row in range(9)]
        self.state = state
        if state:
            for row, col, value in state:
                self.boxes[row][col].value = value

    def reset(self) -> None:
        for row in range(9):
            for col in range(9):
                self.boxes[row][col].value = None

        if self.state:
            for row, col, value in self.state:
                self.boxes[row][col].value = value

        for row in range(9):
            for col in range(9):
                self.boxes[row][col].initialize()

    def is_solved(self) -> bool:
        for row in range(9):
            for col in range(9):
                if self.boxes[row][col].value is None:
                    return False
        return True

    def is_invalid(self) -> tuple[str, int, int] | None:
        # 候補が一つもないboxがある場合
        for row in range(9):
            for col in range(9):
                box = self.boxes[row][col]
                if box.value is None and len(box.expects) == 0:
                    return "no expect", row, col
        # 行で重複チェック
        for row in range(9):
            seen = set()
            for col in range(9):
                value = self.boxes[row][col].value
                if value is not None:
                    if value in seen:
                        return "row duplicate", row, col
                    seen.add(value)
        # 列で重複チェック
        for col in range(9):
            seen = set()
            for row in range(9):
                value = self.boxes[row][col].value
                if value is not None:
                    if value in seen:
                        return "col duplicate", row, col
                    seen.add(value)
        # 3x3ブロックで重複チェック
        for block_row in range(3):
            for block_col in range(3):
                seen = set()
                for row in range(block_row * 3, block_row * 3 + 3):
                    for col in range(block_col * 3, block_col * 3 + 3):
                        value = self.boxes[row][col].value
                        if value is not None:
                            if value in seen:
                                return "block duplicate", row, col
                            seen.add(value)
        return None

    def set_value(self, row: int, col: int, value: int | None) -> None:
        self.boxes[row][col].value = value

    def execute(self) -> None:
        # 一回だけ解く
        # まずはそれぞれのboxを初期化
        for row in range(9):
            for col in range(9):
                self.boxes[row][col].initialize()

        changed = True
        while changed:
            changed = False

            # 行で見る
            for row in range(9):
                existing_values = {
                    self.boxes[row][col].value
                    for col in range(9)
                    if self.boxes[row][col].value is not None
                }
                for col in range(9):
                    if self.boxes[row][col].value is None:
                        self.boxes[row][col].expects -= existing_values

            # 列で見る
            for col in range(9):
                existing_values = {
                    self.boxes[row][col].value
                    for row in range(9)
                    if self.boxes[row][col].value is not None
                }
                for row in range(9):
                    if self.boxes[row][col].value is None:
                        self.boxes[row][col].expects -= existing_values

            # 3x3のブロックで見る
            for block_row in range(3):
                for block_col in range(3):
                    existing_values = set()
                    for row in range(block_row * 3, block_row * 3 + 3):
                        for col in range(block_col * 3, block_col * 3 + 3):
                            if self.boxes[row][col].value is not None:
                                existing_values.add(self.boxes[row][col].value)

                    for row in range(block_row * 3, block_row * 3 + 3):
                        for col in range(block_col * 3, block_col * 3 + 3):
                            if self.boxes[row][col].value is None:
                                self.boxes[row][col].expects -= existing_values

            # 候補が一つだけのboxを確定させる
            for row in range(9):
                for col in range(9):
                    box = self.boxes[row][col]
                    if box.value is None and len(box.expects) == 1:
                        box.value = box.expects.pop()
                        box.expects = {box.value}
                        changed = True

            if changed:
                continue

            # 行で見て、ある数字が入る候補が一つだけのboxを確定させる
            for row in range(9):
                expect_count = {num: [] for num in range(1, 10)}
                for col in range(9):
                    box = self.boxes[row][col]
                    if box.value is None:
                        for expect in box.expects:
                            expect_count[expect].append(box)

                for num, boxes in expect_count.items():
                    if len(boxes) == 1:
                        box = boxes[0]
                        box.value = num
                        box.expects = {num}
                        changed = True
                        break
                else:
                    continue
                break

            if changed:
                continue

            # 列も同様に
            for col in range(9):
                expect_count = {num: [] for num in range(1, 10)}
                for row in range(9):
                    box = self.boxes[row][col]
                    if box.value is None:
                        for expect in box.expects:
                            expect_count[expect].append(box)

                for num, boxes in expect_count.items():
                    if len(boxes) == 1:
                        box = boxes[0]
                        box.value = num
                        box.expects = {num}
                        changed = True
                        break
                else:
                    continue
                break

            if changed:
                continue

            # 3x3のブロックも同様に
            for block_row in range(3):
                for block_col in range(3):
                    expect_count = {num: [] for num in range(1, 10)}
                    for row in range(block_row * 3, block_row * 3 + 3):
                        for col in range(block_col * 3, block_col * 3 + 3):
                            box = self.boxes[row][col]
                            if box.value is None:
                                for expect in box.expects:
                                    expect_count[expect].append(box)

                    for num, boxes in expect_count.items():
                        if len(boxes) == 1:
                            box = boxes[0]
                            box.value = num
                            box.expects = {num}
                            changed = True
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break

            if changed:
                continue

    def print_suudoku(self, expect: bool = False) -> None:
        row_expects = []
        print("  | 1 2 3 | 4 5 6 | 7 8 9 |")
        print("-" * 27)
        for row in range(9):
            row_values = []
            for col in range(9):
                value = self.boxes[row][col].value
                if value:
                    row_values.append(str(value))
                else:
                    row_values.append("?")
                    row_expects.append(self.boxes[row][col])
            print(
                f"{row + 1} | {' '.join(row_values[0:3])} | {' '.join(row_values[3:6])} | {' '.join(row_values[6:9])} |"
            )
            if row % 3 == 2:
                print("-" * 27)

        if not expect:
            return

        if len(row_expects) == 0:
            print("No empty boxes.")
            return

        print("Expected values for empty boxes:")
        for box in row_expects:
            print(f"Box at ({box.row + 1}, {box.col + 1}): expects {sorted(box.expects)}")


if __name__ == "__main__":
    banmen_path = path.join(path.dirname(__file__), "banmen.txt")
    initial_puts = []

    if not path.exists(banmen_path):
        print(f"{banmen_path} not found.")
        exit(1)
    else:
        with open(banmen_path, "r") as f:
            for line in f:
                row, col, value = map(int, line.strip().split())
                initial_puts.append((row, col, value))
        suudoku = Suudoku(state=[(row - 1, col - 1, value) for row, col, value in initial_puts])
        print("Loaded initial values from banmen.txt.")

    print("Initial Suudoku:")
    suudoku.print_suudoku(expect=False)

    suudoku_box_value_history: list[tuple[int, int, int]] = []
    print("Solving Suudoku...")
    progressed = False
    while not suudoku.is_solved():
        suudoku.execute()
        suudoku.print_suudoku(expect=True)
        if suudoku.is_solved():
            print("solved")
            break
        if (invalid := suudoku.is_invalid()) is not None:
            if not progressed:
                if len(suudoku_box_value_history) == 0:
                    print("No more guesses to backtrack, puzzle may be unsolvable.")
                    break
                else:
                    print("Could not solve the puzzle.")
                    break
            print(f"backtrack reason: {invalid[0]} at ({invalid[1]+1}, {invalid[2]+1})")
            # 仮定が間違っていた場合、初期化してやり直す
            suudoku.reset()
            progressed = False
            continue
        else:
            # 進展がない場合、仮定を試みる
            min_ex_boxes = sorted((x for row in suudoku.boxes for x in row if x.value is None), key=lambda x: len(x.expects))
            min_box = None
            for box in min_ex_boxes:
                expects = box.expects - {x[2] for x in suudoku_box_value_history if x[0] == box.row and x[1] == box.col}
                if len(expects) == 0:
                    continue
                guess_value = choice(list(expects))
                suudoku.set_value(box.row, box.col, guess_value)
                suudoku_box_value_history.append((box.row, box.col, guess_value))
                print(f"Guessing value {guess_value} for box at ({box.row + 1}, {box.col + 1})")
                progressed = True
                break
            else:
                if not progressed:
                    print("No boxes available for guessing, puzzle may be unsolvable.")
                    break
                # すべての候補を試した場合、初期化してやり直す
                print("All candidates tried for all boxes, resetting to initial state.")
                suudoku.reset()
                progressed = False
                continue
