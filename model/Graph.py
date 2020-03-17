from pprint import pprint


class Graph:
    def __init__(self, nodes=None, links=None):
        if nodes is None:
            nodes = []
        if links is None:
            links = []
        self.nodes = nodes
        self.links = links

    # Find all links of all nodes
    def find_links(self):
        for node in self.nodes:
            links = []
            for link in self.links:
                if link.node_id_1 is node.node_id:
                    links.append(link)
                elif link.node_id_2 is node.node_id:
                    links.append(link)
            node.links = links

    # Calculate the spanning tree
    def spann_tree(self, min_pdu=1):
        for i in range(min_pdu):
            for node in self.nodes:
                self.broadcast(node)
        self.print_tree()

    # Send PDU to all links of node
    def broadcast(self, current_node):
        # Iterate through all links of the node
        for link in current_node.links:
            # Find node by id
            for next_node in self.nodes:
                current_node_cost = current_node.sum_cost + link.cost
                if (current_node.node_id is link.node_id_1 and next_node.node_id is link.node_id_2) or \
                        (current_node.node_id is link.node_id_2 and next_node.node_id is link.node_id_1):
                    # Check if the root id of the current node is lower then the next one
                    if current_node.root_id < next_node.root_id:
                        next_node.update(current_node.root_id, current_node_cost, link)
                        print(current_node.name, '=>', next_node.name)
                        self.broadcast(next_node)
                    # Check if the nodes have the same root node and the current node has a lower cost then the next one
                    elif current_node.root_id is next_node.root_id and current_node_cost < next_node.sum_cost:
                        next_node.update(current_node.root_id, current_node_cost, link)
                        print(current_node.name, '=>', next_node.name)
                        self.broadcast(next_node)

    # Print the spanning tree
    def print_tree(self):
        dict_tree = {}
        for node in self.nodes:
            if node.next_link.node_id_1 is not node.node_id:
                dict_tree[node.name] = node.next_link.node_id_1
            else:
                dict_tree[node.name] = node.next_link.node_id_2
        pprint(dict_tree, width=1)
