from collections import deque

def bfs(tree, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

tree = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F' , 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node = 'A'
print(f"BFS starting from node {start_node}: {bfs(tree, start_node)}")
