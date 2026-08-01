% File name: food_knowledge_base.pl

:- dynamic killed/1.

% Food facts and rules must be together
food(apple).
food(vegetable).

food(Y) :-
    eats(_, Y),
    \+ killed(Y).

% John likes every food
likes(john, X) :-
    food(X).

% John likes peanuts
likes(john, peanuts).

% Anil eats peanuts
eats(anil, peanuts).

% Mary eats everything Anil eats
eats(mary, X) :-
    eats(anil, X).

% Anil is alive
alive(anil).
