class Test:
    def __init__(self, graph=None):
        self.graph = graph
        self.visited_node_ids = []

    def check_node_ids_greater_zero(self):
        for node in self.graph.nodes:
            if node.node_id < 1:
                return False
        return True

    def check_one_root_id(self):

        # TODO: ???
        return True

    def check_graph_connected(self, node=None):
        if node is None:
            node = self.graph.nodes.index(0)
        # Check if already visited
        for node_id in self.visited_node_ids:
            if node_id is node.node_id:
                return 0
        for link in node.links:
            if link.node_id_1 is node.name:
                for node2 in self.graph.nodes:
                    if node2.name is link.node_id_2:
                        self.visited_node_ids.append(node)
                        return 1 + self.check_graph_connected(node2)
            elif link.node_id_2 is node.name:
                for node2 in self.graph.nodes:
                    if node2.name is link.node_id_1:
                        self.visited_node_ids.append(node)
                        return 1 + self.check_graph_connected(node2)
        # TODO: check if graph is connected
        return 0

    def check_node_connected_to_itself(self):
        for link in self.graph.links:
            if link.node_id_1 is link.node_id_2:
                return False
        return True
