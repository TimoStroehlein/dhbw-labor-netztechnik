class Graph:
    def __init__(self, nodes=None, links=None):
        if nodes is None:
            nodes = []
        if links is None:
            links = []
        self.nodes = nodes
        self.links = links
        self.counter = 0

    # Find all links of all nodes
    def find_links(self):
        for node in self.nodes:
            links = []
            for link in self.links:
                if link.node_id_1 is node.name:
                    links.append(link)
                elif link.node_id_2 is node.name:
                    links.append(link)
            node.links = links

    # Calculate the spanning tree
    def spann_tree(self):
        self.counter = 0
        for current_node in self.nodes:
            self.broadcast(current_node)

    # Send PDU to all links of node
    def broadcast(self, current_node):
        # Iterate through all links of the node
        for link in current_node.links:
            # Find node by id
            for next_node in self.nodes:
                current_node_cost = current_node.sum_cost + link.cost
                if (current_node.name is link.node_id_1 and next_node.name is link.node_id_2) or \
                        (current_node.name is link.node_id_2 and next_node.name is link.node_id_1):
                    next_node.msg_count += 1
                    # Check if the root id of the current node is lower then the next one
                    if current_node.root_id < next_node.root_id:
                        next_node.root_id = current_node.root_id
                        next_node.sum_cost = current_node_cost
                        next_node.next_link = link
                        self.counter += 1
                        self.print_step()
                        self.broadcast(next_node)
                    # Check if the nodes have the same root node and the current node has a lower cost then the next one
                    elif current_node.root_id is next_node.root_id and current_node_cost < next_node.sum_cost:
                        next_node.root_id = current_node.root_id
                        next_node.sum_cost = current_node_cost
                        next_node.next_link = link
                        self.counter += 1
                        self.print_step()
                        self.broadcast(next_node)

    # Print step of iteration
    def print_step(self):
        print('Step', self.counter, ':')
        for node in self.nodes:
            if node.next_link.node_id_2 is node.name:
                print('name:', node.name, '\tid:', node.node_id, '\tcost:', node.sum_cost, '\tmsg_count:', node.msg_count,'\tnext_link:',
                      node.next_link.node_id_2, '->', node.next_link.node_id_1)
            elif node.next_link.node_id_1 is node.name:
                print('name:', node.name, '\tid:', node.node_id, '\tcost:', node.sum_cost, '\tmsg_count:', node.msg_count, '\tnext_link:',
                      node.next_link.node_id_1, '->', node.next_link.node_id_2)

    # Print the spanning tree
    def print_tree(self):
        print('Result:')
        for node in self.nodes:
            if node.next_link.node_id_2 is node.name:
                print(node.name, '->', node.next_link.node_id_1)
            elif node.next_link.node_id_1 is node.name:
                print(node.name, '->', node.next_link.node_id_2)

    # Print costs from all nodes to the root node
    def print_costs(self):
        print('Costs to root:')
        for node in self.nodes:
            print(node.name, ':', node.sum_cost)
