# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)

box = [[[], [[], [], []], [[[[], [[]], []], [['key']]]], [[], []]], [[[], []], [[]]]]

# logging.debug(box)

stack = []


def look_for_key(box):
    for item in box:
        # if (isinstance(item, list) & len(item) > 1):
        if len(item) != 0: 
            logging.debug(f'item is not empty')
            if item[0] != 'key':
                logging.debug(f'item is not key')
                look_for_key(item)
            else:
                logging.debug(f'-- found {len(item)} thing: {item[0]}')


logging.debug('I\'am looking for a key...')
look_for_key(box)


'''
def look_for_key(box):
    global stack
    logging.debug(f'stack at the beginning {len(stack)}')
    put_box_on_stack(box)
    # pile = box
    # while pile is not empty:
    #     box.
    while stack:
        tookbox = stack.pop()
        for item in box:
            logging.debug(f' Item size: {len(item)}')
            if len(tookbox) > 1:
                put_box_on_stack(tookbox)
            else:
                logging.debug(f'-- looking at the only item: {item}')




def put_box_on_stack(box):
    global stack
    for item in box:
        if isinstance(item, list):
            stack.append(item)
            logging.debug(f'found list, put it on stack. Stack is now: {len(stack)}')


# put_box_on_stack(box)
look_for_key(box)
'''
