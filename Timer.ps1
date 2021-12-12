# echo "Time taken for results for day 1 task 1:"
# python -m timeit -n 1_000 -r 5 -s 'import src.Day1 as day1' 'day1.task(day1.data)'
# echo "Time taken for results for day 1 task 2:"
# python -m timeit -n 1_000 -r 5 -s 'import src.Day1 as day1' 'day1.task(day1.data, 3)'
# echo ""


# echo "Time taken for results for day 2 task 1:"
# python -m timeit -n 1_000 -r 5 -s 'import src.Day2 as day2' 'day2.task_one(day2.data)'
# echo "Time taken for results for day 2 task 2:"
# python -m timeit -n 1_000 -r 5 -s 'import src.Day2 as day2' 'day2.task_two(day2.data)'
# echo ""

# echo "Time taken for results for day 3 task 1:"
# python -m timeit -n 1_000 -r 5 -s 'import src.Day3 as day3' 'day3.task_one(day3.data, 12)'
# echo "Time taken for results for day 3 task 2:"
# python -m timeit -n 1_000 -r 5 -s 'import src.Day3 as day3' 'day3.task_two(day3.data, 12)'
# echo ""


# echo "Time taken for results for day 4 task 1:"
# python -m timeit -n 10 -r 5 -s 'import src.Day4 as day4' 'day4.Bingo(day4.data).play()'
# echo "Time taken for results for day 4 task 2:"
# python -m timeit -n 10 -r 5 -s 'import src.Day4 as day4' 'day4.Bingo(day4.data).last_win()'
# echo ""


# echo "Time taken for results for day 5 task 1:"
# python -m timeit -n 10 -r 5 -s 'import src.Day5 as day5' 'day5.task_one(day5.data)'
# echo "Time taken for results for day 5 task 2:"
# python -m timeit -n 10 -r 5 -s 'import src.Day5 as day5' 'day5.task_two(day5.data)'
# echo ""


echo "Time taken for results for day 6 task 1:"
python -m timeit -n 1_0 -r 5 -s 'import src.Day6 as day6' 'day6.task_one(day6.data)'
echo "Time taken for results for day 6 task 2:"
python -m timeit -n 1_0 -r 5 -s 'import src.Day6 as day6' 'day6.task_two(day6.data)'
echo ""


echo "Time taken for results for day 7 task 1:"
python -m timeit -n 1_0 -r 5 -s 'import src.Day7 as day7' 'day7.task_one(day7.data)'
echo "Time taken for results for day 7 task 2:"
python -m timeit -n 1_0 -r 5 -s 'import src.Day7 as day7' 'day7.task_two(day7.data)'
echo ""