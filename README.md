# MLA0104_AIES

EXPERIMENT NO:1 (Breadth-First Search)

Algorithm Breadth_First_Search(G, Start)

Step 1: Create an empty Queue Q

Step 2: Mark all vertices as NOT VISITED

Step 3: Mark Start as VISITED

Step 4: Insert Start into Q

Step 5: While Q is not empty do
            Remove the front vertex V from Q
            Print V
            For each adjacent vertex U of V do
                If U is NOT VISITED then
                    Mark U as VISITED
                    Insert U into Q
                End If
            End For
        End While

Step 6: Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

EXPERIMENT NO:2 (Depth-First Search)

Algorithm Depth_First_Search(G, Start)

Step 1: Mark all vertices as NOT VISITED

Step 2: Call DFS(Start)

Procedure DFS(Vertex)
    Mark Vertex as VISITED
    Print Vertex
    For each adjacent vertex U of Vertex do
        If U is NOT VISITED then
            Set Parent[U] = Vertex
            DFS(U)
        End If
    End For
End Procedure

Step 3: Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

EXPERIMENT NO 3: Uniform Cost Search (UCS)

Algorithm Uniform_Cost_Search(Graph, Start, Goal)

1. Create an empty Priority Queue PQ

2. Insert (0, Start) into PQ

3. Set Cost[Start] = 0

4. Set Parent[Start] = None

5. Create an empty Visited set

6. While PQ is not empty do
       Remove the node having the lowest cost from PQ
       Let the node be Current
       Let its cost be CurrentCost
       If Current is already in Visited then
           Continue
       End If
       Add Current to Visited
       If Current = Goal then
           Return Cost, Parent and Optimal Path
       End If
       For each neighbour of Current do
           NewCost = CurrentCost + EdgeCost(Current, Neighbour)
           If Neighbour is not present in Cost
              OR NewCost < Cost[Neighbour] then
               Cost[Neighbour] = NewCost
               Parent[Neighbour] = Current
               Insert (NewCost, Neighbour) into PQ
           End If
       End For

   End While

7. Return No Path Found

8. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 4: Water Jug Problem

Algorithm Water_Jug_Problem(Jug1Capacity, Jug2Capacity, Target)

1. Create an empty Queue Q

2. Create an empty Visited set

3. Set InitialState = (0, 0)

4. Insert InitialState into Q

5. Mark InitialState as Visited

6. Set Parent[InitialState] = None

7. While Q is not empty do
       Remove the front state from Q
       Let the state be (X, Y)
       If X = Target OR Y = Target then
           Construct the solution path using Parent
           Display the solution path
           Stop
       End If
       Generate the following possible states:
           a. Fill Jug 1 completely
           b. Fill Jug 2 completely
           c. Empty Jug 1
           d. Empty Jug 2
           e. Pour water from Jug 1 to Jug 2
           f. Pour water from Jug 2 to Jug 1
       For each generated state NewState do
           If NewState is not Visited then
               Mark NewState as Visited
               Set Parent[NewState] = CurrentState
               Insert NewState into Q
           End If
       End For
   End While

8. Display "No solution exists"

9. Stop
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Experiment No-5: A* Search Algorithm

Algorithm A_Star_Search(Graph, Heuristic, Start, Goal)

1. Create an empty Priority Queue OPEN

2. Insert Start into OPEN with priority:
       f(Start) = g(Start) + h(Start)

3. Set:
       g(Start) = 0
       Parent[Start] = None

4. Create an empty CLOSED set

5. While OPEN is not empty do
       Remove the node Current having the lowest f-value
       If Current is already in CLOSED then
           Continue
       End If
       Add Current to CLOSED
       If Current = Goal then
           Construct and return the optimal path
       End If
       For each Neighbour of Current do
           NewCost = g(Current) + EdgeCost(Current, Neighbour)
           If Neighbour is not in g
              OR NewCost < g(Neighbour) then
               g(Neighbour) = NewCost
               f(Neighbour) =
                   g(Neighbour) + h(Neighbour)
               Parent[Neighbour] = Current
               Insert Neighbour into OPEN
               with priority f(Neighbour)
           End If
       End For

   End While

6. Return "No path found"

7. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 6: Greedy Best-First Search

Algorithm Greedy_Best_First_Search(Graph, Heuristic, Start, Goal)

1. Create an empty Priority Queue OPEN

2. Insert Start into OPEN with priority h(Start)

3. Set Parent[Start] = None

4. Create an empty Visited set

5. While OPEN is not empty do
       Remove the node Current having the smallest heuristic value
       If Current is already Visited then
           Continue
       End If
       Mark Current as Visited
       Add Current to the expansion order
       If Current = Goal then
           Construct the path using Parent
           Return the path
       End If
       For each Neighbour of Current do
           If Neighbour is not Visited then
               If Neighbour has no parent then
                   Parent[Neighbour] = Current
               End If
               Insert Neighbour into OPEN
               with priority h(Neighbour)
           End If
       End For

   End While

6. Return "No path found"

7. Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 7: Minimax Algorithm

Algorithm MINIMAX(Node, Depth, IsMaximizingPlayer)

1. If Depth = 0 OR Node is a terminal node then
       Return UtilityValue(Node)
   End If

