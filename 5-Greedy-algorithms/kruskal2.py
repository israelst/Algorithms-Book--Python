
# For me, it does not look like a set, but the book call it this way
class Set():
    def __init__(self, node):
        self.name = node
        self.rank = 0
        self.parent = self

    def find(self):
        "Find the root of the set. This root element is a convenient representative, or name, for the set"
        node = self.parent
        while node.parent != node: node = node.parent
        return node

    def union(self, other_set):
        root1 = self.find()
        root2 = other_set.find()
        if root1 != root2:
            if root1.rank > root2.rank:
                root2.parent = root1
            else:
                root1.parent = root2
                if root1.rank == root2.rank: root2.rank += 1

    def __repr__(self):
        return self.name

