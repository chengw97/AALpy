from aalpy.utils import load_automaton_from_file, generate_random_deterministic_automata
from aalpy.SULs import AutomatonSUL
from aalpy.oracles import RandomWalkEqOracle
from aalpy.learning_algs import run_Lstar, run_KV

# load an automaton
automaton = load_automaton_from_file('C:\\Users\\WangC\\Desktop\\projects\\AALpy\\DotModels\\Angluin_Moore.dot', automaton_type='moore')

# or randomly generate one
# automaton = generate_random_deterministic_automata(automaton_type='dfa', num_states=8, 
#                                                     input_alphabet_size=5, output_alphabet_size=2)

# get input alphabet of the automaton
alphabet = automaton.get_input_alphabet()

# loaded or randomly generated automata are considered as BLACK-BOX that is queried
# learning algorithm has no knowledge about its structure
# create a SUL instance for the automaton/system under learning
sul = AutomatonSUL(automaton)

# define the equivalence oracle
eq_oracle = RandomWalkEqOracle(alphabet, sul, num_steps=5000, reset_prob=0.09)

# start learning
# run_KV is for the most part reacquires much fewer interactions with the system under learning
# learned_dfa = run_KV(alphabet, sul, eq_oracle, automaton_type='dfa')
# or run L*
learned_dfa_lstar = run_Lstar(alphabet, sul, eq_oracle, automaton_type='moore', print_level=3)

# save automaton to file and visualize it
# save_automaton_to_file(learned_dfa, path='Learned_Automaton', file_type='dot')
# or
learned_dfa_lstar.save()

# visualize automaton
# visualize_automaton(learned_dfa)
learned_dfa_lstar.visualize()
# or just print its DOT representation
print(learned_dfa_lstar)