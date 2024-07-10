from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS, initialized with the start node
    result = []  # List to store the order of visited nodes

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        
        if vertex not in visited:
            # If the vertex hasn't been visited yet
            visited.add(vertex)  # Mark it as visited
            result.append(vertex)  # Add it to the result list
            
            # Enqueue all adjacent vertices that haven't been visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
print(f"BFS starting from node {start_node}: {bfs(graph, start_node)}")
