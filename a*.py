from queue import PriorityQueue


class Graph:

    def __init__(self, num, node_values=[]):
        self.nodes = node_values
        self.graph = [[] for i in range(num)]

    def addEdge(self, u, v, cost):
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    def astar(self, start, end_val, heuristic):
        closed_list = [-1] * len(self.nodes)  # Open list: stores f of nodes
        open_list = [-1] * len(self.nodes)  # Closed list
        queue = PriorityQueue()

        open_list[start] = heuristic[start]
        queue.put((heuristic[start], start))

        condition = True

        while condition:
            if not queue.empty():
                node = queue.get()
                c = node[0]
                q = node[1]
            else:
                print("Crashed")
                break

            for node, cost in self.graph[q]:

                g = (c - heuristic[q]) + cost
                h = heuristic[node]
                f = g + h

                # Check if successor is goal state, break if true
                if self.nodes[node] == end_val:
                    print("Path found from %s to %s with cost %d" % (
                        self.nodes[start], self.nodes[node], f
                    ))
                    condition = False
                    break

                if open_list[node] != -1 and open_list[node] < f:
                    continue

                if closed_list[node] != -1 and closed_list[node] < f:
                    continue

                open_list[node] = f
                queue.put((f, node))

            closed_list[q] = c


if __name__ == '__main__':
    g = Graph(7, ['A', 'B', 'C', 'D', 'E', 'F', 'Z'])
    g.addEdge(0, 1, 4)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 5, 5)
    g.addEdge(1, 4, 12)
    g.addEdge(2, 4, 10)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 4, 2)
    g.addEdge(4, 6, 5)
    g.addEdge(5, 6, 16)

    g.astar(0, 'Z', [14, 12, 11, 6, 4, 11, 0])
