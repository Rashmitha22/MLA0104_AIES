import heapq


def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]

    cost = {start: 0}
    parent = {start: None}

    visited = set()
    expansion_order = []

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        expansion_order.append(current_node)

        if current_node == goal:
            path = construct_path(parent, start, goal)

            return expansion_order, cost, parent, path

        for neighbour, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbour)
                )

    return expansion_order, cost, parent, None


def construct_path(parent, start, goal):
    """
    Construct the optimal path from start to goal.
    """

    if goal not in parent:
        return None

    path = []
    current_node = goal

    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]

    path.reverse()

    if path[0] != start:
        return None

    return path


def main():
    print("=" * 60)
    print("            UNIFORM COST SEARCH")
    print("=" * 60)

    try:
        number_of_vertices = int(
            input("Enter the number of vertices: ")
        )

        number_of_edges = int(
            input("Enter the number of edges: ")
        )

        if number_of_vertices <= 0:
            print("Error: Number of vertices must be greater than zero.")
            return

        if number_of_edges < 0:
            print("Error: Number of edges cannot be negative.")
            return

        graph = {}

        print("\nEnter the vertex names:")

        for index in range(number_of_vertices):
            vertex = input(
                f"Vertex {index + 1}: "
            ).strip()

            if not vertex:
                print("Error: Vertex name cannot be empty.")
                return

            if vertex in graph:
                print("Error: Duplicate vertex entered.")
                return

            graph[vertex] = []

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

            if source not in graph or destination not in graph:
                print(
                    "Error: Source or destination vertex does not exist."
                )
                return

            if edge_cost < 0:
                print(
                    "Error: UCS requires non-negative edge costs."
                )
                return

            # Undirected weighted graph
            graph[source].append((destination, edge_cost))
            graph[destination].append((source, edge_cost))

        for vertex in graph:
            graph[vertex].sort(key=lambda item: item[0])

        start = input(
            "\nEnter the starting vertex: "
        ).strip()

        goal = input(
            "Enter the goal vertex: "
        ).strip()

        if start not in graph:
            print("Error: Starting vertex does not exist.")
            return

        if goal not in graph:
            print("Error: Goal vertex does not exist.")
            return

        expansion_order, cost, parent, path = uniform_cost_search(
            graph,
            start,
            goal
        )

        print("\n" + "=" * 60)
        print("WEIGHTED ADJACENCY LIST")
        print("=" * 60)

        for vertex, neighbours in graph.items():
            formatted_neighbours = []

            for neighbour, edge_cost in neighbours:
                formatted_neighbours.append(
                    f"{neighbour}({edge_cost:g})"
                )

            print(
                f"{vertex} -> {', '.join(formatted_neighbours)}"
            )

        print("\n" + "=" * 60)
        print("NODE EXPANSION ORDER")
        print("=" * 60)

        print(" -> ".join(expansion_order))

        print("\n" + "=" * 60)
        print("MINIMUM DISCOVERED COST")
        print("=" * 60)

        for vertex in graph:
            if vertex in cost:
                print(
                    f"Cost from {start} to {vertex}: "
                    f"{cost[vertex]:g}"
                )
            else:
                print(
                    f"Cost from {start} to {vertex}: "
                    "Not discovered"
                )

        print("\n" + "=" * 60)
        print("PARENT OF EACH DISCOVERED NODE")
        print("=" * 60)

        for vertex in cost:
            if parent[vertex] is None:
                print(
                    f"Parent of {vertex}: None "
                    "(Starting node)"
                )
            else:
                print(
                    f"Parent of {vertex}: {parent[vertex]}"
                )

        print("\n" + "=" * 60)
        print("OPTIMAL PATH")
        print("=" * 60)

        if path is None:
            print(
                f"No path exists from {start} to {goal}."
            )
        else:
            print(
                f"Optimal path: {' -> '.join(path)}"
            )

            print(
                f"Minimum total cost: {cost[goal]:g}"
            )

        print("\n" + "=" * 60)
        print("FINAL RESULT")
        print("=" * 60)

        print(f"Starting node     : {start}")
        print(f"Goal node         : {goal}")
        print(
            f"Expanded nodes    : {len(expansion_order)}"
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
                f"Optimal path cost : {cost[goal]:g}"
            )
        else:
            print("Result            : Goal not reachable")

    except ValueError:
        print(
            "Error: Enter valid numbers for vertices, "
            "edges and costs."
        )

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
