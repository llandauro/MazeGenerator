import random
from Graph import Graph

class Maze:

    
    # first step is to generate a graph similar to a chess board:
    # We have cell
    # start of the algorithm:
    # initialize the maze with one cell chosen arbitrarily (say cell at coord (0,0)) and 
    # add it to the UST (Uniform Spanning Tree)
    # random walk until you reach a cell already in the maze

    
    def __init__(self, graph):
        self.graph = graph
        self.maze = set() #maze is a set of edges since we are looking for a subgraph of graphs
        self.visited = []

    def cell_in_maze(self, cell):
        result = False
        #iterate through the maze
        for edge in self.maze:
            if edge[0] == cell or edge[1] == cell:
                result = True
                break
        return result
    
    def random_walk(self, start_cell):
        path = []
        current_cell = start_cell
        while current_cell not in self.visited:
            self.visited.append(current_cell)
            neighbors = self.graph.adjacency_list()[current_cell]
            next_cell = random.choice(neighbors)
            path.append((current_cell, next_cell))
            current_cell = next_cell
        return path

    def generate_maze(self):
        #Step 1: Choose a random cell and add it to the set of visited cells
        random_cell = random.choice(self.graph.cells) #here you get the random cell
        #keep on selecting random vertices until all are part of the maze
        #I need to figure out a way to see if a vertex is in the graph by traversing the edges of the graph
        self.visited.append(random_cell)

        #Step 2: Select a different random cell that is NOT in the visited cells set
        current_cell = random.choice(self.graph.cells)
        while current_cell in self.visited:
            current_cell = random.choice(self.graph.cells)

        while len(self.visited) < len(self.graph.cells):
            path = self.random_walk(current_cell)
            self.maze.update(path)

            # Step 3: Select a random cell that has already been visited
            current_cell = random.choice(list(self.visited))

        return self.maze
    
# Test
width = 3
length = 3
graph = Graph(width, length)
maze_gen = Maze(graph)
maze = maze_gen.generate_maze()

print("Generated Maze:")
for edge in maze:
    print(edge)

    
            




        




