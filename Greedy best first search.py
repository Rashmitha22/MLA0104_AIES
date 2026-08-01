import heapq


def construct_path(parent, start, goal):
    """
    Construct the path from start node to goal node.
    """

    if goal not in parent:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    if path[0] != start:
        return None

    return path


def calculate_path_cost(graph, path):
    """
    Calculate the total edge cost of the returned path.
    """

    if path is None:
        return None

    total_cost = 0

    for index in range(len(path) - 1):
        current = path[index]
        next_node = path[index + 1]

        for neighbour, edge_cost in graph[current]:
            if neighbour == next_node:
                total_cost += edge_cost
                break

    return total_cost


def greedy_best_first_search(graph, heuristic, start, goal):
    """
    Perform Greedy Best-First Search.

    The node with the smallest heuristic value is expanded first.
    """

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic[start], start)
    )

    parent = {start: None}
    visited = set()

    expansion_order = []
    discovered_nodes = [start]

    while priority_queue:
        current_h, current_node = heapq.heappop(
            priority_queue
        )

        if current_node in visited:
            continue

        visited.add(current_node)
        expansion_order.append(current_node)

        if current_node == goal:
            path = construct_path(
                parent,
                start,
                goal
            )

            return (
                path,
                expansion_order,
                parent,
                discovered_nodes
            )

        for neighbour, edge_cost in graph[current_node]:
            if neighbour not in visited:

                if neighbour not in parent:
                    parent[neighbour] = current_node
                    discovered_nodes.append(neighbour)

                heapq.heappush(
                    priority_queue,
                    (
                        heuristic[neighbour],
                        neighbour
                    )
                )

    return (
        None,
        expansion_order,
        parent,
        discovered_nodes
    )


def main():
    print("=" * 70)
    print("             GREEDY BEST-FIRST SEARCH")
    print("=" * 70)

    try:
        number_of_vertices = int(
            input("Enter the number of vertices: ")
        )

        number_of_edges = int(
            input("Enter the number of edges: ")
        )

        if number_of_vertices <= 0:
            print(
                "Error: Number of vertices must be greater than zero."
            )
            return

        if number_of_edges < 0:
            print(
                "Error: Number of edges cannot be negative."
            )
            return

        graph = {}
        heuristic = {}

        print("\nEnter the vertex names:")

        for index in range(number_of_vertices):
            vertex = input(
                f"Vertex {index + 1}: "
            ).strip()

            if not vertex:
                print(
                    "Error: Vertex name cannot be empty."
                )
                return

            if vertex in graph:
                print(
                    "Error: Duplicate vertex entered."
                )
                return

            graph[vertex] = []

        print("\nEnter heuristic values:")

        for vertex in graph:
            heuristic_value = float(
                input(
                    f"Heuristic value h({vertex}): "
                )
            )

            if heuristic_value < 0:
                print(
                    "Error: Heuristic value cannot be negative."
                )
                return

            heuristic[vertex] = heuristic_value

        print("\nEnter weighted edges in the format:")
        print("Source Destination Cost")
        print("Example: A B 4")

        for index in range(number_of_edges):
            edge_data = input(
                f"Edge {index + 1}: "
            ).split()

            if len(edge_data) != 3:
                print(
                    "Error: Enter source, destination and cost."
                )
                return

            source = edge_data[0]
            destination = edge_data[1]

            edge_cost = float(edge_data[2])

            if (
                source not in graph
                or destination not in graph
            ):
                print(
                    "Error: Source or destination vertex does not exist."
                )
                return

            if edge_cost < 0:
                print(
                    "Error: Edge cost cannot be negative."
                )
                return

            # Undirected graph
            graph[source].append(
                (destination, edge_cost)
            )

            graph[destination].append(
                (source, edge_cost)
            )

        for vertex in graph:
            graph[vertex].sort(
                key=lambda item: item[0]
            )

        start = input(
            "\nEnter the starting vertex: "
        ).strip()

        goal = input(
            "Enter the goal vertex: "
        ).strip()

        if start not in graph:
            print(
                "Error: Starting vertex does not exist."
            )
            return

        if goal not in graph:
            print(
                "Error: Goal vertex does not exist."
            )
            return

        path, expansion_order, parent, discovered_nodes = (
            greedy_best_first_search(
                graph,
                heuristic,
                start,
                goal
            )
        )

        print("\n" + "=" * 70)
        print("WEIGHTED ADJACENCY LIST")
        print("=" * 70)

        for vertex, neighbours in graph.items():
            formatted_neighbours = []

            for neighbour, edge_cost in neighbours:
                formatted_neighbours.append(
                    f"{neighbour}({edge_cost:g})"
                )

            print(
                f"{vertex} -> "
                f"{', '.join(formatted_neighbours)}"
            )

        print("\n" + "=" * 70)
        print("HEURISTIC VALUES")
        print("=" * 70)

        for vertex in heuristic:
            print(
                f"h({vertex}) = {heuristic[vertex]:g}"
            )

        print("\n" + "=" * 70)
        print("NODE EXPANSION ORDER")
        print("=" * 70)

        print(
            " -> ".join(expansion_order)
        )

        print("\n" + "=" * 70)
        print("DISCOVERED NODES")
        print("=" * 70)

        print(
            " -> ".join(discovered_nodes)
        )

        print("\n" + "=" * 70)
        print("PARENT OF EACH DISCOVERED NODE")
        print("=" * 70)

        for vertex in parent:
            if parent[vertex] is None:
                print(
                    f"Parent of {vertex}: None "
                    "(Starting node)"
                )
            else:
                print(
                    f"Parent of {vertex}: "
                    f"{parent[vertex]}"
                )

        print("\n" + "=" * 70)
        print("SEARCH PATH")
        print("=" * 70)

        if path is None:
            print(
                f"No path exists from {start} to {goal}."
            )

        else:
            path_cost = calculate_path_cost(
                graph,
                path
            )

            print(
                "Path found: "
                + " -> ".join(path)
            )

            print(
                f"Path cost: {path_cost:g}"
            )

        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            f"Starting node    : {start}"
        )

        print(
            f"Goal node        : {goal}"
        )

        print(
            f"Expanded nodes   : "
            f"{len(expansion_order)}"
        )

        print(
            "Expansion order  : "
            + " -> ".join(expansion_order)
        )

        if path:
            print(
                "Path found       : "
                + " -> ".join(path)
            )

            print(
                f"Total path cost  : "
                f"{calculate_path_cost(graph, path):g}"
            )

            print(
                "Result           : Goal reached"
            )

            print(
                "Optimality       : Not guaranteed"
            )

        else:
            print(
                "Result           : Goal not reachable"
            )

    except ValueError:
        print(
            "Error: Enter valid numeric values."
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )


if __name__ == "__main__":
    main()
