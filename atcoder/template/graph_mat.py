import heapq


class GraphMat:
    def __init__(self, maxsize=10 ** 6, initval=float("inf")):
        """
        nodes : 0, 1, 2, ... , n-1
        edges[node_i][node_j] describes cost between node_i and node_j
        """
        self._n = maxsize  # number of nodes
        self._edges = [[0 if i == j else initval for j in range(self._n)] for i in range(self._n)]  # adjacency matrix

    def add_edge(self, a, b, cost, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        self._edges[a][b] = cost
        if not directed:
            self._edges[b][a] = cost

    def dijkstra(self, node_start, initval=float("inf")):
        """
        Return shoretet distance to each nodes from node_start
        """
        assert 0 <= node_start < self._n
        l_dij = [initval] * self._n
        l_dij[node_start] = 0
        heapnode_dist = [(0, node_start)]  # (distance, node)
        while heapnode_dist:
            cost, node_now = heapq.heappop(heapnode_dist)
            if l_dij[node_now] != initval:
                continue
            # visit
            l_dij[node_now] = cost
            for node_to, dist in enumerate(self._edges[node_now]):
                if node_to == node_now or dist == float("inf"):
                    continue
                heapq.heappush(heapnode_dist, (cost + dist, node_to))
        return l_dij

    def bellman_ford(self, node_start=None):
        """
        Return distance matrix
        """
        assert (0 <= node_start < self._n) or node_start is None
        bf_list = [[0 if i == j else float("inf") for i in range(self._n)] for j in range(self._n)]
        for k in range(self._n):
            for i in range(self._n):
                if node_start is not None and node_start != i:
                    continue
                for j in range(self._n):
                    bf_list[i][j] = min(bf_list[i][j], bf_list[i][k] + bf_list[k][j])
        return bf_list if node_start is None else bf_list[node_start]

    def find_negative_loop(self):
        return False
