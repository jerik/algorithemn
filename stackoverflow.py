import logging
import sys
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')
# logging.debug('Step: %s' % guess)
# print <map object at ...>: print(list(result))
# import pdb; pdb.set_trace()


# https://stackoverflow.com/a/62478167/1933185
def main():
    input = 'C3:32,11'

    with open('test.txt', 'r') as f:
        head = lambda x: x[0:x.find(':')]  # get head of line from 0 to position of :
        # use if ... else list comprehension and save output in box
        box = [input + '\n' if head(line) == head(input) else line for line in f.readlines()]

    with open('test.txt', 'w') as f:
        [f.write(line) for line in box]  # overwrite test.txt with content of box


def hey(ho):
    print(ho)
    logging.debug(ho)


if __name__ == '__main__':
    main()
