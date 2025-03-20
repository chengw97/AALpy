from aalpy import generate_random_deterministic_automata

import random
random.seed(1)

from itertools import combinations

automaton_type = 'moore'
num_states = 4
model = generate_random_deterministic_automata(automaton_type, 4, 2, 2, ensure_minimality=False)

model.visualize(path="LearnedModel_moore37")

def get_prefixes(model):
    # returns a dictionary where each state is mapped to a prefix
    # eg. {'s0': (), 's1' : (i1,i2),}
    # print the results

    prefix_map = {}

    model.compute_prefixes()
    
    for s in model.states:
        prefix_map[s.state_id] = s.prefix
    
    for k, v in prefix_map.items():
        print(f'{k}: {v}')
    
    return prefix_map

def is_minimal(model):
    # check if the model is minimal, by using AALpy's inbuild functions
    # if model is not minimal, minimize it using AALpy's inbuild functions
    
    if not model.is_minimal():
        model.minimize()
        print('Model was not minimal. Model is now minimized.')
    else:
        print('Model is minimal')
    
    return is_minimal

def random_sequences(model):
    # given a model, get its input alphabet and execute 10 randomly generated sequances on it
    # each sequence is of random length in range [2-10]
    # print only the last output of the sequence
    input_alphabet = model.get_input_alphabet()
    print(input_alphabet)

    states = model.states

    for _ in range(10):
        test_sequence = random.choices(input_alphabet, k=random.randint(2,10))
        last_output = model.execute_sequence(model.initial_state, test_sequence)[-1]
        print(last_output)

def compute_characterization_set(model):
    # figure out how to compute a characterization set (in build function)
    # explain in a comment what a characterization set is
    # use characterization set to distinguish all pairs of states

    # a set of sequences that can distinguish all states in the automation
    char_set =  model.compute_characterization_set()

    for s1, s2 in list(combinations(model.states, 2)):

        diff_found = False

        for test_sequence in char_set:
            last_out_s1 = model.execute_sequence(s1, test_sequence)
            last_out_s2 = model.execute_sequence(s2, test_sequence)

            if last_out_s1 != last_out_s2:
                print(s1.state_id, s2.state_id, test_sequence)
                diff_found = True
                break
        
        if not diff_found:
            print(f'States {s1.state_id} and {s2.state_id} are not distinguishable.')
    return

def distinguish_states(s1, s2):
    # write a function that returns a distinguishing sequance between two states, or if it cannot be found, return None
    input_alphabet = model.get_input_alphabet()
    dist_seq = model.find_distinguishing_seq(s1, s2, input_alphabet)
    
    return dist_seq


if __name__ == '__main__':
    get_prefixes(model)
    is_minimal(model)
    random_sequences(model)
    compute_characterization_set(model)

    states = model.states
    for s1, s2 in list(combinations(model.states, 2)):
        dist_seq = distinguish_states(s1, s2)
        print(f"distinguishing seq of {s1.state_id} between {s2.state_id} is {dist_seq}")
