import getopt
import os
import re
import sys

from controller.Test import Test
from controller.Graph import Graph
from model.Link import Link
from model.Node import Node

MAX_IDENT = 10
MAX_ITEMS = 100000
MAX_COST = 10000
MAX_NODE_ID = 100000


def read_file():
    # Get inputfile from command line
    inputfile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:', ['ifile='])
    except getopt.GetoptError:
        print('You need to pass at least one argument:')
        print('__main__.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
    if len(sys.argv) < 3:
        print('You need to pass at least one argument:')
        print('__main__.py -i <inputfile>')
        sys.exit(2)
    # Read file
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), inputfile), 'r') as file:
        nodes = []
        links = []
        counter = 0
        print('Input:')
        for line in file:
            counter += 1
            # Check if the maximum number of items has been reached
            if counter > MAX_ITEMS:
                break
            # Check if line is node
            result = re.search('^\\s*([a-zA-Z][a-zA-Z0-9]*)\\s?=\\s?([0-9]*);.*', line)
            if result:
                # Check if name exceeds max length
                if len(result.group(1)) > MAX_IDENT:
                    continue
                # Check if node id exceeds max number
                if int(result.group(2)) > MAX_NODE_ID:
                    continue
                # Check if name is root (reserved)
                if result.group(1) is 'Root':
                    continue
                nodes.append(Node(int(result.group(2)), result.group(1)))
                print(nodes[-1].name, ':', nodes[-1].node_id)
                continue
            # Check if line is link
            result = re.search('^\\s*([a-zA-Z][a-zA-Z0-9]*)\\s?-\\s?([a-zA-Z][a-zA-Z0-9]*)\\s?:\\s?([0-9]*);.*', line)
            if result:
                # Check if name exceeds max length
                if len(result.group(1)) > MAX_IDENT or len(result.group(2)) > MAX_IDENT:
                    continue
                # Check if link cost exceeds max cost
                if int(result.group(3)) > MAX_COST:
                    continue
                # Check if name is root (reserved)
                if result.group(1) is 'Root' or result.group(2) is 'Root':
                    continue
                links.append(Link(result.group(1), result.group(2), int(result.group(3))))
                print(links[-1].node_id_1, '-', links[-1].node_id_2, ':', links[-1].cost)
                continue
            # Check if line is comment
            result = re.search('//.*', line)
            if result:
                continue
            # Check if line is empty
            result = re.search('^\\s*$', line)
            if result:
                continue
            print('Error in line (', counter, '): ', line)

        return Graph(nodes, links)


def main():
    # Init
    graph = read_file()
    graph.find_links()
    # Test
    test = Test(graph)
    result, msg = test.check_node_ids_greater_zero()
    if not result:
        print('Error on node with id', msg, ', ids cannot be 0 or less.')
        return
    result, msg = test.check_one_root_id_exists()
    if not result:
        print('Root with id', msg, 'cannot exist multiple times.')
        return
    result, msg1, msg2 = test.check_node_connected_to_itself()
    if not result:
        print('Node with link', msg1, '-', msg2, 'cannot be connected to itself.')
        return
    result, msg1, msg2 = test.check_link_uniqueness()
    if not result:
        print('Link', msg1, '-', msg2, 'cannot exist more than once.')
        return
    if not test.check_graph_connected():
        print('Graph is not connected.')
        return
    print('All tests passed.')
    print('Node count:', len(graph.nodes))
    print('Link count:', len(graph.links))
    # Calculate
    graph.spann_tree()
    graph.print_tree()
    graph.print_costs()


if __name__ == '__main__':
    main()
