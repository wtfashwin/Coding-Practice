#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s

from queue import Queue

class Node():
    def __init__(self):
        self.distance = -1
        self.children = []
        self.visited = False

def bfs(n, m, edges, s):
    # Write your code here
    nodes = [Node() for _ in range(n)]
    for edge in edges:
        first, second = [nodes[i - 1] for i in edge]
        first.children.append(second)
        second.children.append(first)
    
    top = nodes[s - 1]
    top.distance = 0
    queue = Queue()
    queue.put(top)
    while(not queue.empty()):
        node = queue.get()
        for child in node.children:
            if (not child.visited) or (child.distance > node.distance + 6):
                child.distance = node.distance + 6
                child.visited = True
                queue.put(child)
    del nodes[s - 1]
    return [node.distance for node in nodes]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
