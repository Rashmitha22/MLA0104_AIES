% resolution_predicate_logic.pl

% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).
tryassassinate(marcus, caesar).

% Rules
person(X) :-
    man(X).

roman(X) :-
    pompeian(X).

% People who try to assassinate someone are not loyal.
not_loyal(X, Y) :-
    person(X),
    tryassassinate(X, Y).

% If a Roman is not loyal to Caesar, then he hates Caesar.
hates(X, caesar) :-
    roman(X),
    not_loyal(X, caesar).
