from collections import deque

# Function to calculate the squared distance between two points
def squared_distance(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

# Function to find the minimum number of lighthouses involved
def min_lighthouses_to_alert(n, lighthouses):
    # Adjacency list to store lighthouses that each lighthouse can pass the beam to
    adj = [[] for _ in range(n)]
    
    # For each lighthouse, find the nearest lighthouse (in both clockwise and counterclockwise direction)
    for i in range(n - 1):  # We don't need to process the last one (chief guard's lighthouse)
        distances = []
        for j in range(n):
            if i != j:
                dist = squared_distance(lighthouses[i], lighthouses[j])
                distances.append((dist, j))
        
        # Sort the distances to find the nearest lighthouse
        distances.sort()
        
        # The nearest lighthouse (smallest distance) will be the one we can send the beam to
        adj[i] = [j for _, j in distances]
    
    # Now we need to use BFS to find the shortest path from lighthouse 0 to lighthouse n-1 (chief's lighthouse)
    visited = [False] * n
    queue = deque([(0, 0)])  # (current lighthouse index, number of lighthouses involved)
    visited[0] = True
    
    while queue:
        current, steps = queue.popleft()
        
        # If we reach the chief guard's lighthouse, return the number of lighthouses involved
        if current == n - 1:
            return steps
        
        # Visit all the adjacent lighthouses
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, steps + 1))
    
    return -1  # In case no path is found, but the problem guarantees a path

# Input reading
n = int(input())  # Number of lighthouses
lighthouses = [tuple(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
print(min_lighthouses_to_alert(n, lighthouses))
