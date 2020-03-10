class Graph:
    def __init__(self, nodes=None, links=None):
        if nodes is None:
            nodes = []
        if links is None:
            links = []
        self.nodes = nodes
        self.links = links
