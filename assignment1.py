from search import *
import math
import heapq

class RoutingGraph(Graph):
    
    def __init__(self, map_str):
        self.map_str = map_str
        self.obstacles = []
        self.fuel_stations = []
        self.goals = []
        self.agents = []
        rows = self.map_str.strip().splitlines()
        for i, row in enumerate(rows):
            row = row.strip()
            for j, column, in enumerate(row):
                column = column.strip()
                if column == 'X' or column == '-' or column == '|' or column == '+':
                    self.obstacles.append((i, j))
                elif column == 'F':
                    self.fuel_stations.append((i, j))
                elif column == 'G':
                    self.goals.append((i, j))
                elif column in ['0','1','2','3','4','5','6','7','8','9']:
                    self.agents.append((i, j, int(column)))
                elif column == 'S':
                    self.agents.append((i, j, math.inf))
        
    def starting_nodes(self):
        return self.agents
    
    def outgoing_arcs(self, tail_node):
        arcs = []
        moves = [('N' , -1, 0),
                 ('E' ,  0, 1),
                 ('S' ,  1, 0),
                 ('W' ,  0, -1),
                 ('Fuel up', 0, 0)]
        row, column, fuel = tail_node
        for move in moves:
            direction, row_move, column_move = move
            new_row = row + row_move
            new_column = column + column_move
            
            
            if direction == 'Fuel up' and (new_row, new_column) in self.fuel_stations and fuel < 9:
                head_node = (new_row, new_column, 9)
                arc = Arc(tail_node, head_node, action=direction, cost=15)
                arcs.append(arc)
            elif (new_row, new_column) not in self.obstacles:
                if fuel > 0 and direction != 'Fuel up':
                    head_node = (new_row, new_column, fuel-1)
                    arc = Arc(tail_node, head_node, action=direction, cost=5)
                    arcs.append(arc)
            
        return arcs 
    
    def is_goal(self, node):
        row, column, fuel = node
        for goal in self.goals:
            i, j = goal
            if row == i and column == j:
                return True
        return False
    def estimated_cost_to_goal(self, path):
        node = path[-1]
        possible_heuristics = set()
        row, column, fuel = node.head
        for goal in self.goals:
            i, j = goal
            heuristic = math.ceil(math.sqrt((row-i)**2 + (column-j)**2) + len(path))
            possible_heuristics.add(heuristic)
        return min(possible_heuristics)*2
            
class AStarFrontier(Frontier):
    
    def __init__(self, map_graph):
        self.container = []
        self.map_graph = map_graph
        self.entry_count = 0
        self.expanded = set()
    
    def add(self, path):
        heapq.heappush(self.container, (self.map_graph.estimated_cost_to_goal(path), self.entry_count, path))
        #heapq.heappush(self.container, (sum(arc.cost for arc in path), self.entry_count, path))
        self.entry_count += 1
        
    def __iter__(self):
        return self
    
    def __next__(self):

        while True:        
            if len(self.container) > 0:
                cost, entry_count, path = heapq.heappop(self.container)
                if path[-1].head not in self.expanded:
                    self.expanded.add(path[-1].head)
                    return path
            
            else:
                raise StopIteration        
    

def print_map(map_graph, frontier, solution):
    final_map = []
    obstacles = map_graph.obstacles
    expanded = frontier.expanded
    goals = map_graph.goals
    path = set()
    for i in solution:
        row, column, fuel = i.head
        path.add((row, column))
    rows = map_graph.map_str.strip().splitlines()
    for row in rows:
        final_map.append(list(row.strip()))
    
    for item in expanded:
        row, column, fuel = item
        if final_map[row][column] == ' ':
            final_map[row][column] = '.'        
    for item in path:
        row, column = item
        if final_map[row][column] == ' ' or final_map[row][column] == '.':
            final_map[row][column] = '*'
            
    for row in final_map:
        print(''.join(row))
def main():
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """
    
    
    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0
    
    frontier = AStarFrontier(map_graph)
    
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)     
        
    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
if __name__ == "__main__":
    main()