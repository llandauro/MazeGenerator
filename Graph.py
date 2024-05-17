class Graph:
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.adjacency_list = {}
        
        for x_coord in range(self.rows):
            for y_coord in range(self.columns):
                cell_coordinates = (x_coord, y_coord)
                self.adjacency_list[cell_coordinates] = []

                # Directions: right, down, left, up
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                
                for dx, dy in directions:
                    neighbor_x, neighbor_y = x_coord + dx, y_coord + dy
                    if 0 <= neighbor_x < rows and 0 <= neighbor_y < columns:
                        self.adjacency_list[cell_coordinates].append((neighbor_x, neighbor_y))



    def get_neighbors(self, x_coord, y_coord):
        return self.adjacency_list[(x_coord, y_coord)]

# # Test
# rows = 3
# columns = 2
# graph = Graph(rows, columns)
# for cell_coordinates, neighbors in graph.adjacency_list.items():
#     print(f"Cell {cell_coordinates} has neighbors: {neighbors}")
