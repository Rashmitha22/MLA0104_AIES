def is_safe(vertex, color, graph, color_assignment):
    for adjacent_vertex in graph[vertex]:
        if color_assignment.get(adjacent_vertex) == color:
            return False

    return True


def map_coloring(
    vertices,
    graph,
    colors,
    vertex_index,
    color_assignment,
    trace
):
    """
    Solve the Map Coloring Problem using backtracking.
    """

    # All vertices have been colored
    if vertex_index == len(vertices):
        return True

    current_vertex = vertices[vertex_index]

    for color in colors:
        trace.append(
            f"Trying color {color} for vertex {current_vertex}"
        )

        if is_safe(
            current_vertex,
            color,
            graph,
            color_assignment
        ):
            color_assignment[current_vertex] = color

            trace.append(
                f"Assigned {color} to vertex {current_vertex}"
            )

            if map_coloring(
                vertices,
                graph,
                colors,
                vertex_index + 1,
                color_assignment,
                trace
            ):
                return True

            trace.append(
                f"Backtracking from vertex {current_vertex}, "
                f"removing color {color}"
            )

            del color_assignment[current_vertex]

        else:
            trace.append(
                f"Color {color} is not safe for "
                f"vertex {current_vertex}"
            )

    return False


def validate_coloring(graph, color_assignment):
    """
    Validate that adjacent vertices have different colors.
    """

    for vertex in graph:
        for adjacent_vertex in graph[vertex]:
            if (
                vertex in color_assignment
                and adjacent_vertex in color_assignment
                and color_assignment[vertex]
                == color_assignment[adjacent_vertex]
            ):
                return False

    return True


def main():
    print("=" * 70)
    print("                MAP COLORING PROBLEM")
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

        vertices = []
        graph = {}

        print("\nEnter vertex names:")

        for index in range(number_of_vertices):
            vertex = input(
                f"Vertex {index + 1}: "
            ).strip().upper()

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

            vertices.append(vertex)
            graph[vertex] = []

        print("\nEnter edges in the format:")
        print("Source Destination")
        print("Example: A B")

        for index in range(number_of_edges):
            edge_data = input(
                f"Edge {index + 1}: "
            ).strip().upper().split()

            if len(edge_data) != 2:
                print(
                    "Error: Enter exactly two vertex names."
                )
                return

            source, destination = edge_data

            if source not in graph or destination not in graph:
                print(
                    "Error: Source or destination vertex does not exist."
                )
                return

            if source == destination:
                print(
                    "Error: A vertex cannot be connected to itself."
                )
                return

            if destination not in graph[source]:
                graph[source].append(destination)

            if source not in graph[destination]:
                graph[destination].append(source)

        number_of_colors = int(
            input("\nEnter the number of colors: ")
        )

        if number_of_colors <= 0:
            print(
                "Error: Number of colors must be greater than zero."
            )
            return

        colors = []

        print("\nEnter color names:")

        for index in range(number_of_colors):
            color = input(
                f"Color {index + 1}: "
            ).strip().title()

            if not color:
                print(
                    "Error: Color name cannot be empty."
                )
                return

            if color in colors:
                print(
                    "Error: Duplicate color entered."
                )
                return

            colors.append(color)

        color_assignment = {}
        trace = []

        solution_found = map_coloring(
            vertices,
            graph,
            colors,
            0,
            color_assignment,
            trace
        )

        print("\n" + "=" * 70)
        print("ADJACENCY LIST")
        print("=" * 70)

        for vertex in vertices:
            neighbours = ", ".join(
                sorted(graph[vertex])
            )

            print(
                f"{vertex} -> {neighbours}"
            )

        print("\n" + "=" * 70)
        print("AVAILABLE COLORS")
        print("=" * 70)

        print(", ".join(colors))

        print("\n" + "=" * 70)
        print("SEARCH TRACE")
        print("=" * 70)

        for step_number, message in enumerate(
            trace,
            start=1
        ):
            print(
                f"Step {step_number}: {message}"
            )

        print("\n" + "=" * 70)
        print("COLOR ASSIGNMENT")
        print("=" * 70)

        if solution_found:
            for vertex in vertices:
                print(
                    f"Vertex {vertex}: "
                    f"{color_assignment[vertex]}"
                )
        else:
            print(
                "No valid coloring is possible "
                "with the given number of colors."
            )

        print("\n" + "=" * 70)
        print("EDGE VALIDATION")
        print("=" * 70)

        if solution_found:
            for vertex in vertices:
                for adjacent_vertex in graph[vertex]:
                    if vertex < adjacent_vertex:
                        first_color = color_assignment[vertex]
                        second_color = color_assignment[
                            adjacent_vertex
                        ]

                        status = (
                            "Pass"
                            if first_color != second_color
                            else "Fail"
                        )

                        print(
                            f"{vertex}({first_color}) - "
                            f"{adjacent_vertex}({second_color}) "
                            f": {status}"
                        )

        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            f"Number of vertices : {number_of_vertices}"
        )

        print(
            f"Number of edges    : {number_of_edges}"
        )

        print(
            f"Available colors   : {number_of_colors}"
        )

        if solution_found:
            validation = validate_coloring(
                graph,
                color_assignment
            )

            print(
                "Result             : Valid coloring found"
            )

            print(
                "Validation         : "
                + ("Pass" if validation else "Fail")
            )
        else:
            print(
                "Result             : No valid coloring found"
            )

    except ValueError:
        print(
            "Error: Please enter valid integer values."
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )


if __name__ == "__main__":
    main()
