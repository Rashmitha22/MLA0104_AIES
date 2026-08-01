% Forward Chaining Program

% Initial facts

fact(has_feathers).
fact(lays_eggs).
fact(can_fly).

% Rules

bird :-
    fact(has_feathers),
    fact(lays_eggs).

flying_bird :-
    bird,
    fact(can_fly).

animal :-
    flying_bird.

living_organism :-
    animal.
