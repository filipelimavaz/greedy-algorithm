from OrderedVector import OrderedVector as OrderedVector

class Greedy:
    def __init__(self, target):
        self.target = target
        self.find = False

    def search(self, current_city):
        print('-----------')
        print('Current City: {}'.format(current_city.city_name))
        current_city.visited = True

        if current_city == self.target:
            self.find = True
        else:
            ordered_vector = OrderedVector(len(current_city.adjacent_cities))
            for adjacent in current_city.adjacent_cities:
                if adjacent.node.visited == False:
                    adjacent.node.visited = True
                    ordered_vector.add(adjacent.node)
                    
            ordered_vector.print()

            if ordered_vector.valor_list[0] != None:
                self.search(ordered_vector.valor_list[0])
