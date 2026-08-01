import heapq


def construct_path(parent, start, goal):
    """
    Construct the path from start to goal.
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


def a_star_search(graph, heuristic, start, goal):
    """
    Perform A* Search on a weighted graph.

    Returns:
        path              : Optimal path from start to goal
        expansion_order   : Order in which nodes were expanded
        g_cost            : Actual cost from start
        f_cost            : Estimated total cost
        parent            : Parent of each discovered node
    """

    open_queue = []

    g_cost = {start: 0}
    f_cost = {start: heuristic[start]}
    parent = {start: None}

    heapq.heappush(
        open_queue,
        (f_cost[start], g_cost[start], start)
    )

    closed_set = set()
    expansion_order = []

    while open_queue:
        current_f, current_g, current_node = heapq.heappop(
            open_queue
        )

        if current_node in closed_set:
            continue

        closed_set.add(current_node)
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
                g_cost,
                f_cost,
                parent
            )

        for neighbour, edge_cost in graph[current_node]:
            new_g_cost = current_g + edge_cost

            if (
                neighbour not in g_cost
                or new_g_cost < g_cost[neighbour]
            ):
                g_cost[neighbour] = new_g_cost

                f_cost[neighbour] = (
                    new_g_cost + heuristic[neighbour]
                )

                parent[neighbour] = current_node

                heapq.heappush(
                    open_queue,
                    (
                        f_cost[neighbour],
                        g_cost[neighbour],
                        neighbour
                    )
                )

    return (
        None,
        expansion_order,
        g_cost,
        f_cost,
        parent
    )


def main():
    print("=" * 65)
    print("                A* SEARCH ALGORITHM")
    print("=" * 65)

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
                    "Error: Heuristic values cannot be negative."
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
                    "Error: A* requires non-negative edge costs."
                )
                return

            # Undirected weighted graph
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

        path, expansion_order, g_cost, f_cost, parent = (
            a_star_search(
                graph,
                heuristic,
                start,
                goal
            )
        )

        print("\n" + "=" * 65)
        print("WEIGHTED ADJACENCY LIST")
        print("=" * 65)

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

        print("\n" + "=" * 65)
        print("HEURISTIC VALUES")
        print("=" * 65)

        for vertex in heuristic:
            print(
                f"h({vertex}) = {heuristic[vertex]:g}"
            )

        print("\n" + "=" * 65)
        print("NODE EXPANSION ORDER")
        print("=" * 65)

        print(
            " -> ".join(expansion_order)
        )

        print("\n" + "=" * 65)
        print("COST DETAILS")
        print("=" * 65)

        print(
            f"{'Node':<10}"
            f"{'g(n)':<12}"
            f"{'h(n)':<12}"
            f"{'f(n)=g+h':<15}"
        )

        print("-" * 49)

        for vertex in g_cost:
            print(
                f"{vertex:<10}"
                f"{g_cost[vertex]:<12g}"
                f"{heuristic[vertex]:<12g}"
                f"{f_cost[vertex]:<15g}"
            )

        print("\n" + "=" * 65)
        print("PARENT OF EACH DISCOVERED NODE")
        print("=" * 65)

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

        print("\n" + "=" * 65)
        print("OPTIMAL PATH")
        print("=" * 65)

        if path is None:
            print(
                f"No path exists from {start} to {goal}."
            )

        else:
            print(
                "Optimal path: "
                + " -> ".join(path)
            )

            print(
                f"Minimum total cost: "
                f"{g_cost[goal]:g}"
            )

        print("\n" + "=" * 65)
        print("FINAL RESULT")
        print("=" * 65)

        print(
            f"Starting node     : {start}"
        )

        print(
            f"Goal node         : {goal}"
        )

        print(
            f"Expanded nodes    : "
            f"{len(expansion_order)}"
        )

        print(
            "Expansion order   : "
            + " -> ".join(expansion_order)
        )

        if path:
            print(
                "Optimal path      : "
                + " -> ".join(path)
            )

            print(
                f"Optimal path cost : "
                f"{g_cost[goal]:g}"
            )

            print(
                "Result            : Goal reached"
            )

        else:
            print(
                "Result            : Goal not reachable"
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
