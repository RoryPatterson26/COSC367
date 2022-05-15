
import math

def euclidean_distance(v1, v2):
    return math.sqrt(sum([(x-y)**2 for x, y in zip(v1, v2)]))


def majority_element(labels):
    highest_frequency = 0
    highest_frequency_label = None
    frequencies = dict()
    for label in labels:
        frequencies[label] = frequencies.get(label, 0) + 1
    for item in frequencies:
        if frequencies[item] > highest_frequency:
            highest_frequency = frequencies[item]
            highest_frequency_label = item
    return highest_frequency_label


def knn_predict(input, examples, distance, combine, k):

    new_examples = []
    for item in examples:
        input_type, output_type = item
        new_examples.append((item, distance(input, input_type)))

    new_examples.sort(key=lambda x: x[1])
    furthest_distance = new_examples[k - 1][1]
    results = [x[1] for x, dist in new_examples if dist <= furthest_distance]

    return combine(results)

def num_parameters(unit_counts):
    parameters = 0
    inputs = unit_counts[0]
    for i in unit_counts[1:]:
        parameters += i*inputs + i
        inputs = i
    return parameters

def num_crossovers(parent_expression1, parent_expression2):
    if type(parent_expression1) == list and type(parent_expression2) == list:
        return len(parent_expression1) * len(parent_expression2)
    elif type(parent_expression1) == list:
        return len(parent_expression1) * len([parent_expression2])
    elif type(parent_expression2) == list:
        return len([parent_expression1]) * len(parent_expression2)
    else:
        return len([parent_expression1]) * len([parent_expression2])

expression1 = ['+', 12, 'x']
expression2 = ['-', 3, 6]
print(num_crossovers(expression1, expression2))
expression1 = 'weight'
expression2 = ['-', 8, 4]
print(num_crossovers(expression1, expression2))