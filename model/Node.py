from model.Link import Link


class Node:
    def __init__(self, node_id=0, name='', links=None, sum_cost=0, next_link=Link(), msg_count=0):
        self.node_id = node_id
        self.name = name
        self.links = links          # All links
        self.root_id = node_id      # ID of the root
        self.sum_cost = sum_cost    # Sum cost from this node to the root node
        self.next_link = next_link  # Next link to the root
        self.msg_count = msg_count  # Broadcast message count
