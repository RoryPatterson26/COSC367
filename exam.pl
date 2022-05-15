even_length([]).
even_length([_,_|T]) :- even_length(T).

same_evens([], Y).
same_evens([_,H|T], Y) :- H=Y, same_evens(T, Y).

same_evens([_,H|T]):- same_evens(T, H).

test_answer :-
    same_evens([a, b, c, b, d, b]),
    same_evens([a, b]),
    same_evens([]),
    writeln('OK').
