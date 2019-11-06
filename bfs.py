class Graph:

    def __init__(self, num):
        self.graph = [[] for i in range(num)]

    def addEdge(self, u, v, cost):
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    def bfs(self, start, end):
        visited = [False for i in self.graph]
        queue = [start, ]
        visited[start] = True
        path = []

        while True:

            if len(queue) != 0:
                curr_node = queue.pop(0)
            else:
                break

            path.append(curr_node)
            if curr_node == end:
                print("Path found from %d to %d (%s)" % (
                    start, end, ' -> '.join(map(str, path))
                ))
                break

            for node, _ in self.graph[curr_node]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)


if __name__ == "__main__":
    graph = Graph(14)
    graph.addEdge(0, 1, 3)
    graph.addEdge(0, 2, 6)
    graph.addEdge(0, 3, 5)
    graph.addEdge(1, 4, 9)
    graph.addEdge(1, 5, 8)
    graph.addEdge(2, 6, 12)
    graph.addEdge(2, 7, 14)
    graph.addEdge(3, 8, 7)
    graph.addEdge(8, 9, 5)
    graph.addEdge(8, 10, 6)
    graph.addEdge(9, 11, 1)
    graph.addEdge(9, 12, 10)
    graph.addEdge(9, 13, 2)

    graph.bfs(0, 9)
