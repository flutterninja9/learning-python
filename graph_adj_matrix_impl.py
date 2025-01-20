class Graph:
    def __init__(self, size):
        self.vertex_list = []
        self.MAX_SIZE = size
        self.adj_list = [[0 for _ in range(size)] for _ in range(size)]

    # unoptimized way
    def get_index_of_vertex(self, val):
        for index in range(len(self.vertex_list)):
            vertex = self.vertex_list[index]
            if vertex == val:
                return index
        return -1

    def add_vertex(self, val):
        if len(self.vertex_list) == self.MAX_SIZE:
            return # no space left to accomodate new vertex

        self.vertex_list.append(val)

    def add_edge(self, start, end, is_directed = False):
        start_index = self.get_index_of_vertex(start)
        end_index = self.get_index_of_vertex(end)

        self.adj_list[start_index][end_index] = 1

        if not is_directed:
            self.adj_list[end_index][start_index] = 1


    def display(self):
        for row in self.adj_list:
            print(row)

if __name__ == '__main__':
    graph = Graph(4)

    # Adding vertices
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')

    # Adding edges
    graph.add_edge('A', 'B', is_directed=True)
    graph.add_edge('B', 'D', is_directed=True)
    graph.add_edge('D', 'C', is_directed=True)
    graph.add_edge('C', 'A', is_directed=True)
    graph.add_edge('A', 'D', is_directed=True)
    graph.add_edge('B', 'C', is_directed=True)

    # Display all
    graph.display()