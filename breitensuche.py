# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
from collections import deque
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')


def main():
    graph = {}
    graph['du'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['tom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['tom'] = []
    graph['jonny'] = []

    search_queue = deque()
    search_queue += graph['du']

    while search_queue:
        person = search_queue.popleft()
        logging.debug(f'Person: {person}')
        if person_is_seller(person):
            logging.debug(f'{person} ist mangohaendler')
            print(person + " ist Mangohaendler!")
            return True
        else:
            search_queue += graph[person]
            logging.debug(f'added: graph[{person}]')


def person_is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    main()
