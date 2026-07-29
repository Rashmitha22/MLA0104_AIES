# MLA0104_AIES

EXPERIMENT NO:1 (Breadth-First Search)

1. Create an empty Queue Q.
2. Create an empty Set Visited.
3. Enqueue(Start) into Q.
4. Add Start to Visited.
5. While Q is not empty do
      a. Node ← Dequeue(Q)
      b. Print(Node)
      c. For each Neighbor of Node do
            If Neighbor is not in Visited then
                Add Neighbor to Visited
                Enqueue(Neighbor)
            End If
         End For
   End While
6. Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

EXPERIMENT NO:2 (Depth-First Search)

Algorithm DFS(Graph, Node, Visited)

1. If Node is not in Visited then
      Add Node to Visited
      Print(Node)

      For each Neighbor of Node do
           If Neighbor is not in Visited then
                DFS(Graph, Neighbor, Visited)
           End If
      End For
   End If

2. Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

EXPERIMENT NO 3: Uniform Cost Search (UCS)

Algorithm UCS(Graph, Start, Goal)

1. Create a Priority Queue PQ
2. Insert (0, Start) into PQ
3. Create an empty Set Visited

4. While PQ is not empty do
      (Cost, Node) ← Remove node with minimum cost

      If Node = Goal then
           Print Cost
           Stop
      End If

      If Node is not in Visited then
           Add Node to Visited
         **  For each (Neighbor, EdgeCost) of Node do
                If Neighbor is not in Visited then
                     Insert (Cost + EdgeCost, Neighbor) into PQ
                End If
           End For**
      End If
   End While

5. Print "Goal not found"

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 4: Water Jug Problem

Algorithm WaterJug(x, y, target)

1. Create an empty queue Q.
2. Create an empty set Visited.
3. Insert the initial state (0, 0) into Q.
4. Mark (0, 0) as visited.

5. While Q is not empty do
      a. Remove state (a, b) from Q.
      b. If a = target or b = target then
            Print "Target reached"
            Stop
      c. Generate all possible next states:
            - Fill Jug1
            - Fill Jug2
            - Empty Jug1
            - Empty Jug2
            - Pour Jug1 into Jug2
            - Pour Jug2 into Jug1
      d. Add each unvisited state to Q.
   End While

6. Print "No solution exists."
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------

   Experiment No-5: A* Search Algorithm

   Algorithm A_STAR(Graph, Start, Goal, Heuristic)

1. Create an empty priority queue OPEN.
2. Insert Start into OPEN with priority h(Start).
3. Set g(Start) = 0.
4. Set Parent(Start) = NULL.
5. Create an empty set CLOSED.

6. WHILE OPEN is not empty DO

      Current ← Remove node with minimum f-value from OPEN

      IF Current = Goal THEN
          Construct and print the path
          Print total cost
          STOP
      END IF

      Add Current to CLOSED

      FOR each Neighbor of Current DO
          NewCost ← g(Current) + Cost(Current, Neighbor)
          IF Neighbor is not in CLOSED
             OR NewCost < g(Neighbor) THEN
              g(Neighbor) ← NewCost
              f(Neighbor) ← g(Neighbor) + h(Neighbor)
              Parent(Neighbor) ← Current
              Insert or update Neighbor in OPEN
          END IF

      END FOR

   END WHILE
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 6: Greedy Best-First Search

Algorithm GREEDY_BEST_FIRST_SEARCH(Graph, Start, Goal, Heuristic)

1. Create an empty Priority Queue OPEN.
2. Create an empty Set VISITED.
3. Insert Start into OPEN with priority h(Start).

4. WHILE OPEN is not empty DO

      Current ← Remove node with minimum heuristic value from OPEN

      IF Current = Goal THEN
          Print the path
          STOP
      END IF

      IF Current is not in VISITED THEN
          Add Current to VISITED
          FOR each Neighbor of Current DO
              IF Neighbor is not in VISITED THEN
                  Insert Neighbor into OPEN with priority h(Neighbor)
                  Store Current as Parent of Neighbor
              END IF
          END FOR
      END IF

   END WHILE

5. Print "Goal not found."

END

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 7: Minimax Algorithm

Algorithm MINIMAX(Node, Depth, IsMax)

1. If Node is a terminal node OR Depth = 0 then
       Return Utility(Node)

2. If IsMax = TRUE then
       Best ← -∞
       For each Child of Node do
            Value ← MINIMAX(Child, Depth-1, FALSE)
            Best ← max(Best, Value)
       End For
       Return Best

