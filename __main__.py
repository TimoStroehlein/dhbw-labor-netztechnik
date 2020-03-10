import json
import os

from src.model.Graph import Graph
from src.model.Link import Link
from src.model.Node import Node

path = '/media/timo/DATA/PycharmProjects/dhbw-labor-netztechnik/'


def main():
    with open(os.path.join(path, 'files/graph.json'), 'r') as file:
        data = json.load(file)
        nodes = []
        links = []
        if data['nodes']:
            for node in data['nodes']:
                if node['node_id'] and node['cost']:
                    nodes.append(Node(node['node_id'], node['cost']))

        if data['links']:
            for link in data['links']:
                if link['node_id_1'] and link['node_id_2'] and link['cost']:
                    links.append(Link(link['node_id_1'], link['node_id_2'], link['cost']))

        graph = Graph(nodes, links)
        print(graph)


if __name__ == '__main__':
    main()
