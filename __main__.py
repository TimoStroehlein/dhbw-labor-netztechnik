import os
import re

from Test import Test
from model.Graph import Graph
from model.Link import Link
from model.Node import Node


def read_file():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/graph.st'), 'r') as file:
        nodes = []
        links = []
        for line in file:
            # Check if line is node
            result = re.search('^\\s*([a-zA-Z]+)\\s?=\\s?([0-9]*);.*', line)
            if result:
                nodes.append(Node(result.group(2), result.group(1)))
                result.group(1)
            # Check if line is link
            result = re.search('^\\s*([a-zA-Z]+)\\s?-\\s?([a-zA-Z])\\s?:\\s?([0-9]*);.*', line)
            if result:
                links.append(Link(result.group(1), result.group(2), int(result.group(3))))
        return Graph(nodes, links)


def print_graph(graph):
    print('Node count: ', graph.nodes.count())
    print('Link count: ', graph.links.count())


def main():
    # Init
    graph = read_file()
    graph.find_links()
    # Test
    test = Test(graph)
    if not test.check_node_ids_greater_zero():
        return
    print('')
    if not test.check_one_root_id():
        return
    if test.check_graph_connected() is not graph.nodes.count():
        return
    if not test.check_node_connected_to_itself():
        return
    print_graph(graph)
    # Calculate
    graph.spann_tree(10)


if __name__ == '__main__':
    main()
