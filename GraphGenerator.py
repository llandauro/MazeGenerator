class GraphGenerator:
    class Edge:
        def __init__(self, first_cell, second_cell):
            self.nodes = [first_cell, second_cell]  # nodes connected by this edge

    class Cell:
        def __init__(self, coordinates):
            self.coordinates = coordinates

    def __init__(self, width, length):
        self.cells = []
        self.edges = []
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

    def get_cell_index(self, x_coord, y_coord):
        return y_coord * width + x_coord

# test:
# width = 5
# length = 5
# graph = GraphGenerator(width, length)


