from pathlib import Path

FILEPATH = f"{Path()}/data/day4.txt"


test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


with open(FILEPATH, "r") as f:
     data = f.read()


class Bingo:
    

    def __init__(self, data: str, *args, **kwargs):

        self.set_up_game(data)


    def set_up_game(self, data):

        data = data.split("\n\n")
        self.game_numbers = list(map(int, data[0].split(",")))

        self.boards = [Board(data[i], i-1) for i in range(1, len(data))]


    def play(self):

        for round in self.game_numbers:
            for board in self.boards:

                if board.mark_board(round):
                    return board.solve(round)


    def last_win(self):

        last_result = None
        winning = []

        for round in self.game_numbers:
            for board in self.boards:
                if board.mark_board(round) and board not in winning:
                    last_result = board.solve(round)
                    winning.append(board)

        return last_result


class Board:
    

    def __init__(self, data: str, num, *args, **kwargs):

        self.rows = [list(map(int, d.split())) for d in data.split("\n")]
        self.cols = [list(col) for col in zip(*self.rows)]

        self.name = num


    def mark_board(self, number: int):

        self.rows = [[True if x == number else x for x in row] for row in self.rows]
        self.cols = [[True if x == number else x for x in col] for col in self.cols]

        if self.check(self.rows) or self.check(self.cols):

            return True


    def check(self, lst):

        for l in lst:
            if all([x == True for x in l]):
                return True


    def solve(self, number: int):

        return number * sum(list(filter(lambda x: type(x) != type(True), sum(self.cols, []))))


if __name__ == "__main__":
    print(f"Solution to day 4 test task 1: {Bingo(test).play()}")
    print(f"Solution to day 4 real task 1: {Bingo(data).play()}")

    print(f"Solution to day 4 test task 2: {Bingo(test).last_win()}")
    print(f"Solution to day 4 real task 2: {Bingo(data).last_win()}")

