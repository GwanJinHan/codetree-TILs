import sys
input = sys.stdin.readline

n = int(input())


class TrieNode:
    def __init__(self, level):
        self.level = level
        self.children = {}


root = TrieNode(0)

for _ in range(n):
    _, *foods = input().rstrip().split()
    level = 0
    t = root
    for food in foods:
        level += 1
        if food not in t.children:
            t.children[food] = TrieNode(level)

        t = t.children[food]


def search(node):
    l = sorted(node.children.items())
    for name, child_node in l:
        print("--" * (child_node.level - 1), end="")
        print(name)
        search(child_node)


search(root)