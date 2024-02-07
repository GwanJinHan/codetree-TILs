import sys
input = sys.stdin.readline

n = int(input())
arr = list(set(map(int, input().split())))
m = bin(max(arr))[2:]
l = len(m)


class TrieNode:
    def __init__(self):
        self.left = None  # 0
        self.right = None  # 1


root = TrieNode()

for num in arr:
    t = root
    target = "0" * (l + 2 - len(bin(num))) + bin(num)[2:]

    for tar in target:
        if tar == "0":
            if t.left is None:
                t.left = TrieNode()
            t = t.left
        elif tar == "1":
            if t.right is None:
                t.right = TrieNode()
            t = t.right

ans = ""
t = root
for num in m:
    if num == "0":
        if t.right is None:
            t = t.left
            ans += "0"
        else:
            t = t.right
            ans += "1"
    elif num == "1":
        if t.left is None:
            t = t.right
            ans += "0"
        else:
            t = t.left
            ans += "1"

print(int(ans, 2))