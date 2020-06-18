# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys, pdb
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')
# logging.debug('Step: %s' % guess)
# print <map object at ...>: print(list(result))
# pdb.set_trace()


def main():
    fibunacci()
    # test_fibs()
    # list_comprehension()


def hey(ho):
    print(ho)
    logging.debug(ho)


# https://stackoverflow.com/a/21857893/1933185
def fibunacci():
    logging.debug('-' * 12)
    fibus = [0, 1]
    for i in range(2, 13):
        fibus.append(fibus[i-1] + fibus[i-2])
    hey('fibus: %s' % fibus)


def test_fibs():
    fibus = [0, 1]
    fibus = fibus + [fibus.append(fibus[i-1] + fibus[i-2]) for i in range(2, 50)]*0
    hey(fibus)


# https://www.programiz.com/python-programming/list-comprehension
# alternative: https://www.datacamp.com/community/tutorials/python-list-comprehension
# nice to know: https://stackoverflow.com/a/231855/1933185
def list_comprehension():
    h_letters = []
    for letter in 'human':
        h_letters.append(letter)

    hey('for loop: ' + ('%s ' * len(h_letters)) % tuple(h_letters))

    # Syntax of list comprehension
    # [expression FOR item IN list]
    lc_letters = [letter for letter in 'human']
    hey('list comprehension: ' + ('%s ' * len(lc_letters)) % tuple(lc_letters))

    lb_letters = list(map(lambda x: x, 'human'))
    hey('list + map + lambda: ' + ('%s ' * len(lb_letters)) % tuple(lb_letters))

    # one if
    number_list = [x for x in range(20) if x % 2 == 0]
    hey('number_list: %s' % number_list)

    # two if's
    num_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
    hey('num_list: %s' % num_list)

    # if ... else
    obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
    hey('obj: %s' % obj)

    transposed = []
    matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    hey('transposed with for loop: %s' % transposed)

    matrix = [[1, 2], [3, 4], [5, 7], [7, 8]]
    transpose = [[row[i] for row in matrix] for i in range(2)]
    hey('transpose: %s' % transpose)


def tinker_filter():
    # logging.debug((lambda x: x * x)(3))
    logging.debug('-' * 10)
    seq = [10, 7, 23, 12, 5, 4, 3, 11, 0, 1]
    filtered_result = filter(lambda x: x > 4, seq)
    logging.debug(list(filtered_result))
    # pdb.set_trace()


def tinker_guru():
    # CALL A REGULAR FUNCTION
    guru(printer_one, 'Printer 1 REGULAR CALL')
    guru(printer_two, 'Printer 2 REGULAR CALL \n')
    # CALL A REGULAR FUNCTION THROUGH A LAMBDA
    guru(lambda: printer_one('Printer 1 LAMBDA CALL'))
    guru(lambda: printer_two('Printer 2 LAMBDA CALL'))
    # TINKER
    guru(lambda: print('Print statement with lambda'))


# A REGULAR FUNCTION
def guru(funct, *args):
    funct(*args)


def printer_one(arg):
    return print(arg)


def printer_two(arg):
    print(arg)


# https://www.guru99.com/python-lambda-function.html
def more_tinker():
    string = 'some kind of a useless lambda'
    logging.debug(lambda string: print(string))

    x = 'Here we go with lambda'
    logging.debug((lambda x: logging.debug(x))(x))
    (lambda x: print(x))(x)


def lambda_tinker():
    foo = lambda x, y: x * x + y
    z = 10
    bar = lambda x, y: foo(x, z) + foo(y, z)
    logging.debug(foo(5, 2))
    logging.debug(bar(5, 2))
    # pdb.set_trace()


def step_two():
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x % 2 == 0), my_list))
    logging.debug('new_list: %s' % new_list)
    # logging.debug(f'new_list: {new_list}')


# https://www.programiz.com/python-programming/anonymous-function
def step_one():
    double = lambda x: x * 2
    logging.debug('double: %s' % double(5))


if __name__ == '__main__':
    main()
