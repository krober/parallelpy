from datetime import datetime
from parallelpy import Parallelizer

num_top_iterations = 10
num_nested_iterations = 500000


def top_function():

    results = []

    args = [1] * num_top_iterations

    par = Parallelizer(
        target=nested_function,
        args=args,
        enable_results=True,
        auto_proc_count=True,
        max_proc_count=8
    )

    # par.run()

    # for arg in args:
    #     nested_function(arg, results)

    results = par.run()
    return results


# def nested_function(a):

#     for i in range(num_nested_iterations):
#         a *= 2


def nested_function(a, results):

    for i in range(num_nested_iterations):
        a *= 2

    result = (a,)

    results.append(result)


def main():

    pre_calc_time = datetime.now()
    results = top_function()
    calc_time = datetime.now() - pre_calc_time

    print('\n****************************')
    print('Calc time=', calc_time)
    print('****************************')


if __name__ == '__main__':

    main()
