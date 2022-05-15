def is_valid_expression(object, function_symbols, leaf_symbols):

    if type(object) is int:
        return True
    elif type(object) is str and object in leaf_symbols:
        return True
    elif type(object) is list and len(object) == 3:
        start_valid = type(object[0]) is str and object[0] in function_symbols
        end_valid = [is_valid_expression(object[x], function_symbols, leaf_symbols) for x in range(1, 3)]
        return all([start_valid] + end_valid)
    else:
        return False
    

def depth(expression):
    result = 0
    if type(expression) is list:
        result += max([depth(expression[1]), depth(expression[2])])
        result += 1
    return result

def random_expression(function_symbols, leaves, max_depth):
    if not max_depth or (10 * random.randint(0, 1)) > 5:
        return leaves[random.randint(0, len(leaves) - 1)]
    else:
        return [function_symbols[random.randint(0, len(function_symbols) - 1)], random_expression(function_symbols, leaves, max_depth - 1), random_expression(function_symbols, leaves, max_depth - 1)]

def evaluate(expression, bindings):
    if type(expression) is int:
        return expression
    elif type(expression) is str:
        return bindings[expression]
    else:
        func = bindings[expression[0]]
        return func(evaluate(expression[1], bindings), evaluate(expression[2], bindings))


def generate_rest(initial_sequence, expression, length_to_generate):
    results = initial_sequence[::]
    bindings_list = {
        "i": len(results),
        "x": results[-2],
        "y": results[-1],        
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
    }

    for i in range(length_to_generate):
        result = evaluate(expression, bindings)
        results.append(result)

        bindings_list["i"] = len(results)
        bindings_list["x"] = results[-2]
        bindings_list["y"] = results[-1]

    return results[len(initial_sequence):]
