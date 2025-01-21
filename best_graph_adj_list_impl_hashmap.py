from collections import deque

class Graph:
    def __init__(self):
        # Will store map of vertex -> connected vertices
        self.vertex_mapping = {}

    def add_vertex(self, val):
        self.vertex_mapping[val] = []

    def add_edge(self, start, end, is_directed = False):
        self.vertex_mapping[start].append(end)

        if not is_directed:
            self.vertex_mapping[end].append(start)

    def display(self):
        for vertex, connected_vertices in self.vertex_mapping.items():
            print(f'For node {vertex}')
            adj_nodes = [j for j in connected_vertices]
            print(f'Adjacent nodes are {adj_nodes}')

    def get_index(self, node):
        keys = list(self.vertex_mapping.keys())
        return keys.index(node)

    def dfs(self, node):
        visited = [False for _ in range(len(self.vertex_mapping.items()))]

        def dfs_helper(local_node):
            index = self.get_index(local_node)
            vertices = self.vertex_mapping[local_node]
            # Process the node
            print(local_node, end=" ")
            visited[index] = True
            for vertex in vertices:
                vertex_index = self.get_index(vertex)
                if not visited[vertex_index]:
                    dfs_helper(vertex)
        
        dfs_helper(node)
        print('\n')
        
    def bfs(self, node):
        visited = [False for _ in range(len(self.vertex_mapping.keys()))]
        queue = deque()
        
        index = self.get_index(node)
        visited[index] = True
        queue.append(node)
        
        while len(queue) != 0:
            node = queue.popleft()
            print(node, end=" ")
            neighbors = self.vertex_mapping[node]
            for vertex in neighbors:
                vertex_index = self.get_index(vertex)
                if not visited[vertex_index]:
                    visited[vertex_index] = True
                    queue.append(vertex)

        print('\n')

if __name__ == '__main__':
    graph = Graph()

    # Adding vertices
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')

    # Adding edges
    graph.add_edge('A', 'B', is_directed=True)
    graph.add_edge('A', 'C', is_directed=True)
    graph.add_edge('B', 'D', is_directed=True)

    # Display all
    # graph.display()

    # DFS traversal
    graph.dfs('A')

    # DFS traversal
    graph.bfs('A')