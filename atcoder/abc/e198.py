import heapq


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
        self._prev = []

    def add_edge(self, a, b, cost=1, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        self._edges[a].append(cost * self._n + b)
        if not directed:
            self._edges[b].append(cost * self._n + a)

    def dijkstra(self, node_start, initval=float("inf"), C=[]):
        """
        Return shoretet distance to each nodes from node_start
        """
        assert 0 <= node_start < self._n
        list_dijkstra = [initval] * self._n
        # list_prev = [-1] * self._n
        list_rslt = []
        list_color = [set([C[i]]) for i in range(self._n)] if C else None
        heapnode_dist = [(node_start, 0)]
        while heapnode_dist:  # O(N)
            # Where to visit
            node_now, node_fr = heapq.heappop(heapnode_dist)  # O(logN)
            cost, node_to = divmod(node_now, self._n)
            # Continue if visited
            if list_dijkstra[node_to] != initval:
                continue
            # Visit
            list_dijkstra[node_to] = cost
            # list_prev[node_to] = node_fr
            if C[node_to] not in list_color[node_fr]:
                list_rslt.append(node_to + 1)
            list_color[node_to] = list_color[node_to] | list_color[node_fr]

            # Update cost of nodes adjacent to the node(node_to).
            for edge_nxt in self._edges[node_to]:  # O(M)
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                # continue if visited
                if list_dijkstra[node_nxt] != initval:
                    continue
                # Update cost
                heapq.heappush(heapnode_dist, ((cost + cost_nxt) * self._n + node_nxt, node_to))  # O(logN)
        # self._prev = list_prev
        return list_dijkstra, list_rslt


N = int(input())
C = list(map(int, input().split()))
AB = [map(int, input().split()) for _ in range(N - 1)]
g = GraphList(N)
for a, b in AB:
    g.add_edge(a - 1, b - 1)
list_dij, list_rslt = g.dijkstra(0, C=C)
print(1)
print(*sorted(list_rslt), sep="\n")
