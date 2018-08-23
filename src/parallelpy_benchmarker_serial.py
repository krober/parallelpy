from datetime import datetime

num_top_iterations = 10
num_nested_iterations = 500000


def top_function():

    results = []

    args = [1] * num_top_iterations

    for arg in args:
        nested_function(arg, results)

    return results


def nested_function(a, results):

    for i in range(num_nested_iterations):
        a *= 2

    result = a

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

