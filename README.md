 # MLA0104_AIES

------------------------------------------------------------------------------------------------------------------------------------------------------------------

EXPERIMENT NO:1 Breadth-First Search in python.

Breadth_First_Search(G, Start)

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

EXPERIMENT NO:2 (Depth-First Search)in python.

Depth_First_Search(G, Start)

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

EXPERIMENT NO 3: Uniform Cost Search (UCS)in python.

Uniform_Cost_Search(Graph, Start, Goal)

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

8. Return No Path Found

9. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 4: Water Jug Problem in python.

Water_Jug_Problem(Jug1Capacity, Jug2Capacity, Target)

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

9. Display "No solution exists"

10. Stop
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No-5: A* Search Algorithm in python.

A_Star_Search(Graph, Heuristic, Start, Goal)

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

7. Return "No path found"

8. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 6: Greedy Best-First Search in python.

Greedy_Best_First_Search(Graph, Heuristic, Start, Goal)

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

7. Return "No path found"

8. Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 7: Minimax Algorithm in python.

MINIMAX(Node, Depth, IsMaximizingPlayer)

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

4. Else
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

6. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 8: Alpha–Beta Pruning in python.

ALPHA_BETA(
    Node,
    Depth,
    Alpha,
    Beta,
    IsMaximizingPlayer
)

1. If Depth = 0 OR Node is a terminal node then
   
       Return UtilityValue(Node)
   End If

3. If IsMaximizingPlayer = True then
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

4. Else
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

6. Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 9:Forward Chaining in python.

FORWARD_CHAINING(Facts, Rules, Goal)

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

5. Return False

6. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 10: Backward Chaining in python.

BACKWARD_CHAINING(Goal, Facts, Rules, Visited)

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

7. Return False

8. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 11: N-Queen Problem in python.

N_QUEENS(Board, Row, N)

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
4. Return

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

Experiment No 12: Cryptarithmetic Problem in python.

SOLVE_CRYPTARITHMETIC(Word1, Word2, Result)

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

8. If no solution is stored then
       Display "No solution exists"
   Else
       Display all valid solutions
   End If

9. Stop
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 13: Map Coloring Problem in python.

MAP_COLORING(Graph, Colors, VertexIndex)

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

5. Return False

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
Experiment No 14:Sum of Integers from 1 to N using Recursion in Prolog

1. Start
2. Read the value of N
3. If N = 0, return 0
4. Otherwise,
      Sum = N + Sum(N-1)
5. Display the Sum
6. Stop

 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 15:Database with Name and Date of Birth using Prolog

NAME_DOB_DATABASE

Step 1: Store Name and DOB as facts.

Step 2: Accept a query for a person's name.

Step 3: Search the database.

Step 4: If the name exists then
            Display the DOB.
        Else
            Display "Record Not Found."

Step 5: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 16:Student–Teacher–Subject Code Database using Prolog

STUDENT_TEACHER_DATABASE

Step 1: Store Student Name, Teacher Name and Subject Code.

Step 2: Accept a query.

Step 3: Search the database.

Step 4: If a matching record is found then
            Display Student, Teacher and Subject Code.
        Else
            Display "Record Not Found."

Step 5: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 17:Planets Database using Prolog

PLANETS_DATABASE

Step 1: Store Planet Name, Position, Type and Number of Moons.

Step 2: Accept a query for a planet.

Step 3: Search the planets database.

Step 4: If the planet is found then
            Display its details.
        Else
            Display "Planet not found."
           
Step 5: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 18:Towers of Hanoi using Prolog

TOWERS_OF_HANOI(N, Source, Auxiliary, Destination)

Step 1: If N = 1 then
            Display "Move disk from Source to Destination"
            Return
        End If

Step 2: Call TOWERS_OF_HANOI(
            N - 1,
            Source,
            Destination,
            Auxiliary
        )

Step 3: Display "Move disk from Source to Destination"

Step 4: Call TOWERS_OF_HANOI(
            N - 1,
            Auxiliary,
            Source,
            Destination
        )

Step 5: Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 19:Bird Flying Database using Prolog

BIRD_DATABASE

Step 1: Store birds that can fly.

Step 2: Store birds that cannot fly.

Step 3: Accept the bird name.

Step 4: Search the database.

