% Best First Search Algorithm

% Graph edges
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).

% Heuristic values
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 4).
heuristic(d, 5).
heuristic(e, 2).
heuristic(f, 3).
heuristic(g, 0).

% Entry point
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    best_first(
        Goal,
        [[H, Start, [Start]]],
        [],
        ReversePath
    ),
    reverse(ReversePath, Path).

% Goal found
best_first(
    Goal,
    [[_, Goal, Path] | _],
    _,
    Path
).

% Expand the best node
best_first(
    Goal,
    [[_, Current, Path] | Open],
    Visited,
    FinalPath
) :-
    \+ member(Current, Visited),

    findall(
        [H, Next, [Next | Path]],
        (
            edge(Current, Next),
            \+ member(Next, Visited),
            \+ member(Next, Path),
            heuristic(Next, H)
        ),
        Children
    ),

    append(Open, Children, NewOpen),
    sort(NewOpen, SortedOpen),

    best_first(
        Goal,
        SortedOpen,
        [Current | Visited],
        FinalPath
    ).

% Skip already visited nodes
best_first(
    Goal,
    [[_, Current, _] | Open],
    Visited,
    FinalPath
) :-
    member(Current, Visited),

    best_first(
        Goal,
        Open,
        Visited,
        FinalPath
    ).
