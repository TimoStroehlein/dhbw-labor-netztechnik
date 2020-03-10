class Node:
    def __init__(self, node_id='', cost=0, p_link=None, next_hop=None, msg_count=0):
        self.node_id = node_id
        self.cost = cost
        self.p_link = p_link
        self.next_hop = next_hop
        self.msg_count = msg_count
