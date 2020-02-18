# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')


def main():
    sorted = quicksort([10, 5, 2, 3, 12, 33, 1, 22, 17, 11])
    print('sorted result: %s' % sorted)
    logging.debug('sorted result: %s' % sorted)


def quicksort(array):
    if len(array) < 2:
        logging.debug('return array %s' % array)
        return array
    else:
        pivot = array[0]
        sliced = array[1:]
        logging.debug('pivot: %s and sliced: %s' % (pivot, sliced))
        less = [i for i in sliced if i <= pivot]
        greater = [i for i in sliced if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    main()
