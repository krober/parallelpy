from datetime import datetime
# from timeit import timeit

from parallelpy import Parallelizer

num_top_iterations = 10
num_nested_iterations = 500000


def top_function():

    args = [i for i in range(num_top_iterations)]

    par = Parallelizer(
        target=nested_function,
        args=args,
        enable_results=True,
        auto_proc_count=True,
        max_proc_count=8
    )

    results = par.run()

    return results


def nested_function(a, results):

    n = 1

    for i in range(num_nested_iterations):
        n *= 2

    result = a

    results.append(result)


def print_results(results):

    print()
    print(results)


def main():

    # print(timeit(stmt=top_function,
    #              number=10))

    pre_calc_time = datetime.now()
    results = top_function()
    calc_time = datetime.now() - pre_calc_time

    print_results(results)

    print('\n****************************')
    print('Calc time=', calc_time)
    print('****************************')


if __name__ == '__main__':

    main()