2. If IsMaximizingPlayer = True then
       BestValue = -∞
       For each Child of Node do
           Value = MINIMAX(
                       Child,
                       Depth - 1,
                       False
                   )
           BestValue = Maximum(BestValue, Value)
       End For
       Return BestValue

3. Else
       BestValue = +∞
       For each Child of Node do
           Value = MINIMAX(
                       Child,
                       Depth - 1,
                       True
                   )
           BestValue = Minimum(BestValue, Value)
       End For
       Return BestValue

4. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 8: Alpha–Beta Pruning

Algorithm ALPHA_BETA(
    Node,
    Depth,
    Alpha,
    Beta,
    IsMaximizingPlayer
)

1. If Depth = 0 OR Node is a terminal node then
       Return UtilityValue(Node)
   End If

2. If IsMaximizingPlayer = True then
       BestValue = -∞
       For each Child of Node do
           Value = ALPHA_BETA(
                       Child,
                       Depth - 1,
                       Alpha,
                       Beta,
                       False
                   )
           BestValue = Maximum(BestValue, Value)
           Alpha = Maximum(Alpha, BestValue)
           If Beta <= Alpha then
               Prune the remaining children
               Break
           End If
       End For
       Return BestValue

3. Else
       BestValue = +∞
       For each Child of Node do
           Value = ALPHA_BETA(
                       Child,
                       Depth - 1,
                       Alpha,
                       Beta,
                       True
                   )
           BestValue = Minimum(BestValue, Value)
           Beta = Minimum(Beta, BestValue)
           If Beta <= Alpha then
               Prune the remaining children
               Break
           End If
       End For
       Return BestValue

4. Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 9:Forward Chaining

Algorithm FORWARD_CHAINING(Facts, Rules, Goal)

1. Create a set KnownFacts containing all initial facts

2. Set Changed = True

3. While Changed = True do
       Set Changed = False
       For each Rule in Rules do
           Let Rule be:
               Premises → Conclusion
           If all Premises are present in KnownFacts then
               If Conclusion is not present in KnownFacts then
                   Add Conclusion to KnownFacts
                   Record the rule that produced Conclusion
                   Set Changed = True
               End If
           End If
       End For
       If Goal is present in KnownFacts then
           Return True
       End If

   End While

4. Return False

5. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 10: Backward Chaining
Algorithm BACKWARD_CHAINING(Goal, Facts, Rules, Visited)

1. If Goal is present in Facts then
       Return True
   End If

2. If Goal is present in Visited then
       Return False
   End If

3. Add Goal to Visited

4. Find all rules whose conclusion is Goal

5. For each matching Rule do
       Assume RuleSatisfied = True
       For each Premise in Rule do
           If BACKWARD_CHAINING(
                  Premise,
                  Facts,
                  Rules,
                  Visited
              ) = False then
               RuleSatisfied = False
               Break
           End If
       End For
       If RuleSatisfied = True then
           Return True
       End If

   End For

6. Return False

7. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 11: N-Queen Problem

Algorithm N_QUEENS(Board, Row, N)

1. If Row = N then
       Display Board
       Increase SolutionCount
       Return
   End If

2. For Column from 0 to N - 1 do
       If placing a queen at Board[Row][Column] is safe then
           Place Queen at Board[Row][Column]
           Call N_QUEENS(Board, Row + 1, N)
           Remove Queen from Board[Row][Column]
           // Backtracking
       End If
   End For
3. Return

Algorithm IS_SAFE(Board, Row, Column, N)

1. Check all previous rows in the same column

2. Check the upper-left diagonal

3. Check the upper-right diagonal

4. If another queen is found then
       Return False
   Else
       Return True
   End If

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 12: Cryptarithmetic Problem

Algorithm SOLVE_CRYPTARITHMETIC(Word1, Word2, Result)

1. Convert Word1, Word2 and Result to uppercase

2. Collect all unique letters from the three words

3. If the number of unique letters is greater than 10 then
       Display "No solution"
       Stop
   End If

4. Identify the leading letters of all multi-letter words

5. Generate every possible assignment of different digits
   to the unique letters

6. For each assignment do
       If any leading letter is assigned 0 then
           Skip this assignment
       End If
       Convert Word1 into a number using the assignment
       Convert Word2 into a number using the assignment
       Convert Result into a number using the assignment
       If Number1 + Number2 = ResultNumber then
           Store the assignment as a solution
       End If

   End For

7. If no solution is stored then
       Display "No solution exists"
   Else
       Display all valid solutions
   End If

8. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 13: Map Coloring Problem

Algorithm MAP_COLORING(Graph, Colors, VertexIndex)

1. If VertexIndex = NumberOfVertices then
       Return True
   End If

2. Select the current vertex

3. For each Color in Colors do
       If the Color is safe for the current vertex then
           Assign Color to the current vertex
           If MAP_COLORING(
                  Graph,
                  Colors,
                  VertexIndex + 1
              ) = True then
               Return True
           End If
           Remove the assigned Color
           // Backtracking
       End If

   End For

4. Return False

2. Return TRUE

END

Algorithm IS_SAFE(Vertex, Color, Graph, Assignment)

1. For each adjacent vertex of Vertex do
       If Assignment[AdjacentVertex] = Color then
           Return False
       End If

   End For

2. Return True

------------------------------------------------------------------------------------------------------------------------------------------------------------------
