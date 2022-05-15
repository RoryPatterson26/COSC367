
def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        # Complete (a line or two)

        a = sum([weight * i for weight, i in zip(weights, input)])

        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        return 1 if a + bias >= 0 else 0

    return perceptron  # this line is fine

def update_weights(old_weights, eta, inputs, target_diff):
    new_weights = []
    for i in range(len(old_weights)):
        inp = inputs[i]
        weight = old_weights[i]
        new_weights.append(weight + eta * inp * target_diff)
    return new_weights


def update_bias(old_bias, eta, target_diff):
    return old_bias + eta * target_diff


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):

    for _ in range(max_epochs):
        for example, target in training_examples:
            perceptron = construct_perceptron(weights, bias)
            output = perceptron(example)
            if output != target:
                # Update the weight
                target_diff = target - output
                weights = update_weights(weights, learning_rate, example, target_diff)
                bias = update_bias(bias, learning_rate, target_diff)
            print(f"{weights}")
            print(f"{bias}")
    return weights, bias


max_epochs = 1
weights = [1, 1]
bias = 1
learning_rate = 0.5
examples = [
    ([1, -1], 0),   # index 0 (first example)
    ([1, 4], 0),
    ([-1, -1], 1),
    ([3, 4], 1),
]

w,b = learn_perceptron_parameters(weights,bias,examples,learning_rate,max_epochs)
