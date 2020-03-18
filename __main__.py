import json
import os
import re

from model.Graph import Graph
from model.Link import Link
from model.Node import Node

path = '/mnt/DATA/PycharmProjects/dhbw-labor-netztechnik/'


def read_file():
    with open(os.path.join(path, 'files/graph.st'), 'r') as file:
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


def main():
    graph = read_file()
    graph.find_links()
    graph.spann_tree(10)


if __name__ == '__main__':
    main()
