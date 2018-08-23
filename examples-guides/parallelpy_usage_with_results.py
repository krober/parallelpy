from datetime import datetime
from parallelpy import Parallelizer

num_top_iterations = 10
num_nested_iterations = 500000


def top_function():

    results = []

    # args can be a list of single values
    args = [1] * num_top_iterations

    # or args can be a list of some data structure
    # if you need to pass multiple args - whatever
    # nested_function needs to process
    # args = [(1, 2)] * num_top_iterations

    par = Parallelizer(
        target=nested_function, # function to multiproc
        args=args, # list of args from above
        enable_results=True, # enable results list?
        auto_proc_count=True, # enable core count auto-calc?
        max_proc_count=8 # max cores/procs to run simul. - double your actual should be fine
    )

    results = par.run()

    return results


def nested_function(a, results):

    for i in range(num_nested_iterations):
        a *= 2

    # 'return' values can be single value
    result = a

    # or can be multiple values, but again should
    # be encapsulated in a data structure to prevent
    # race conditions: 
    # result = (a, b, c) 

    """
    Race Condition:
        results.append(a)
        results.append(b)
        results.append(c)
    Not Race Condition:
        result = (a, b, c)
        results.append(result)

    You will end up with a list of tuples in this case
    """

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

