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
    # enum()
    version2()

def hey(ho):
    print(ho)
    logging.debug(ho)

def version2():
    foo = 'abcdefghijklmnopqrstuvwxyz'
    bar = [v for i,v in enumerate(foo) if i % 2]
    hey(''.join(bar))
    # join works 
    seperator = ', '
    hey(seperator.join(foo))
    hey(seperator.join('halleluja'))

def enum(): 
    for idx,val in enumerate('hallo'): 
        hey('{}: {}'.format(idx,val))

if __name__ == '__main__':
    main()
