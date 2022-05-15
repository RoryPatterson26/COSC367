import itertools

def calc_probability(is_positive, positive_probability):
    if is_positive:
        return positive_probability
    return 1 - positive_probability

def if_dependencies(node, network, assignment):
    temp_probability = -1
    parents = network[node]["Parents"]
    target_key = tuple([assignment[x] for x in parents])
    temp_probability = calc_probability(assignment[node], network[node]["CPT"][target_key])
    return temp_probability

def joint_prob(network, assignment):
    probability = 1
    for node, is_positive in assignment.items():
        dependencies = network[node]["Parents"]
        if dependencies:
            probability = probability * if_dependencies(node, network, assignment)
        else:
            positive_probability = list(network[node]["CPT"].values())[0]
            probability = probability * calc_probability(is_positive, positive_probability)            
    return probability


def query(network, query_var, evidence):
    probabilities = []
    for is_true in [True, False]:
        hidden_vars = network.keys() - evidence.keys() - {query_var}
        probability = 0
        for value in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var: val for var, val in zip(hidden_vars, value)}
            hidden_assignments[query_var] = is_true
            for i, item in evidence.items():
                hidden_assignments[i] = item
            probability += joint_prob(network, hidden_assignments)
        probabilities.append(probability)
    return {True: probabilities[0]/sum(probabilities), False: probabilities[1]/sum(probabilities)}


network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))