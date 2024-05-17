import random
from Graph import Graph

random.seed(10)

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
        self.visited = set()
    
    def random_walk(self, start_cell):
        path = []
        current_cell = start_cell
        walk_path = []

        while current_cell not in self.visited:
            walk_path.append(current_cell)
            neighbors = self.graph.get_neighbors(*current_cell)
            next_cell = random.choice(neighbors)
            path.append((current_cell, next_cell))
            current_cell = next_cell

            # If a loop is detected within the walk, remove the loop
            if current_cell in walk_path:
                loop_start = walk_path.index(current_cell)
                walk_path = walk_path[:loop_start + 1]
            
        # Add the path to the maze and mark cells as visited
        for edge in path:
            self.maze.add(edge)
            self.visited.add(edge[0])
            self.visited.add(edge[1])

        return path
    def generate_maze(self):
        #Step 1: Choose a random cell and add it to the set of visited cells
        random_cell = random.choice(list(self.graph.adjacency_list.keys())) #here you get the random cell
        #keep on selecting random vertices until all are part of the maze
        #I need to figure out a way to see if a vertex is in the graph by traversing the edges of the graph
        self.visited.add(random_cell)

        #Step 2: Select a different random cell that is NOT in the visited cells set
        while len(self.visited) < len(self.graph.adjacency_list):
            # Step 2: Select a random cell that is not in the visited set
            current_cell = random.choice(list(self.graph.adjacency_list.keys()))
            while current_cell in self.visited:
                current_cell = random.choice(list(self.graph.adjacency_list.keys()))

            # Perform the random walk from the selected cell
            self.random_walk(current_cell)

        return self.maze
    

    def display_maze(self):
        rows = self.graph.rows
        columns = self.graph.columns
        maze_grid = [[' ' for _ in range(2 * columns - 1)] for _ in range(2 * rows - 1)]

        # Place the vertices
        for y in range(columns):
            for x in range(rows):
                maze_grid[2 * x][2 * y] = '.'

        # Place the edges
        for (x1, y1), (x2, y2) in self.maze:
            if x1 == x2:  # horizontal edge
                maze_grid[2 * x1][min(2 * y1, 2 * y2) + 1] = '-'
            elif y1 == y2:  # vertical edge
                maze_grid[min(2 * x1, 2 * x2) + 1][2 * y1] = '|'

        # Convert the maze grid to a string
        maze_str = '\n'.join([''.join(row) for row in maze_grid])
        return maze_str
    
# Test
rows = 7
columns = 7
graph = Graph(rows, columns)
maze_gen = Maze(graph)
maze = maze_gen.generate_maze()

print("Generated Maze:")
for edge in maze:
    print(edge)

print("\nMaze Visualization:")
print(maze_gen.display_maze())

# ._._.
# |   |
# . ._.
# | ._.
#     |
# ._. .

