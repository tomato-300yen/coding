from collections import deque


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.level = None
        self.it = None

    def add_edge(self, fr, to, cap):
        """
        fr --(cap)--> to
        fr <---(0)--- to
        """
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        """
        v1 --(cap1)-> v2
        v1 <-(cap2)-- v2
        """
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, node_start, node_goal):
        """
        Return if node_gloal can be reached from node_start.
        """
        self.level = level = [None] * self.N
        deq = deque([node_start])
        level[node_start] = 0
        while deq:
            node_nxt = deq.popleft()
            lv = level[node_nxt] + 1
            for node_to, cap, _ in self.G[node_nxt]:
                # if cap > 0 and node_to is not visited
                if cap and level[node_to] is None:
                    level[node_to] = lv
                    deq.append(node_to)
        return level[node_goal] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10 ** 9 + 7
        G = self.G
        while self.bfs(s, t):
            (*self.it,) = map(iter, G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow
