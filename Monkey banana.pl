% Monkey Banana Problem
% state(MonkeyPosition, MonkeyStatus, BoxPosition, BananaStatus)

move(
    state(middle, on_box, middle, has_not),
    grasp,
    state(middle, on_box, middle, has)
).

move(
    state(Position, on_floor, Position, has_not),
    climb,
    state(Position, on_box, Position, has_not)
).

move(
    state(Position1, on_floor, Position1, has_not),
    push(Position1, Position2),
    state(Position2, on_floor, Position2, has_not)
) :-
    Position1 \= Position2.

move(
    state(Position1, on_floor, BoxPosition, has_not),
    walk(Position1, Position2),
    state(Position2, on_floor, BoxPosition, has_not)
) :-
    Position1 \= Position2.

goal(state(_, _, _, has)).

solve(State, [], _) :-
    goal(State).

solve(State, [Action | RemainingActions], Visited) :-
    move(State, Action, NewState),
    \+ member(NewState, Visited),
    solve(
        NewState,
        RemainingActions,
        [NewState | Visited]
    ).

monkey_banana(Actions) :-
    InitialState = state(door, on_floor, window, has_not),
    solve(
        InitialState,
        Actions,
        [InitialState]
    ).
