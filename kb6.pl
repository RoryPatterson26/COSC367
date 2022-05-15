directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(Doll1, Doll2) :- directlyIn(X, Doll1), contains(X, Doll2);
    directlyIn(Doll2, Doll1).


test_answer :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).
