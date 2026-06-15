"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        adj_list = {}
        queue = deque([node])

        while queue:
            for i in range(len(queue)):
                curr = queue.pop()
                if curr.val not in adj_list:
                    adj_list[curr.val] = set()
                    for neighbor in curr.neighbors:
                        queue.appendleft(neighbor)
                        adj_list[curr.val].add(neighbor.val)

        node_map = {}
        
        def getOrCreate(val):
            if val not in node_map:
                node_map[val] = Node(val)
            return node_map[val]

        def addNeighbor(curr, val):
            val_node = getOrCreate(val)
            if curr.neighbors and curr.neighbors.count(val_node) > 0:
                return
            if curr.neighbors == None:
                curr.neighbors = [val_node]
            else:
                curr.neighbors.append(val_node)
            if val_node.neighbors == None:
                val_node.neighbors = [curr]
            else:
                val_node.neighbors.append(curr)
        
        for curr_val in adj_list:
            curr_node = getOrCreate(curr_val)
            for neighbor in adj_list[curr_val]:
                addNeighbor(curr_node, neighbor)

        return node_map[node.val]
            