Step 5:
        If bird is in can_fly list then
            Display "Bird can fly."
        Else if bird is in cannot_fly list then
            Display "Bird cannot fly."
        Else
            Display "Bird not found."

Step 6: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 20:Family Tree using Prolog

FAMILY_TREE

Step 1: Store male and female persons.

Step 2: Store parent relationships.

Step 3:
        Mother(X,Y) ← Female(X) AND Parent(X,Y)

Step 4:
        Father(X,Y) ← Male(X) AND Parent(X,Y)

Step 5:
        Grandfather(X,Y) ← Male(X) AND Parent(X,Z) AND Parent(Z,Y)

Step 6:
        Grandmother(X,Y) ← Female(X) AND Parent(X,Z) AND Parent(Z,Y)

Step 7:
        Sister(X,Y) ← Female(X) AND Parent(P,X) AND Parent(P,Y) AND X ≠ Y

Step 8: Display required results.

Step 9: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 21:Disease-Based Diet Suggestion System using Prolog

DIET_SUGGESTION_SYSTEM

Step 1: Store disease and recommended diet details.

Step 2: Accept the disease name.

Step 3: Search the database.

Step 4: If the disease exists then
            Display recommended food.
            Display food to avoid.
        Else
            Display "No diet information found."

Step 5: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 22:Monkey Banana Problem using Prolog

MONKEY_BANANA

Step 1: Set the initial state:
        Monkey at door
        Monkey on floor
        Box at window
        Monkey does not have banana

Step 2: If the monkey has the banana then
            Return success
        End If

Step 3: Generate a valid action:
        Walk
        Push
        Climb
        Grasp

Step 4: Apply the action and create a new state.

Step 5: Repeat Steps 2 to 4 until the banana is obtained.

Step 6: Display the action sequence.

Step 7: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 23:Fruit and Color Identification using Backtracking in Prolog

FRUIT_COLOR_BACKTRACKING

Step 1: Store Fruit and Color as facts.

Step 2: Accept a query.

Step 3: Search for a matching fact.

Step 4: Display the first matching fruit and color.

Step 5: If the user requests another solution then
            Backtrack and search for the next matching fact.
        Else
            Stop.
        End If

Step 6: When no more matching facts exist,
        Display false.

Step 7: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 24:Best First Search Algorithm using Prolog

BEST_FIRST_SEARCH(Start, Goal)

Step 1: OPEN ← [(Start, h(Start), [Start])]

Step 2: VISITED ← empty list

Step 3: While OPEN is not empty do
            Select the node with the smallest heuristic value.
            Remove it from OPEN.
            If CurrentNode = Goal then
                Return Path.
            End If
            If CurrentNode is not in VISITED then
            
                Add CurrentNode to VISITED.
                Generate all adjacent nodes.
                For each adjacent node do
                    If it is not in VISITED then
                        Add it to OPEN with:
                        heuristic value and updated path.
                    End If
                End For
                Sort OPEN by heuristic value.
            End If
        End While

Step 4: Return "No path found."

Step 5: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 25:Medical Diagnosis Expert System using Prolog

MEDICAL_DIAGNOSIS

Step 1: Store symptoms for each disease.

Step 2: Accept patient symptoms.

Step 3: Compare the symptoms with disease rules.

Step 4: If all required symptoms match then
            Display the disease name.
        Else
            Check the next disease rule.
        End If

Step 5: If no disease rule matches then
            Display "Diagnosis not found."

Step 6: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 26:Forward Chaining -1 using Prolog

FORWARD_CHAINING

Step 1: Store the initial facts.

Step 2: Store the rules in the form:
        Premises -> Conclusion

Step 3: Check every rule.

Step 4: If all premises of a rule are true then
            Derive the conclusion.
        End If

Step 5: Add the conclusion to the known facts.

Step 6: Repeat until no new facts can be derived
        or the required goal is reached.

Step 7: Display whether the goal is proved.

Step 8: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 27:Backward Chaining -1 using Prolog

BACKWARD_CHAINING(Goal)

Step 1: If Goal is a known fact then
            Return True
        End If

Step 2: Find a rule:
            Premises -> Goal

Step 3: For each Premise do
            Call BACKWARD_CHAINING(Premise)
        End For

Step 4: If all premises are proved then
            Return True
        Else
            Return False
        End If
