import json
import os

from model.Graph import Graph
from model.Link import Link
from model.Node import Node

path = '/mnt/DATA/PycharmProjects/dhbw-labor-netztechnik/'


def read_file():
    with open(os.path.join(path, 'files/graph.json'), 'r') as file:
        data = json.load(file)
        nodes = []
        links = []
        if data['nodes']:
            for node in data['nodes']:
                if node['node_id'] and node['name']:
                    nodes.append(Node(node['node_id'], node['name']))

        if data['links']:
            for link in data['links']:
                if link['node_id_1'] and link['node_id_2'] and link['cost']:
                    links.append(Link(link['node_id_1'], link['node_id_2'], link['cost']))
        return Graph(nodes, links)


def main():
    graph = read_file()
    graph.find_links()
    graph.spann_tree(1)


if __name__ == '__main__':
    main()
