class GraphMat:
    def __init__(self, maxsize=10 ** 6):
        """
        nodes : 0, 1, 2, ... , n-1
        edges[node_i][node_j] describes cost between node_i and node_j
        """
        self._n = maxsize  # number of nodes
        self._edges = [
            [0 for _ in range(self._n)] for _ in range(self._n)
        ]  # adjacency matrix

    def add_edge(self, a, b, cost, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        self._edges[a][b] = cost
        if not directed:
            self._edges[b][a] = cost

    def bellman_ford(self):
        """
        Return distance matrix
        """
        bf_list = [
            [0 if i == j else float("inf") for i in range(self._n)]
            for j in range(self._n)
        ]
        for k in range(self._n):
            for i in range(self._n):
                for j in range(self._n):
                    bf_list[i][j] = min(bf_list[i][j], bf_list[i][k] + bf_list[k][j])
        return bf_list
