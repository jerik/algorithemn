# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
import random
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')

# running from vim
# error with local...
# :! export LANG="de_DE.UTF-8"; py %


def main():
    # tupel()
    # tupelzuweisung()
    # testthis()
    # zufall()
    listcomp()


def listcomp():
    town = [letter for letter in "Frankfurt"]
    reihe = [int(zahl)**2 for zahl in "123456789"]
    reihe = [zahl + 4 for zahl in range(1, 11)]
    reihe = [zahl/4 for zahl in range(1, 100)]
    buffer = reihe
    hey(buffer)


def hey(ho):
    print(ho)
    logging.debug(ho)


def tupel():
    tupel = 'a', 'b', 'c', 'd', 'e'
    print(tupel)
    # logging.debug(f'{tupel}')
    tupell = ('a', 'b', 'c', 'd', 'e', 'f')
    print(tupell)
    tl = ('a',)
    print(type(tl))
    print(tupell[1:3])
    tupell = ('A',) + tupell[1:]
    print(tupell)


def tupelzuweisung():
    a, b = 1, 7
    a, b, c = 1, 'zwerg', 7
    # print(f'{a} und {b} macht {c}')


def swap(x, y):
    return y, x


def testthis():
    c = 'wirding'
    a, b = swap(1, 2)
    # print(f'{a} und {b} macht {c}')


def zufall():
    for i in range(10):
        x = random.random()
        print(x)


if __name__ == '__main__':
    main()
