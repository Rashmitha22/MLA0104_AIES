% ---------------------------------------
% Forward Chaining Program in Prolog
% ---------------------------------------

% Initial facts
initial_fact(human(ravi)).
initial_fact(human(sita)).
initial_fact(animal(tiger)).

% Rules
% rule(Conclusion, Conditions).

rule(mortal(X), [human(X)]).
rule(living(X), [human(X)]).
rule(living(X), [animal(X)]).
rule(needs_food(X), [living(X)]).

% Start forward chaining
forward_chain :-
    retractall(known(_)),
    load_initial_facts,
    apply_rules,
    nl,
    write('All derived facts:'), nl,
    show_facts.

% Load initial facts into the knowledge base
load_initial_facts :-
    initial_fact(Fact),
    assertz(known(Fact)),
    fail.

load_initial_facts.

% Apply all rules until no new facts are produced
apply_rules :-
    rule(Conclusion, Conditions),
    conditions_true(Conditions),
    \+ known(Conclusion),
    assertz(known(Conclusion)),
    write('Derived: '),
    write(Conclusion),
    nl,
    fail.

apply_rules :-
    new_fact_available,
    !,
    apply_rules.

apply_rules.

% Check whether every condition is known
conditions_true([]).

conditions_true([Condition | Rest]) :-
    known(Condition),
    conditions_true(Rest).

% Check whether any rule can generate a new fact
new_fact_available :-
    rule(Conclusion, Conditions),
    conditions_true(Conditions),
    \+ known(Conclusion),
    !.

% Display all known and derived facts
show_facts :-
    known(Fact),
    write(Fact),
    nl,
    fail.

show_facts.

% Ask whether a particular fact is true
query(Fact) :-
    forward_chain,
    (
        known(Fact)
        ->
        write('Yes, the fact is true: '),
        write(Fact)
        ;
        write('No, the fact could not be derived: '),
        write(Fact)
    ),
    nl.
