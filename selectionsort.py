# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug('Test logger')


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        logging.debug(f'index {i} and item {arr[i]}')
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    logging.debug('#' * 15)
    logging.debug(f'array length start: {len(arr)}')
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        logging.debug(f'found smallest index: {smallest} => item: {arr[smallest]}')
        new_arr.append(arr.pop(smallest))
        logging.debug(f'array length is now {len(arr)}')
    return new_arr


print(selection_sort([5, 3, 6, 2, 19]))
