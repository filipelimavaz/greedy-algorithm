from Graph import Graph as Graph
from Greedy import Greedy as Greedy

graph = Graph()

greedy_search = Greedy(graph.bucharest)
greedy_search.search(graph.arad)
