reflection(point(X1, Y1), point(X2, Y2)) :-
	=(X1, Y2), =(Y1, X2).

test_answer :-
	reflection(point(3, 6), point(6, 3)),
        writeln('OK').
