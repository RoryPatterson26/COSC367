

already_installed([P|Q]) :- installed(P), already_installed(Q).
can_be_installed(Software) :- requires(Software, [H|T]), already_installed(T), installed(H).



requires(prolog, [cmake, yaml, ncurses]).

installed([cmake, java]).
installed([yaml, json]).
installed([vim, emacs]).
installed([ncurses]).

test_answer :-
    can_be_installed(prolog),
    writeln("OK").

test_answer :-
    \+ can_be_installed(prolog),
    writeln("Wrong!").
