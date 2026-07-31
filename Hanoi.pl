% Towers of Hanoi Program

hanoi(1, Source, _, Destination) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

hanoi(N, Source, Auxiliary, Destination) :-
    N > 1,
    N1 is N - 1,

    hanoi(N1, Source, Destination, Auxiliary),

    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl,

    hanoi(N1, Auxiliary, Source, Destination).
