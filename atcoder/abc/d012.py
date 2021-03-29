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

    def bellman_ford(self, initval=float("inf")):
        """
        Return distance matrix
        """
        bf_list = [
            [initval if i != j and el == 0 else el for i, el in enumerate(ll)]
            for j, ll in enumerate(self._edges)
        ]
        for k in range(self._n):
            for i in range(self._n):
                for j in range(self._n):
                    bf_list[i][j] = min(bf_list[i][j], bf_list[i][k] + bf_list[k][j])
        return bf_list


N, M = map(int, input().split())
g = GraphMat(N)
for i in range(M):
    a, b, t = map(int, input().split())
    g.add_edge(a - 1, b - 1, t)
dist_mat = g.bellman_ford()
ans = min([max(ll) for ll in dist_mat])
print(ans)