3. Else
       Best ← +∞
       For each Child of Node do
            Value ← MINIMAX(Child, Depth-1, TRUE)
            Best ← min(Best, Value)
       End For
       Return Best
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 8: Alpha–Beta Pruning

Algorithm ALPHA_BETA(Node, Depth, Alpha, Beta, IsMax)

1. If Node is a terminal node OR Depth = 0 then
       Return Utility(Node)

2. If IsMax = TRUE then
       Best ← -∞
       For each Child of Node do
            Value ← ALPHA_BETA(
                        Child,
                        Depth - 1,
                        Alpha,
                        Beta,
                        FALSE
                     )
            Best ← maximum(Best, Value)
            Alpha ← maximum(Alpha, Best)
            If Alpha ≥ Beta then
                 Break
            End If
       End For
       Return Best

3. Else
       Best ← +∞
       For each Child of Node do
            Value ← ALPHA_BETA(
                        Child,
                        Depth - 1,
                        Alpha,
                        Beta,
                        TRUE
                     )
            Best ← minimum(Best, Value)
            Beta ← minimum(Beta, Best)
            If Alpha ≥ Beta then
                 Break
            End If
       End For
       Return Best

END

8. Print "Goal not found."

END

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 9:Forward Chaining
Algorithm FORWARD_CHAINING(Facts, Rules, Goal)

1. Repeat
2.    NewFact ← False
3.    For each Rule in Rules do
4.         If Rule conditions are satisfied AND
              Rule conclusion is not in Facts then
5.              Add Rule conclusion to Facts
6.              NewFact ← True
7.         End If
8.    End For
9. Until Goal is in Facts OR NewFact = False

10. If Goal is in Facts then
11.      Print "Goal achieved"
12. Else
13.      Print "Goal not achieved"
14. End If

END
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 10: Backward Chaining
Algorithm BACKWARD_CHAINING(Goal, Facts, Rules)

1. If Goal is present in Facts then
       Return TRUE
   End If

2. For each Rule in Rules do
       If Rule conclusion = Goal then
            AllProved ← TRUE
            For each Condition in Rule conditions do
                 If BACKWARD_CHAINING(
                       Condition,
                       Facts,
                       Rules
                    ) = FALSE then
                      AllProved ← FALSE
                      Break
                 End If
            End For
            If AllProved = TRUE then
                 Return TRUE
            End If
       End If

   End For

3. Return FALSE

END
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 11: N-Queen Problem

Algorithm N_QUEEN(Board, Row, N)

1. If Row = N then
       Print Board
       Return TRUE
   End If

2. For Column ← 0 to N - 1 do
       If IS_SAFE(Board, Row, Column, N) then
            Place Queen at Board[Row][Column]
            If N_QUEEN(Board, Row + 1, N) = TRUE then
                 Return TRUE
            End If
            Remove Queen from Board[Row][Column]
       End If

   End For

3. Return FALSE
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 12: Cryptarithmetic Problem
Algorithm CRYPTARITHMETIC


1. Set Words ← ["SEND", "MORE"]
2. Set Result ← "MONEY"

3. Find all unique letters from Words and Result.

4. Generate all possible digit assignments for the letters.

5. For each assignment do

      If a leading letter is assigned 0 then
           Continue with the next assignment
      End If

      SEND_VALUE ← Convert SEND using assigned digits
      MORE_VALUE ← Convert MORE using assigned digits
      MONEY_VALUE ← Convert MONEY using assigned digits

      If SEND_VALUE + MORE_VALUE = MONEY_VALUE then
           Print the letter-digit assignment
           Print the arithmetic equation
           Stop
      End If

   End For

6. Print "No solution found."

END

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 13: Map Coloring Problem

Algorithm MAP_COLORING(Graph, m, Vertex)

1. If Vertex = Number of Vertices then
       Return TRUE

2. For Color ← 1 to m do
       If IS_SAFE(Graph, Color, Vertex) then
            Assign Color to Vertex
            If MAP_COLORING(Graph, m, Vertex + 1) = TRUE then
                 Return TRUE
            End If
            Remove Color from Vertex
       End If

   End For

3. Return FALSE

END
Algorithm IS_SAFE(Graph, Color, Vertex)

1. For every Adjacent Vertex do
       If Adjacent Vertex has the same Color then
            Return FALSE
       End If
2. Return TRUE

END

------------------------------------------------------------------------------------------------------------------------------------------------------------------
