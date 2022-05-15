import math

def max_value(tree):
    if type(tree) is int:
        return tree

    value = -1 * math.inf
    for t in tree:
        value = max(value, min_value(t))
    return value


def min_value(tree):
    if type(tree) is int:
        return tree

    value = math.inf
    for t in tree:
        value = min(value, max_value(t))
    return value

def min_action_value(tree):
    if type(tree) is int:
        return None, tree

    value = math.inf
    index = -1
    for i,t in enumerate(tree):
        max_val = max_value(t)
        if max_val < value:
            value = max_val
            index = i
    return index, value


def max_action_value(tree):
    if type(tree) is int:
        return None, tree

    value = -1*math.inf
    index = -1
    for i,t in enumerate(tree):
        min_val = min_value(t)
        if min_val > value:
            value = min_val
            index = i
    return index, value


if __name__ == "__main__":
    # game_tree = 3

    # action, value = min_action_value(game_tree)
    # print("Best action if playing min:", action)
    # print("Best guaranteed utility:", value)
    # print()
    # action, value = max_action_value(game_tree)
    # print("Best action if playing max:", action)
    # print("Best guaranteed utility:", value)


    game_tree = [2, [-1, 5], [1, 3], 4]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

