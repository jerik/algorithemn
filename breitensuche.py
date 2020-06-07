# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
from collections import deque
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')

graph = {}


def main():
    global graph
    graph['du'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['tom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['tom'] = []
    graph['jonny'] = []
    logging.debug(f'graph: {graph}')

    search('du')


def search(name):
    global graph
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    logging.debug(f'Start searching with: {name}')

    while search_queue:
        person = search_queue.popleft()
        logging.debug(f'Person: {person}')
        if person not in searched:
            # import pdb; pdb.set_trace()
            if person_is_seller(person):
                logging.debug(f'{person} ist mangohaendler')
                print(person + " ist Mangohaendler!")
                return True
            else:
                search_queue += graph[person]
                logging.debug(f'added: graph[{person}]')
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    main()
