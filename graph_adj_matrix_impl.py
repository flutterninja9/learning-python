from collections import deque

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

    def dfs(self, node):
        visited = [False for _ in range(self.MAX_SIZE)]
        index = self.get_index_of_vertex(node)

        def dfs_helper(index):
            visited[index] = True
            print(self.vertex_list[index], end=" ")
            neighbors = self.adj_list[index]

            for i in range(self.MAX_SIZE):
                is_adjacent = True if neighbors[i] == 1 else False
                is_visited = visited[i]

                if is_adjacent and not is_visited:
                    dfs_helper(i)

        
        dfs_helper(index)
        print('\n')

    def bfs(self, node):
        queue = deque()
        visited = [False for _ in range(self.MAX_SIZE)]
        index = self.get_index_of_vertex(node)
        visited[index] = True
        queue.append(index)

        while len(queue) != 0:
            first_index = queue.popleft()
            print(self.vertex_list[first_index], end=" ")
            neighbor = self.adj_list[first_index]

            for i in range(self.MAX_SIZE):
                is_visited = visited[i]
                is_adjacent = True if neighbor[i] == 1 else False

                if is_adjacent and not is_visited:
                    visited[i] = True
                    queue.append(i)
        
        print('\n')


if __name__ == '__main__':
    graph = Graph(4)

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

    # DFS Traversal
    graph.dfs('A')

    # BFS Traversal
    graph.bfs('A')