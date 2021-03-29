import heapq


class GraphList:
    def __init__(self, maxsize=10 ** 6, edge_type="cost_mod"):
        """
        nodes : 0, 1, 2, ... , n-1
        edges[node_from] describes edges from node_from
        Edge type(edge_type) defines the type of element of edges  :
            'cost_mod'   -- cost*n + node_to
            'unweighted' -- node_to
        """
        self._n = maxsize  # number of nodes
        self._edges = [[] for _ in range(self._n)]  # adjacency list
        assert edge_type in set(["cost_mod", "unweighted"])
        self._edgetype = edge_type  # edgetype

    def add_edge(self, a, b, cost=None, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        if self._edgetype == "cost_mod" and cost is not None:
            pass
        elif self._edgetype == "unweighted" and cost is None:
            cost = 1
        else:
            assert False
        self._edges[a].append(cost * self._n + b)
        if not directed:
            self._edges[b].append(cost * self._n + a)

    def dijkstra(self, node_start, initval=float("inf")):
        """
        Return shoretet distance from node_start
        """
        assert 0 <= node_start < self._n
        dist_dijkstra = [initval] * self._n
        heapnode_dist = [node_start]
        while heapnode_dist:
            # Where to visit
            nodedist_now = heapq.heappop(heapnode_dist)
            cost, node_to = divmod(nodedist_now, self._n)
            # Continue if visited
            if dist_dijkstra[node_to] != initval:
                continue
            # Visit
            dist_dijkstra[node_to] = cost

            # Update cost of nodes adjacent to the node(node_to).
            for edge_nxt in self._edges[node_to]:
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                # continue if visited
                if dist_dijkstra[node_nxt] != initval:
                    continue
                # Update cost
                heapq.heappush(heapnode_dist, (cost + cost_nxt) * self._n + node_nxt)
        return dist_dijkstra


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N - 1)]
Q = int(input())
AB = [list(map(int, input().split())) for _ in range(Q)]
g = GraphList(N)
for x, y in XY:
    g.add_edge(x - 1, y - 1, 1)
d_list = []
for i in range(N):
    d_list.append(g.dijkstra(i))
for a, b in AB:
    print(d_list[a - 1][b - 1] + 1)
