from queue import PriorityQueue

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


def heuristic(state):
    """Number of misplaced tiles."""
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count


def neighbours(state):
    blank = state.index(0)
    result = []

    for move in MOVES[blank]:
        temp = list(state)
        temp[blank], temp[move] = temp[move], temp[blank]
        result.append(tuple(temp))

    return result


def print_board(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


def astar(start):

    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start))

    visited = {}
    parent = {}

    visited[start] = 0
    parent[start] = None

    while not pq.empty():

        f, g, state = pq.get()

        if state == GOAL:

            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("\nA* SOLUTION FOUND\n")

            for step, board in enumerate(path):
                print("Step", step)
                print_board(board)

            print("Total Moves =", len(path) - 1)
            return

        for nxt in neighbours(state):

            new_cost = g + 1

            if nxt not in visited or new_cost < visited[nxt]:
                visited[nxt] = new_cost
                priority = new_cost + heuristic(nxt)
                pq.put((priority, new_cost, nxt))
                parent[nxt] = state

    print("No Solution Found")


if __name__ == "__main__":

    start = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    print("INITIAL STATE\n")
    print_board(start)

    astar(start)
