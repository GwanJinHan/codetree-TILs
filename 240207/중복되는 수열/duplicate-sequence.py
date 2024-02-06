import sys
input = sys.stdin.readline

n = int(input())

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(10)]
    

root = TrieNode()
flag = False

def insert_word(s):
    global flag
    t = root

    for char in s:
        index = int(char)
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        if t.is_end:
            flag = True
        
        t = t.children[index]
    
    if t.is_end:
        flag = True
    else:
        t.is_end = True


for _ in range(n):
    insert_word(input().rstrip())
    if flag:
        break

print(0 if flag else 1)