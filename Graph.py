from Node import Node as Node
from Adjacent import Adjacent as Adjacent
    
class Graph:
    arad = Node('Arad', 366)
    zerind = Node('Zerind', 374)
    oradea = Node('Oradea', 380)
    timisoara = Node('Timisoara', 329)
    sibiu = Node('Sibiu', 253)
    fagaras = Node('Fagaras', 178)
    lugoj = Node('Lugoj', 244)
    mehadia = Node('Mehadia', 241)
    dobreta = Node('Dobreta', 242)
    rimnicu_vilcea = Node('Rimnicu Vilcea', 193)
    pitesti = Node('Pitesti', 98)
    craivoa = Node('Craivoa', 160)
    bucharest = Node('Bucharest', 0)
    giurgiu = Node('Giurgiu', 77)
    urziceni = Node('Urziceni', 80)
    neamt = Node('Neamt', 234)
    iasi = Node('Iasi', 226)
    vaslui = Node('Vaslui', 199)
    hirsova = Node('Hirsova', 151)
    eforie = Node('Eforie', 161)

    arad.add_adjacent_city(Adjacent(zerind, 75))
    arad.add_adjacent_city(Adjacent(timisoara, 118))
    arad.add_adjacent_city(Adjacent(sibiu, 140))

    zerind.add_adjacent_city(Adjacent(arad, 75))
    zerind.add_adjacent_city(Adjacent(oradea, 71))

    oradea.add_adjacent_city(Adjacent(zerind, 71))
    oradea.add_adjacent_city(Adjacent(sibiu, 151))

    timisoara.add_adjacent_city(Adjacent(arad, 118))
    timisoara.add_adjacent_city(Adjacent(lugoj, 111))

    lugoj.add_adjacent_city(Adjacent(timisoara, 111))
    lugoj.add_adjacent_city(Adjacent(mehadia, 70))

    dobreta.add_adjacent_city(Adjacent(mehadia, 75))
    dobreta.add_adjacent_city(Adjacent(craivoa, 120))

    craivoa.add_adjacent_city(Adjacent(dobreta, 120))
    craivoa.add_adjacent_city(Adjacent(rimnicu_vilcea, 146))
    craivoa.add_adjacent_city(Adjacent(pitesti, 138))

    rimnicu_vilcea.add_adjacent_city(Adjacent(craivoa, 146))
    rimnicu_vilcea.add_adjacent_city(Adjacent(sibiu, 80))
    rimnicu_vilcea.add_adjacent_city(Adjacent(pitesti, 97))

    sibiu.add_adjacent_city(Adjacent(arad, 140))
    sibiu.add_adjacent_city(Adjacent(oradea, 151))
    sibiu.add_adjacent_city(Adjacent(fagaras, 99))
    sibiu.add_adjacent_city(Adjacent(rimnicu_vilcea, 80))

    fagaras.add_adjacent_city(Adjacent(sibiu, 99))
    fagaras.add_adjacent_city(Adjacent(bucharest, 211))

    pitesti.add_adjacent_city(Adjacent(rimnicu_vilcea, 97))
    pitesti.add_adjacent_city(Adjacent(craivoa, 138))
    pitesti.add_adjacent_city(Adjacent(bucharest, 101))

    bucharest.add_adjacent_city(Adjacent(fagaras, 211))
    bucharest.add_adjacent_city(Adjacent(pitesti, 101))
    bucharest.add_adjacent_city(Adjacent(giurgiu, 90))
    bucharest.add_adjacent_city(Adjacent(urziceni, 85))

    urziceni.add_adjacent_city(Adjacent(bucharest, 85))
    urziceni.add_adjacent_city(Adjacent(vaslui, 142))
    urziceni.add_adjacent_city(Adjacent(hirsova, 98))

    hirsova.add_adjacent_city(Adjacent(urziceni, 98))
    hirsova.add_adjacent_city(Adjacent(eforie, 86))

    vaslui.add_adjacent_city(Adjacent(urziceni, 142))
    vaslui.add_adjacent_city(Adjacent(iasi, 92))

    iasi.add_adjacent_city(Adjacent(vaslui, 92))
    iasi.add_adjacent_city(Adjacent(neamt, 87))

    neamt.add_adjacent_city(Adjacent(iasi, 87))