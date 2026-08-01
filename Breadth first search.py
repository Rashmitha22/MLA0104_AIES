from collections import deque


def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])

    traversal = []
    parent = {start: None}
    distance = {start: 0}

    visited.add(start)

    while queue:
        current_vertex = queue.popleft()
        traversal.append(current_vertex)

        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

                parent[neighbour] = current_vertex
                distance[neighbour] = distance[current_vertex] + 1

    return traversal, parent, distance


def find_shortest_path(parent, start, destination):
    if destination not in parent:
        return None

    path = []
    current_vertex = destination

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = parent[current_vertex]

    path.reverse()

    if path[0] != start:
        return None

    return path


def main():
    print("=" * 60)
    print("        BREADTH FIRST SEARCH - BFS")
    print("=" * 60)

    try:
        number_of_vertices = int(input("Enter the number of vertices: "))
        number_of_edges = int(input("Enter the number of edges: "))

        if number_of_vertices <= 0:
            print("Error: Number of vertices must be greater than zero.")
            return

        if number_of_edges < 0:
            print("Error: Number of edges cannot be negative.")
            return

        graph = {}

        print("\nEnter the vertex names:")
        for index in range(number_of_vertices):
            vertex = input(f"Vertex {index + 1}: ").strip()

            if not vertex:
                print("Error: Vertex name cannot be empty.")
                return

            if vertex in graph:
                print("Error: Duplicate vertex entered.")
                return

            graph[vertex] = []

        print("\nEnter the edges in the format: source destination")
        print("Example: A B")

        for index in range(number_of_edges):
            source, destination = input(
                f"Edge {index + 1}: "
            ).split()

            if source not in graph or destination not in graph:
                print(
                    f"Error: Vertex {source} or {destination} "
                    "does not exist."
                )
                return

            # Undirected graph
            graph[source].append(destination)
            graph[destination].append(source)

        # Sort neighbours for consistent output
        for vertex in graph:
            graph[vertex].sort()

        start_vertex = input("\nEnter the starting vertex: ").strip()

        if start_vertex not in graph:
            print("Error: Starting vertex does not exist.")
            return

        traversal, parent, distance = breadth_first_search(
            graph,
            start_vertex
        )

        print("\n" + "=" * 60)
        print("ADJACENCY LIST")
        print("=" * 60)

        for vertex, neighbours in graph.items():
            print(f"{vertex} -> {neighbours}")

        print("\n" + "=" * 60)
        print("BFS TRAVERSAL")
        print("=" * 60)

        print(" -> ".join(traversal))

        print("\n" + "=" * 60)
        print("PARENT OF EACH VERTEX")
        print("=" * 60)

        for vertex in traversal:
            if parent[vertex] is None:
                print(f"Parent of {vertex}: None (Starting vertex)")
            else:
                print(f"Parent of {vertex}: {parent[vertex]}")

        print("\n" + "=" * 60)
        print("DISTANCE FROM STARTING VERTEX")
        print("=" * 60)

        for vertex in graph:
            if vertex in distance:
                print(
                    f"Distance from {start_vertex} to "
                    f"{vertex}: {distance[vertex]}"
                )
            else:
                print(
                    f"Distance from {start_vertex} to "
                    f"{vertex}: Not reachable"
                )

        print("\n" + "=" * 60)
        print("SHORTEST PATHS")
        print("=" * 60)

        for vertex in graph:
            path = find_shortest_path(
                parent,
                start_vertex,
                vertex
            )

            if path is None:
                print(
                    f"Shortest path from {start_vertex} "
                    f"to {vertex}: No path"
                )
            else:
                print(
                    f"Shortest path from {start_vertex} "
                    f"to {vertex}: {' -> '.join(path)}"
                )

        unreachable_vertices = [
            vertex for vertex in graph
            if vertex not in distance
        ]

        print("\n" + "=" * 60)
        print("FINAL RESULT")
        print("=" * 60)

        print(f"Starting vertex : {start_vertex}")
        print(f"Visited vertices: {len(traversal)}")
        print(f"BFS order       : {' -> '.join(traversal)}")

        if unreachable_vertices:
            print(
                "Unreachable vertices: "
                + ", ".join(unreachable_vertices)
            )
        else:
            print("All vertices are reachable.")

    except ValueError:
        print(
            "Error: Enter valid numbers and provide each edge "
            "using exactly two vertex names."
        )

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
