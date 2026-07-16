from collections import deque


graph = {
    3: [1, 2],
    1: [4],
    2: [5],
    4: [],
    5: []
}

def bfs(start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
            queue.extend(graph[node])  
    return traversal

result = bfs(3)
print("BFS Traversal:", result)
