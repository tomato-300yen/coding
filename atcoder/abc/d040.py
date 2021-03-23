class Node:
    def __init__(self, val, parrent=None, children=[]):
        self.parrent_of_tree = parrent
        self.children = children
        self.val = val  # root

    def reset_children(self):
        self.children = []

    def add_children(self, node):
        self.children.append(node)

    def set_parrent(self, node):
        self.parrent_of_tree = node


class UnionFindTree:

    __all__ = ["find_root", "merge", "same", "size"]

    def __init__(self, maxsize=10 ** 6):
        assert maxsize > 0

        self._n = maxsize  # number of nodes
        # parent_or_size[V] ...
        #  if negative : V is the root of the group
        #                and the value*(-1) is the size of the tree
        #  else        : the value is the parent node of V
        # self._parent_or_size = [-1] * maxsize
        self._parent_or_size = [None(val=-1)] * maxsize

    def find_root_node(self, a):
        """Find the root of a. Dose not change tree structure"""
        assert 0 <= a < self._n

        node_pos = self._parent_or_size[a]
        while node_pos.val >= 0:
            node_pos = self._parent_or_size[node_pos.val]
        else:
            node_root_pos = node_pos
        return node_root_pos

    def merge(self, a, b):
        """Merge the group of a and the group of b"""
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a.val == root_b.val:
            return True
        else:
            # The size of the group of b should be larger
            if (
                -self._parent_or_size[root_a.val].val
                > -self._parent_or_size[root_b.val].val
            ):
                root_a, root_b = root_b, root_a
            # Merge the group of a with the group of b
            self._parent_or_size[root_b.val].val += self._parent_or_size[root_a.val].val
            self._parent_or_size[root_a.val].val = root_b.val
            # b is parent, a is child
            self._parent_or_size[root_a.val].set_parrent(root_b)
            self._parent_or_size[root_b.val].add_children(root_a)
            return False

    def same(self, a, b):
        """See if the group of a and the group of b are the same"""
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        return root_a == root_b

    def size(self, a):
        """Return the size of the group of a"""
        assert 0 <= a < self._n

        root_a = self.find_root(a)
        return -self._parent_or_size[root_a]


N, M = map(int, input().split())
ABY = [list(map(int, input().split())) for i in range(M)]
ABY = sorted(ABY, key=lambda x: -x[2])
Q = int(input())
VW = [list(map(int, input().split())) for i in range(Q)]

tree = UnionFindTree(N)
