from datetime import datetime
# from timeit import timeit

num_top_iterations = 10
num_nested_iterations = 500000


def top_function():

    results = []

    args = [i for i in range(num_top_iterations)]

    for arg in args:
        nested_function(arg, results)

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

    print_results(results)
    
    print('\n****************************')
    print('Calc time=', calc_time)
    print('****************************')
    
    
if __name__ == '__main__':

    main()
