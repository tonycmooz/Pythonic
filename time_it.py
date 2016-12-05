import time


def time_it(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "\nThis process took {} seconds to execute".format(str((t2 - t1))) + "\n"
    return wrapper


@time_it
def sum_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nThe sum of all numbers in the given range: " + str((sum(num_list))))


print(sum_function())

