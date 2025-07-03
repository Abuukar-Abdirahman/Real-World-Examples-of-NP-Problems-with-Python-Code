# Traveling Salesperson Problem (TSP) - Brute Force (Python)
from itertools import permutations

cities = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('B', 'C'): 35,
    ('B', 'A'): 10,
    ('C', 'A'): 15,
    ('C', 'B'): 35,
}

def total_distance(route):
    dist = 0
    for i in range(len(route)):
        dist += cities.get((route[i], route[(i+1)%len(route)]), float('inf'))
    return dist

all_routes = permutations(['A', 'B', 'C'])
shortest = min(all_routes, key=total_distance)
print("Shortest Route:", shortest)

