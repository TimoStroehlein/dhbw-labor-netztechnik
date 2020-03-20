class Test:
    def __init__(self, graph=None):
        self.graph = graph
        self.visited_node_ids = []

    def check_node_ids_greater_zero(self):
        for node in self.graph.nodes:
            if node.node_id < 1:
                return False, node.node_id
        return True, 0

    def check_one_root_id_exists(self):
        node_ids = []
        for node in self.graph.nodes:
            node_ids.append(node.node_id)
        node_ids.sort()
        if node_ids.__len__() > 1 and node_ids[0] is node_ids[1]:
            return False, node_ids[0]
        return True, 0

    def check_node_connected_to_itself(self):
        for link in self.graph.links:
            if link.node_id_1 is link.node_id_2:
                return False, link.node_id_1, link.node_id_2
        return True, '', ''

    def check_link_uniqueness(self):
        for i1 in range(len(self.graph.links)):
            for i2 in range(len(self.graph.links)):
                if i1 is i2:
                    continue
                l1 = self.graph.links[i1]
                l2 = self.graph.links[i2]
                if (l1.node_id_1 is l2.node_id_1 and l1.node_id_2 is l2.node_id_2) or \
                        (l1.node_id_1 is l2.node_id_2 and l1.node_id_2 is l2.node_id_1):
                    return False, l1.node_id_1, l1.node_id_2
        return True, '', ''

    def check_graph_connected(self, node=None):
        if node is None:
            node = self.graph.nodes[0]
        for visited_node_id in self.visited_node_ids:
            if visited_node_id is node.node_id:
                return 0
        self.visited_node_ids.append(node.node_id)
        # Check if already visited
        for link in node.links:
            if link.node_id_1 is node.name:
                for node2 in self.graph.nodes:
                    if node2.name is link.node_id_2:
                        self.check_graph_connected(node2)
            elif link.node_id_2 is node.name:
                for node2 in self.graph.nodes:
                    if node2.name is link.node_id_1:
                        self.check_graph_connected(node2)
        return len(self.graph.nodes) is len(self.visited_node_ids)
