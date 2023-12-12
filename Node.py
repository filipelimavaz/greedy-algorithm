class Node:
    def __init__(self, city_name, target_distance):
        self.city_name = city_name
        self.visited = False
        self.target_distance = target_distance
        self.adjacent_cities = []

    def add_adjacent_city(self, adjacent):
        self.adjacent_cities.append(adjacent)
    
    def print_adjacent_cities(self):
        for i in self.adjacent_cities:
            print(i.node.city_name, i.cost)