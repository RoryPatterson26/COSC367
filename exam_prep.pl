leaf(Z).
tree(X, Y, Z) :- tree(Y); leaf(Y), tree(Z); leaf(Z).
inorder(X, Y) :-

test_answer :- inorder(tree(1, leaf(2), leaf(3)), T), writeln(T).