Step 5: Stop

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 28:Knowledge Representation using Prolog.

1.Start the program.

2.Define the rule that John likes every food.

3.Define the food items (apple and vegetable).

4.Define that John likes peanuts.

5.Define that Mary eats everything Anil eats.

6.Define that Anil eats peanuts and is alive.

7.Define the rule that anything eaten by someone and not killed is food.

8.Execute queries to verify the knowledge base.

9.Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No 29:Resolution Using Predicate Logic Using Prolog

RESOLUTION_PREDICATE_LOGIC()

Step 1: Enter the facts into the knowledge base.

Marcus is a man.
Marcus is a Pompeian.
Caesar is a ruler.
Marcus tried to assassinate Caesar.

Step 2: Define the rules.

Every man is a person.

Every Pompeian is a Roman.

Anyone who tries to assassinate someone is not loyal to that person.

Every Roman who is not loyal to Caesar hates Caesar.

Step 3: Load the knowledge base into Prolog.

Step 4: Execute the query.

loyal(marcus, caesar).

If Marcus is loyal to Caesar then

Return True

Else

Return False

End If

Step 5: Execute the query.

hates(marcus, caesar).

If Marcus hates Caesar then

Return True

Else

Return False

End If

Step 6: Display the inference results.

Step 7: Stop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 30:Forward Chaining-2 in Prolog

START

Create a list called KNOWN_FACTS

Add all initial facts to KNOWN_FACTS

REPEAT
    NEW_FACT_ADDED = FALSE
    FOR every rule in the knowledge base
    
        IF all conditions of the rule are in KNOWN_FACTS
           AND the conclusion is not already in KNOWN_FACTS
        THEN
            Add the conclusion to KNOWN_FACTS
            Set NEW_FACT_ADDED = TRUE
        END IF
    END FOR

UNTIL NEW_FACT_ADDED = FALSE

Display all facts in KNOWN_FACTS

STOP

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experiment No 31:Backward Chaining-2 in Prolog

START
Take a goal
Check whether the goal is a known fact
IF the goal is a fact
    Display "Goal proved"
ELSE
    Find a rule that can produce the goal
    
    IF such a rule exists
        Check all conditions of the rule
        IF all conditions are proved
            Display "Goal proved"
        ELSE
            Display "Goal not proved"
        END IF
    ELSE
        Display "Goal not proved"
    END IF
END IF

STOP

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No:32

Implementation of Decision Tree Classification using Python

START

1. Create the training dataset.

2. Assign numerical values for:
      Weather:
          0 → Sunny
          1 → Overcast
          2 → Rain

      Temperature:
          0 → Hot
          1 → Mild
          2 → Cool

3. Assign output values:
      0 → No
      1 → Yes

4. Create a Decision Tree Classifier.

5. Train the classifier using the training data.

6. Get Weather value from the user.

7. Get Temperature value from the user.

8. Give the user input to the Decision Tree.

9. Predict the result.

10. If result = 1:
        Display "YES, You can play"
    Else:
        Display "NO, You cannot play"

STOP
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No:33

Implementation of Feed Forward Propagation in a Neural Network using Python

START

1. Read input values x1 and x2.

2. Read weights w1 and w2.

3. Read bias b.

4. Calculate weighted sum:

      net = (x1 × w1) + (x2 × w2) + b

5. Apply Sigmoid activation function:

      output = 1 / (1 + e^(-net))

6. Display the weighted sum.

7. Display the final output.

STOP
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Experiment No:34

Implementation of Backward Propagation (Backpropagation) in a Neural Network using Python

START

1. Read input values x1 and x2.

2. Read weights w1 and w2.

3. Read bias b.

4. Read the target output.

5. Calculate weighted sum:

      net = (x1 × w1) + (x2 × w2) + b

6. Calculate predicted output using Sigmoid:

      output = 1 / (1 + e^(-net))

7. Calculate error:

      error = target - output

8. Calculate gradient:

      gradient = error × output × (1 - output)

9. Update the weights:

      w1 = w1 + learning_rate × gradient × x1
      w2 = w2 + learning_rate × gradient × x2

10. Update the bias:

      b = b + learning_rate × gradient

11. Display the error and updated weights.

STOP

------------------------------------------------------------------------------------------------------------------------------------------------------------------
