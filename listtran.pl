
has_cycle([H|T]) :- member(H, T); has_cycle(T).


test_answer :-
    has_cycle([a,b,c,d,b,e,f]),
    writeln('OK').

test_answer :-
    writeln('Wrong!').
