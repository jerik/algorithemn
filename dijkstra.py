# see: https://github.com/egonschiele/grokking_algorithms
import logging, sys
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')

processed = []


def main():
    global processed
    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a'] = {}
    graph['a']['fin'] = 1
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}
    logging.debug(f'graph: {graph}')

    infinity = float('inf')

    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity

    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    logging.debug(f'--- Start calculating')
    node = find_lowest_cost_node(costs)
    while node is not None:
        logging.debug(f'node: {node}')
        cost = costs[node]
        logging.debug(f'cost: {cost}')
        neighbors = graph[node]
        logging.debug(f'neighbors: {neighbors}')
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            logging.debug(f'costs[n]: {costs[n]} > new_cost: {new_cost} ?')
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
                logging.debug(f'update costs[n]: {new_cost} and parents[n]: {node}')
        processed.append(node)
        logging.debug(f'processed: {processed}')
        node = find_lowest_cost_node(costs)

    logging.debug(f'Final costs: {costs}')
    logging.debug(f'Final parents: {parents}')


def find_lowest_cost_node(costs):
    global processed
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        logging.debug(f'\tflcn: {cost}')
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    main()
