# see: https://github.com/egonschiele/grokking_algorithms
import logging
logging.basicConfig(filename='binary_search.log', level=logging.DEBUG)


def binary_search(mylist, item):
    low = 0
    high = len(mylist) - 1

    # import pdb; breakpoint()
    # logging.debug(mid)
    i = 1
    while low <= high:
        mid = (low + high) // 2
        guess = mylist[mid]
        logging.debug(f'Step {i}: {guess}')
        i += 1
        if guess == item:
            # return {mid: mylist[mid]}
            return f'Mid: {mid} => item: {mylist[mid]}'
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


mylist = list(range(1, 100))
mylist = list(range(1, 128))
mylist = list(range(1, 134959))  # with 8 position it takes a while
print(binary_search(mylist, 77))
