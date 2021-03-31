from collections import deque


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
        None is returned if negative loop was found.
        """
        assert 0 <= node_start < self._n
        list_bellman = [initval] * self._n
        list_bellman[node_start] = 0
        queue = deque([node_start])
        count = 0
        while queue:
            node_now = queue.popleft()
            for edge_nxt in self._edges[node_now]:
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                new_cost = list_bellman[node_now] + cost_nxt
                if list_bellman[node_nxt] > new_cost:
                    list_bellman[node_nxt] = new_cost
                    queue.append(node_nxt)
                    # negative loop was found
                    if count == self._n:
                        return None
                    count += 1
        return list_bellman


N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
g = GraphList(N)
for a, b, c in ABC:
    g.add_edge(a - 1, b - 1, -c, directed=True)
bf_list = g.bellman_ford(node_start=0)
print(-bf_list[-1] if bf_list else "inf")
