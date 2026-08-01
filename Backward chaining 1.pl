% Backward Chaining Program

% Known facts

fact(has_feathers).
fact(lays_eggs).
fact(can_fly).

% Rules represented as:
% rule(Conclusion, ListOfPremises)

rule(bird, [has_feathers, lays_eggs]).
rule(flying_bird, [bird, can_fly]).
rule(animal, [flying_bird]).
rule(living_organism, [animal]).

% A goal is true if it is a known fact

prove(Goal) :-
    fact(Goal).

% A goal is true if a rule concludes it
% and all its premises can be proved

prove(Goal) :-
    rule(Goal, Premises),
    prove_all(Premises).

% Prove all goals in a list

prove_all([]).

prove_all([Goal | RemainingGoals]) :-
    prove(Goal),
    prove_all(RemainingGoals).
