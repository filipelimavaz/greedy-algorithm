import numpy as np

class OrderedVector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.valor_list = np.empty(self.capacity, dtype=object)

    def print(self):
        if self.last_position == -1:
            print('List is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.valor_list[i].city_name, ' - ', self.valor_list[i].target_distance)

    def add(self, node):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return
        
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.valor_list[i].target_distance > node.target_distance:
                break
            if i == self.last_position:
                position = i + 1
        x = self.last_position

        while x >= position:
            self.valor_list[x + 1] = self.valor_list[i]
            x -= 1
        
        self.valor_list[position] = node
        self.last_position += 1