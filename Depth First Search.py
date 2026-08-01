def dfs(graph, vertex, visited, traversal, parent, depth, current_depth):
    visited.add(vertex)
    traversal.append(vertex)
    depth[vertex] = current_depth

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            parent[neighbour] = vertex
            dfs(graph, neighbour, visited, traversal,
                parent, depth, current_depth + 1)


def get_path(parent, start, destination):
    if destination == start:
        return [start]

    if destination not in parent:
        return None

    path = []

    while destination is not None:
        path.append(destination)
        destination = parent.get(destination)

    path.reverse()
    return path


def main():

    print("=" * 60)
    print("        DEPTH FIRST SEARCH (DFS)")
    print("=" * 60)

    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    graph = {}

    print("\nEnter vertex names")

    for i in range(vertices):
        vertex = input(f"Vertex {i+1}: ")
        graph[vertex] = []

    print("\nEnter edges (Source Destination)")

    for i in range(edges):
        source, destination = input(
            f"Edge {i+1}: ").split()

        graph[source].append(destination)
        graph[destination].append(source)

    for vertex in graph:
        graph[vertex].sort()

    start = input("\nEnter starting vertex: ")

    visited = set()
    traversal = []
    parent = {start: None}
    depth = {}

    dfs(graph, start, visited, traversal,
        parent, depth, 0)

    print("\n" + "=" * 60)
    print("ADJACENCY LIST")
    print("=" * 60)

    for vertex in graph:
        print(vertex, "->", graph[vertex])

    print("\n" + "=" * 60)
    print("DFS TRAVERSAL")
    print("=" * 60)

    print(" -> ".join(traversal))

    print("\n" + "=" * 60)
    print("PARENT OF EACH VERTEX")
    print("=" * 60)

    for vertex in traversal:

        if parent[vertex] is None:
            print(vertex, " : None (Root)")
        else:
            print(vertex, ":", parent[vertex])

    print("\n" + "=" * 60)
    print("DEPTH OF EACH VERTEX")
    print("=" * 60)

    for vertex in traversal:
        print(vertex, ":", depth[vertex])

    print("\n" + "=" * 60)
    print("PATH FROM START VERTEX")
    print("=" * 60)

    for vertex in graph:

        path = get_path(parent, start, vertex)

        if path:
            print(start, "to", vertex, ":",
                  " -> ".join(path))
        else:
            print(start, "to", vertex,
                  ": No Path")

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print("Starting Vertex :", start)
    print("Visited Vertices :", len(traversal))
    print("Traversal Order :", " -> ".join(traversal))

    if len(traversal) == vertices:
        print("Graph is Connected")
    else:
        print("Graph is Disconnected")


if __name__ == "__main__":
    main()
