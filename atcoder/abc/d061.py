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

    def bellman_ford(self, start=None, initval=float("inf")):
        """
        Return distance matrix
        """
        bf_list = [
            [0 if i == j else initval if el == 0 else el for i, el in enumerate(line)]
            for j, line in enumerate(self._edges)
        ]
        for k in range(self._n):
            for i in range(self._n):
                if start is not None and start != i:
                    continue
                for j in range(self._n):
                    bf_list[i][j] = max(bf_list[i][j], bf_list[i][k] + bf_list[k][j])
        return bf_list


N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
g = GraphMat(N)
for a, b, c in ABC:
    g.add_edge(a - 1, b - 1, c, directed=True)
bf_list = g.bellman_ford(start=0, initval=0)
print(*g._edges, sep="\n")
print(*bf_list, sep="\n")
print(bf_list[0][-1])
