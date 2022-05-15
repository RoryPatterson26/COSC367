eats(X, Y):- likes(X, Y).
eats(A, B):- hungry(A), edible(B).


edible(crisps).
hungry(bob).
likes(bob, sushi).

test_answer :- eats(bob, crisps),
               writeln('Bob eats crisps.').
