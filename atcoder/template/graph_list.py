from collections import deque
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

    def add_edge(self, a, b, cost=1, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        self._edges[a].append(cost * self._n + b)
        if not directed:
            self._edges[b].append(cost * self._n + a)

    def dijkstra(self, node_start, initval=float("inf")):
        """
        Return shoretet distance to each nodes from node_start
        """
        assert 0 <= node_start < self._n
        list_dijkstra = [initval] * self._n
        heapnode_dist = [node_start]
        while heapnode_dist:
            # Where to visit
            node_now = heapq.heappop(heapnode_dist)
            cost, node_to = divmod(node_now, self._n)
            # Continue if visited
            if list_dijkstra[node_to] != initval:
                continue
            # Visit
            list_dijkstra[node_to] = cost

            # Update cost of nodes adjacent to the node(node_to).
            for edge_nxt in self._edges[node_to]:
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                # continue if visited
                if list_dijkstra[node_nxt] != initval:
                    continue
                # Update cost
                heapq.heappush(heapnode_dist, (cost + cost_nxt) * self._n + node_nxt)
        return list_dijkstra

    def bellman_ford(self, node_start, initval=float("inf")):
        """
        Return shoretet distance to each nodes from node_start.
        None is returned if negative loop was found
        """
        assert 0 <= node_start < self._n
        list_bellman = [initval * self._n]
        queue = deque([node_start])
        count = 0
        while queue:
            node_now = queue.popleft()
            for edge_nxt in self._edges[node_now]:
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                new_cost = list_bellman[node_now] + cost_nxt
                if list_bellman[node_nxt] > new_cost:
                    list_bellman[node_nxt] = new_cost
                    queue.push(node_nxt)
                    # negative loop was found
                    if count == self._n:
                        return None
                    count += 1
        return list_bellman

    def prim(self, node_start, initval=float("inf"), return_edge_num=False):
        """
        Return the cost of min spanning tree (, and its number of edges)
        """
        assert 0 <= node_start < self._n
        list_prim = [initval] * self._n
        heapnode_dist = [node_start]
        edge_num = 0
        while heapnode_dist:
            # Where to visit
            node_now = heapq.heappop(heapnode_dist)
            cost, node_to = divmod(node_now, self._n)
            # Continue if visited
            if list_prim[node_to] != initval:
                continue
            # Visit
            list_prim[node_to] = cost
            edge_num += 1

            # Update cost of nodes adjacent to the node(node_to).
            for edge_nxt in self._edges[node_to]:
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                # continue if visited
                if list_prim[node_nxt] != initval:
                    continue
                # Update cost
                heapq.heappush(heapnode_dist, cost_nxt * self._n + node_nxt)
        return sum(list_prim), edge_num if return_edge_num else list_prim
