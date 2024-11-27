from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []

    def set_parent(self, parent):
        assert self.parent is None, "parent already set."
        self.parent = parent
        parent.children.append(self)


class Tree:
    def __init__(self, n):
        self.nodes = {i: Node(i) for i in range(1, n+1)}
        self.root = self.nodes[1]
        self.record = {i: 0 for i in range(1, n+1)}

    def add_relation(self, parent, child):
        self.nodes[child].set_parent(self.nodes[parent])

    def add_record(self, idx, val):
        self.record[idx] += val 

    def build(self):
        q = deque([self.root])
        ans = [0] * (len(self.nodes) + 1)

        while q:
            cur = q.popleft()
            for child in cur.children:
                self.record[child.val] += self.record[cur.val]
                q.append(child)

        for i in range(1, len(self.nodes) + 1):
            ans[i] = self.record[i]
        return ans[1:]

n, m = map(int, input().split())
tree = Tree(n)

parent = list(map(int, input().split()))
for i, p in enumerate(parent):
    if p == -1:
        continue
    tree.add_relation(p, i + 1)

for _ in range(m):
    idx, val = map(int, input().split())
    tree.add_record(idx, val)

print(" ".join(map(str, tree.build())))
