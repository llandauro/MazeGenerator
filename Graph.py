class Graph:
    class Edge:
        def __init__(self, first_cell, second_cell):
            self.nodes = [first_cell, second_cell]  # nodes connected by this edge

    class Cell:
        def __init__(self, coordinates):
            self.coordinates = coordinates

    def __init__(self, width, length):
        self.cells = []
        self.edges = []
        self.width = width
        self.length = length
        for x_coord in range(width):
            for y_coord in range(length):
                cell_coordinates = [x_coord, y_coord]
                self.cells.append(self.Cell(cell_coordinates))
                # add edges for each cell if they are not on the rightmost or bottommost edge
                if x_coord < width - 1:
                    self.edges.append(self.Edge(self.get_cell_index(x_coord, y_coord),
                                                 self.get_cell_index(x_coord + 1, y_coord)))
                if y_coord < length - 1:
                    self.edges.append(self.Edge(self.get_cell_index(x_coord, y_coord),
                                                 self.get_cell_index(x_coord, y_coord + 1)))

    def get_cell_index(self, x_coord, y_coord): #maybe no need for width? 
        return y_coord * self.width + x_coord
    
    def get_cell(self, x_coord, y_coord):
        return self.cells[x_coord][y_coord]
    
    def adjacency_list(self):
        adjacency = {}
        for cell_index, cell in enumerate(self.cells):
            adjacency[cell_index] = []
            for edge in self.edges:
                if cell_index in edge.nodes:
                    neighbor = edge.nodes[0] if edge.nodes[1] == cell_index else edge.nodes[1]
                    adjacency[cell_index].append(neighbor)
        return adjacency
    
    #supposed to enumerate the cells and return the adjacency list related to the cells, and if asked about the current cells,
    #gives the according neighbors


# # Test
# width = 2
# length = 2
# graph = Graph(width, length)
# adjacency = graph.adjacency_list()
# for cell_index, neighbors in adjacency.items():
#     print(f"Cell {cell_index} has neighbors: {neighbors}")

