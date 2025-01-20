class Graph:
    def __init__(self):
        self.vertex_list = []
        self.adjacency_list = []
        # Will store map of vertex -> index
        self.vertex_mapping = {}
    
    # unoptimized way
    def get_index_of_vertex(self, val):
        for index in range(len(self.vertex_list)):
            vertex = self.vertex_list[index]
            if vertex == val:
                return index
        return -1

    def add_vertex(self, val):
        self.vertex_list.append(val)
        index = self.get_index_of_vertex(val)
        self.vertex_mapping[val] = index
        self.adjacency_list.append([])

    def add_edge(self, start, end, is_directed = False):
        index_start = self.vertex_mapping[start]
        index_end = self.vertex_mapping[end]

        self.adjacency_list[index_start].append(index_end)

        if not is_directed:
            self.adjacency_list[index_end].append(index_start)

    def display(self):
        for index in range(len(self.vertex_list)):
            node = self.vertex_list[index]
            print(f'For node {node}')
            adj_nodes = [self.vertex_list[j] for j in self.adjacency_list[index]]
            print(f'Adjacent nodes are {adj_nodes}')


if __name__ == '__main__':
    graph = Graph()

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