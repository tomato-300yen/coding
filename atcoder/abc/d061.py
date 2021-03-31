class GraphList:
    def __init__(self, maxsize=10 ** 6):
        """
        nodes : 0, 1, 2, ... , n-1
        edges[node_from] describes edges from node_from
        Edge type(edge_type) defines the type of element of edges  :
            'cost_mod'   -- cost*n + node_to
            'unweighted' -- node_to
        """
        self._n = maxsize  # number of nodes
        self._edges = [[] for _ in range(self._n)]  # adjacency list

    def add_edge(self, a, b, cost=1, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        self._edges[a].append(cost * self._n + b)
        if not directed:
            self._edges[b].append(cost * self._n + a)

    def bellman_ford(self, node_start, initval=float("inf")):
        """
        Negative cost can be treated.
        Return shoretet distance to each nodes from node_start.
        None is returned if negative loop was found. (Only for undirected)
        """
        assert 0 <= node_start < self._n
        d = [initval] * self._n
        d[node_start] = 0
        count = 0
        while True:
            update = False
            # for all edges
            for i, e_list in enumerate(self._edges):
                for e in e_list:
                    cost, node_to = divmod(e, self._n)
                    if (d[i] != float("inf")) and (d[node_to] > d[i] + cost):
                        d[node_to] = d[i] + cost
                        update = True
            if not update:
                break
            count += 1
            if count == self._n:
                return None
        return d

    def find_negative_loop(self):
        """
        Return if the graph has negative looop. (only for undirected)
        """
        d = [0] * self._n
        # from node i
        for i in range(self._n):
            # for all edges
            for j, e_line in enumerate(self._edges):
                for e in e_line:
                    cost, node_nxt = divmod(e, self._n)
                    if d[node_nxt] > d[j] + cost:
                        d[node_nxt] = d[j] + cost

                        if i == self._n - 1:
                            return True
        return False


N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
g = GraphList(N)
for a, b, c in ABC:
    g.add_edge(a - 1, b - 1, -c, directed=True)
bf_list = g.bellman_ford(node_start=0)
print(-bf_list[-1] if bf_list else "inf")
