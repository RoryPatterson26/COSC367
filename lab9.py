import csv
def posterior(prior, likelihood, observation):
    vals = []
    for i, is_true in enumerate([True, False]):
        result = abs(prior - i)
        for j, obs in enumerate(observation):
            observation_likelihood = likelihood[j]
            if obs:
                result *= observation_likelihood[is_true]
            else:
                result *= 1 - observation_likelihood[is_true]
        vals.append(result)
    return vals[0]/sum(vals)


def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 

    true = 0
    false = 0
    for index, line in enumerate(training_examples):
        if index != 0:
            if int(line[-1]):
                true += 1
            else:
                false += 1
    return (true + pseudo_count) / (true + false + pseudo_count * 2)

def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file: 
        training_examples = [tuple(row) for row in csv.reader(in_file)] 

    likelihood = [[] for x in range(len(training_examples[0]) - 1)]

    true = 0
    false = 0
    for index, line in enumerate(training_examples):
        if index != 0: 
            for item_index, item in enumerate(line):
                if item_index == len(line) - 1:
                    if int(item):
                        true += 1
                    else:
                        false += 1
        
                elif int(item): 
                    spam_value = int(line[-1])
                    likelihood[item_index].append(spam_value)

    for i in range(len(likelihood)):
        result = [0, 0]
        for value in likelihood[i]:
            result[value] += 1
        result[False] = (result[False] + pseudo_count) / (false + pseudo_count * 2)
        result[True] = (result[True] + pseudo_count) / (true + pseudo_count * 2)
        likelihood[i] = result
    return likelihood


def nb_classify(prior, likelihood, input_vector): 
    probability = posterior(prior, likelihood, input_vector)
    if probability <= 0.5:
        return "Not Spam", 1 - probability
    else:
        return "Spam", probability


prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))
    