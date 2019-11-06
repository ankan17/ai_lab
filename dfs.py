class Graph:

    def __init__(self, num):
        self.graph = [[] for i in range(num)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, end):
        visited = [False for i in self.graph]
        stack = [start, ]
        visited[start] = True
        path = []

        while True:

            if len(stack) != 0:
                curr_node = stack.pop(-1)
            else:
                break

            path.append(curr_node)
            if curr_node == end:
                print("Path found from %d to %d (%s)" % (
                    start, end, ' -> '.join(map(str, path))
                ))
                break

            for node in self.graph[curr_node]:
                if not visited[node]:
                    visited[node] = True
                    stack.append(node)


if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 2)
    graph.addEdge(3, 4)

    graph.dfs(0, 2)
