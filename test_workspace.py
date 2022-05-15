from search import *
from statistics import pvariance
import heapq
class PriorityFrontier(Frontier):


    def __init__(self):
        # The constructor does not take any arguments.
        self.container = []
        # Complete the rest
        self.entrycount = 0
        self.expanded = set()

    def add(self, path):
        variance = pvariance([arc.cost for arc in path])
        heapq.heappush(self.container, (sum(arc.cost for arc in path), variance, self.entrycount, path))
        self.entrycount+=1
        
    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional information for iteration."""
        return self

    def __next__(self):
        # Complete
        while True:
            if len(self.container) > 0:
                cost, variance, entrycount, path = heapq.heappop(self.container)
                if path[-1].head not in self.expanded:
                    self.expanded.add(path[-1].head)
                    return path
            else:
                raise StopIteration   # raise this when the container is exhuasted



graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)


graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A', 1), ('S','B',2),
               ('A', 'G', 3), ('B', 'G', 2)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)



graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'C', 'G'},
    edge_list=[('S','A', 1), ('S','C',2), ('S', 'B', 2),
               ('A', 'G', 3), ('C', 'G', 2), ('B', 'G', 2)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)