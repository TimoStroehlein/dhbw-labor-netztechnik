import os
import re

from controller.Test import Test
from controller.Graph import Graph
from model.Link import Link
from model.Node import Node


def read_file():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/graph.st'), 'r') as file:
        nodes = []
        links = []
        counter = 0
        for line in file:
            counter += 1
            # Check if line is node
            result = re.search('^\\s*([a-zA-Z]+)\\s?=\\s?([0-9]*);.*', line)
            if result:
                nodes.append(Node(int(result.group(2)), result.group(1)))
                continue
            # Check if line is link
            result = re.search('^\\s*([a-zA-Z]+)\\s?-\\s?([a-zA-Z])\\s?:\\s?([0-9]*);.*', line)
            if result:
                links.append(Link(result.group(1), result.group(2), int(result.group(3))))
                continue
            result = re.search('//.*', line)
            if result:
                continue
            print('Error in line (', counter, '): ', line)

        return Graph(nodes, links)


def print_graph(graph):
    print('Node count: ', graph.nodes.__len__())
    print('Link count: ', graph.links.__len__())


def main():
    # Init
    graph = read_file()
    graph.find_links()
    # Test
    test = Test(graph)
    if not test.check_node_ids_greater_zero():
        return
    print('')
    if not test.check_one_root_id_exists():
        return
    if test.check_graph_connected() is not graph.nodes.__len__():
        print('Graph is not connected.')
        return
    if not test.check_node_connected_to_itself():
        return
    print_graph(graph)
    # Calculate
    graph.spann_tree(10)


if __name__ == '__main__':
    main()
