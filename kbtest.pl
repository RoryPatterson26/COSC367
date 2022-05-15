reflection(point1(A, B), point2(C, D)):- point(X, Y), point(Y,X).

test_answer :-
    reflection(point(3, 6), point(6, 3)),
    writeln('OK').
