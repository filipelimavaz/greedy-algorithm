# Greedy Search - Arad to Bucharest Route Problem 🌍

This is a greedy search algorithm developed to solve the famous problem of finding the most efficient route from Arad to Bucharest, passing through various cities in Romania.

## Problem Description 🗺️

The problem consists of finding the least costly path from Arad to Bucharest, where each city is a node, and the roads between them are edges, each with an associated cost.

## Greedy Search Algorithm 🚀

Greedy search is an informed search algorithm that uses heuristics to prioritize the exploration of promising paths. In this case, the algorithm tries to move towards the city that appears closest to Bucharest, considering a straight line and not the mileage cost of the roads. This is the best search method if we do not want to consider geological factors such as the curvature of the Earth or inclines/depressions in the roads since these factors can increase or decrease the distance to the goal.

![Arad to Bucharest map](https://github.com/filipelimavaz/greedy-algorithm/blob/main/map.png)

## Classes

### 1. `OrderedVector`

The `OrderedVector` class represents an ordered vector used in greedy search to prioritize nodes with lower cost.

- **Methods:**
  - `__init__(self, capacity)`: Initializes the ordered vector with a specific capacity.
  - `print(self)`: Prints the elements of the vector.
  - `add(self, node)`: Adds a node to the vector while maintaining order.

### 2. `Node`

The `Node` class represents a node in the graph, which in this context, is a city in Romania.

- **Attributes:**
  - `city_name`: Name of the city.
  - `visited`: Flag to indicate if the node was visited during the search.
  - `target_distance`: Distance to the destination (Bucharest).
  - `adjacent_cities`: List of adjacent cities.

- **Methods:**
  - `add_adjacent_city(self, adjacent)`: Adds an adjacent city to the list.
  - `print_adjacent_cities(self)`: Prints the adjacent cities.

### 3. `Greedy`

The `Greedy` class represents the greedy search algorithm to find the most efficient path to the destination.

- **Methods:**
  - `__init__(self, target)`: Initializes the algorithm with the destination node.
  - `search(self, current_city)`: Executes the greedy search from a city.

### 4. `Graph`

The `Graph` class represents the graph that contains the nodes/cities and their connections.

### 5. `Adjacent`

The `Adjacent` class represents an edge between two nodes, indicating the traversal cost.

- **Attributes:**
  - `node`: Adjacent node.
  - `cost`: Cost of traversal to the adjacent node.
