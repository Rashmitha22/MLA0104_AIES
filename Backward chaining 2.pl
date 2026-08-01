% Facts
human(ravi).
human(sita).
animal(tiger).

% Rules
mortal(X) :-
    human(X).

living(X) :-
    human(X).

living(X) :-
    animal(X).

needs_food(X) :-
    living(X).

% Check goal
check(Goal) :-
    call(Goal),
    write('Yes, Goal Proved: '),
    write(Goal), nl.

check(Goal) :-
    \+ call(Goal),
    write('Goal Cannot Be Proved: '),
    write(Goal), nl.
