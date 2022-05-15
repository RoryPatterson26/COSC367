from search import *
from math import sqrt
from heapq import *

class LocationGraph(ExplicitGraph):
    
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        self.edge_set = set()
        
        for edge in edges:
            location_1 = locations[edge[0]]
            location_2 = locations[edge[1]]
            edge_distance = sqrt((location_1[0]-location_2[0])**2 + (location_1[1]-location_2[1])**2)
            new_edge = (edge[0], edge[1], edge_distance)
            self.edge_set.add(new_edge)
            new_edge = (edge[1], edge[0], edge_distance)
            self.edge_set.add(new_edge)
        
        self.edge_list = list(self.edge_set)
        self.edge_list.sort(key=lambda tup: (tup[0], tup[1]))
             
        
#stuff
class LCFSFrontier(Frontier):
    
    def __init__(self):
        self.container = []
        
    def add(self, path):
        total_cost = sum([x.cost for x in path])
        heappush(self.container, (total_cost, path))


    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            
            return heappop(self.container)[1]
            
        else:
            raise StopIteration   # don't change this one    




#stuff

graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)