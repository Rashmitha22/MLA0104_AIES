from collections import deque
import tkinter as tk
from typing import Dict, List, Optional, Tuple

Position = Tuple[int, int]

# 0 = open path
# 1 = wall
# 2 = start
# 3 = goal
MAZE = [
    [2, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 3]
]

ROWS = len(MAZE)
COLS = len(MAZE[0])
CELL_SIZE = 70


def find_value(value: int) -> Optional[Position]:
    """Find the position of a value in the maze."""
    for row in range(ROWS):
        for column in range(COLS):
            if MAZE[row][column] == value:
                return row, column
    return None


def bfs_shortest_path(
    start: Position,
    goal: Position
) -> Optional[List[Position]]:
    """Return the shortest path from start to goal using BFS."""

    queue = deque([start])
    visited = {start}

    parent: Dict[Position, Optional[Position]] = {
        start: None
    }

    # Up, Down, Left, Right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        current_row, current_column = queue.popleft()

        if (current_row, current_column) == goal:
            path: List[Position] = []
            current: Optional[Position] = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for row_change, column_change in directions:
            new_row = current_row + row_change
            new_column = current_column + column_change
            next_position = (new_row, new_column)

            is_inside_maze = (
                0 <= new_row < ROWS
                and 0 <= new_column < COLS
            )

            if not is_inside_maze:
                continue

            is_wall = MAZE[new_row][new_column] == 1

            if not is_wall and next_position not in visited:
                visited.add(next_position)
                parent[next_position] = (
                    current_row,
                    current_column
                )
                queue.append(next_position)

    return None


def convert_path_to_moves(path: List[Position]) -> List[str]:
    """Convert path coordinates into movement directions."""
    moves: List[str] = []

    for index in range(1, len(path)):
        previous_row, previous_column = path[index - 1]
        current_row, current_column = path[index]

        row_difference = current_row - previous_row
        column_difference = current_column - previous_column

        if row_difference == -1:
            moves.append("UP")
        elif row_difference == 1:
            moves.append("DOWN")
        elif column_difference == -1:
            moves.append("LEFT")
        elif column_difference == 1:
            moves.append("RIGHT")

    return moves


class MazeApplication:
    def __init__(self, root: tk.Tk, path: List[Position]) -> None:
        self.root = root
        self.path = path
        self.current_path_index = 0

        self.root.title("AI Maze Escape using BFS")

        canvas_width = COLS * CELL_SIZE
        canvas_height = ROWS * CELL_SIZE

        self.canvas = tk.Canvas(
            root,
            width=canvas_width,
            height=canvas_height,
            background="white"
        )
        self.canvas.pack(padx=15, pady=15)

        self.status_label = tk.Label(
            root,
            text="Press Start BFS to begin",
            font=("Arial", 14)
        )
        self.status_label.pack(pady=5)

        self.start_button = tk.Button(
            root,
            text="Start BFS",
            command=self.start_animation,
            font=("Arial", 13)
        )
        self.start_button.pack(pady=10)

        self.draw_maze()
        self.draw_robot(path[0])

    def draw_maze(self) -> None:
        """Draw the complete maze."""
        for row in range(ROWS):
            for column in range(COLS):
                x1 = column * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                cell = MAZE[row][column]

                if cell == 1:
                    fill_colour = "black"
                elif cell == 2:
                    fill_colour = "lightblue"
                elif cell == 3:
                    fill_colour = "lightgreen"
                else:
                    fill_colour = "white"

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=fill_colour,
                    outline="gray"
                )

                if cell == 2:
                    self.canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2,
                        text="START",
                        font=("Arial", 10, "bold")
                    )

                if cell == 3:
                    self.canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2,
                        text="GOAL",
                        font=("Arial", 10, "bold")
                    )

    def draw_robot(self, position: Position) -> None:
        """Draw the AI robot at the specified position."""
        self.canvas.delete("robot")

        row, column = position

        margin = 15

        x1 = column * CELL_SIZE + margin
        y1 = row * CELL_SIZE + margin
        x2 = (column + 1) * CELL_SIZE - margin
        y2 = (row + 1) * CELL_SIZE - margin

        self.canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            fill="orange",
            outline="red",
            width=2,
            tags="robot"
        )

    def start_animation(self) -> None:
        """Start animating the shortest BFS path."""
        self.start_button.config(state=tk.DISABLED)
        self.current_path_index = 0
        self.status_label.config(text="BFS is finding the shortest path...")
        self.animate_path()

    def animate_path(self) -> None:
        """Move the robot along the shortest path."""
        if self.current_path_index < len(self.path):
            position = self.path[self.current_path_index]
            self.draw_robot(position)

            move_number = self.current_path_index

            self.status_label.config(
                text=f"Move: {move_number}"
            )

            self.current_path_index += 1
            self.root.after(500, self.animate_path)

        else:
            total_moves = len(self.path) - 1

            self.status_label.config(
                text=f"You win! Goal reached in {total_moves} moves."
            )


def main() -> None:
    start = find_value(2)
    goal = find_value(3)

    if start is None:
        raise ValueError("Start position is missing from the maze.")

    if goal is None:
        raise ValueError("Goal position is missing from the maze.")

    shortest_path = bfs_shortest_path(start, goal)

    if shortest_path is None:
        print("No valid path exists between START and GOAL.")
        return

    moves = convert_path_to_moves(shortest_path)

    print("Shortest path found using BFS")
    print("Path coordinates:", shortest_path)
    print("Movement sequence:", " → ".join(moves))
    print("Total number of moves:", len(moves))

    root = tk.Tk()
    MazeApplication(root, shortest_path)
    root.mainloop()


if __name__ == "__main__":
    main()
