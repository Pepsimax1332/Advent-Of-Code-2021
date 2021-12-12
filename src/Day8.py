from pathlib import Path

from Day7 import task_two

FILEPATH = f"{Path()}/data/day8.txt"

test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb 
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

test_data = [[d.split(" ") for d in t.split(" | ")] for t in test.split("\n")]

with open(FILEPATH, "r") as f:
    data = [[d.split(" ") for d in t.split(" | ")] for t in f.read().split("\n")]


def task_one(data):

    digits_count = {i:0 for i in range(10)}

    for i, o in data:
        for d in o:
            if len(d) == 2:
                digits_count[1] += 1
            elif len(d) == 4:
                digits_count[3] += 1
            elif len(d) == 3:
                digits_count[6] += 1
            elif len(d) == 7:
                digits_count[7] += 1

    return sum(digits_count.values())

if __name__ == "__main__":
    print(f"Solution to day 8 test task 1: {task_one(test_data)}")
    print(f"Solution to day 8 real task 1: {task_one(data)}")

    # print(f"Solution to day 7 test task 1: {task_two(test_data)}")
    # print(f"Solution to day 7 real task 1: {task_two(data)}")

