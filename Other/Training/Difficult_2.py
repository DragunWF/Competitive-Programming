import sys

STARTER_NODE = "A"
DESTINATION_NODE = "E"

class WeightedDirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.add_node(source)
        if destination not in self.graph:
            self.add_node(destination)
        self.graph[source].append((destination, weight))

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def print_graph(self):
        for node, edges in self.graph.items():
            print(f"Node {node}:")
            for dest, weight in edges:
                print(f"  -> {dest} (Weight: {weight})")


def solve() -> None:
    sys.stdout.write(f"Djikstra's Algorithm ({STARTER_NODE} -> {DESTINATION_NODE})\n")
    graph = create_graph()

    paths = {}
    current_path = [STARTER_NODE]

    def traverse(node: str, path_cost: int):
        """
        Traverses via recursion
        :return:
        """
        current_path.append(node)
        neighbors = graph.get_neighbors(node)
        if node == DESTINATION_NODE:
            paths[path_cost] = current_path.copy()
            current_path.clear()
            current_path.append(STARTER_NODE)
            return
        elif not neighbors:  # Recursion base case
            current_path.clear()
            current_path.append(STARTER_NODE)
            return
        for node in neighbors:
            traverse(node[0], node[1] + path_cost)

    traverse(STARTER_NODE, 0)
    print_shortest_path(paths)


def print_shortest_path(paths: list[dict: [int, str]]) -> None:
    if not paths:
        sys.stdout.write(f"INF (No path found)\n")
        return
    shortest_travel_time = min(paths.keys())
    # Remove duplicated starter node the shortest path output
    if paths[shortest_travel_time].count(STARTER_NODE) == 2:
        paths[shortest_travel_time].pop(paths[shortest_travel_time].index(STARTER_NODE))
    sys.stdout.write(f"Shortest Path: {' -> '.join(paths[shortest_travel_time])}\n")
    sys.stdout.write(f"Cost: {shortest_travel_time}")


def create_graph() -> WeightedDirectedGraph:
    graph = WeightedDirectedGraph()
    graph.add_edge("A", "B", 10)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "D", 7)
    graph.add_edge("C", "D", 3)
    graph.add_edge("D", "E", 2)
    graph.add_node("E")  # Add a node with no outgoing edges
    return graph


if __name__ == "__main__":
    solve()
