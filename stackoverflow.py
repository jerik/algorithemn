import logging
import sys
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')
# logging.debug('Step: %s' % guess)
# print <map object at ...>: print(list(result))
# import pdb; pdb.set_trace()


# https://stackoverflow.com/q/62478289/1933185
def main():
    ini_list = [('G 05', 'Over-Speed', '1.63'), ('Load 23A_UF', 'Over-Voltage', '11.37'), ('Load 21A_UF', '11.38'), ('Load 08A_UF', '11.38'), ('Load 07A_UF', '11.38'), ('Load 12A_UF', '11.38'), ('Load 24A_UF', '11.38'), ('Load 15A_UF', '11.38'), ('Load 16A_UF', '11.38'), ('Load 04A_UF', '11.38'), ('Load 03A_UF', '11.38'), ('Load 18A_UF', '11.38'), ('Load 25A_UF', '11.38'), ('Load 27A_UF', '11.39'), ('Load 26A_UF', '11.39'), ('G 05', 'Over-Speed', '1.63'), ('G 05', 'Over-Voltage', '1.63'), ('NSG_2', 'OverVoltage', '2.72'), ('G 01', 'Out of Step', '2.72')]

    reasons = {'sum_of_reasons': 0}
    for item in ini_list:
        reason = lambda x: 'No Reason Given' if len(x) == 2 else x[1]
        add_fault(reason(item), reasons)
    # https://docs.python.org/3/library/stdtypes.html#old-string-formatting
    # https://stackabuse.com/python-string-interpolation-with-the-percent-operator/
    {print('%s: %s this is %.2f' % (k, reasons[k], reasons[k]/reasons['sum_of_reasons'])) for k in reasons}

def add_fault(fault, reasons):
    reasons['sum_of_reasons'] += 1
    if fault in reasons:
        reasons[fault] += 1
    else:
        reasons[fault] = 1

# https://stackoverflow.com/a/62478167/1933185
def find_line():
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
