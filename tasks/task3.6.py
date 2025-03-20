from aalpy.utils import generate_random_deterministic_automata, generate_random_mealy_machine, generate_random_moore_machine

from random import seed
seed(3)

# dfa
random_dfa = generate_random_deterministic_automata(automaton_type='dfa', num_states=3, 
                                                    input_alphabet_size=2, output_alphabet_size=2)
random_dfa.visualize(path="LearnedModel_dfa")

'''
2. prefix
s1: epsilon
s2: i1
s3: i1, i1

state  input  next_state
s1     i1     s2
s1     i2     s2
s2     i1     s3
s2     i2     s1
s3     i1     s3
s3     i2     s2

3. distinguishment
s1,s2: i1(F,T);i1,i2(FF,TF)
s1,s3: i1(F,T);i1,i2(FF,TF)
s2,s3: i2,i1(FF,FT);i2,i1,i2(FFF,FTF)

4. formalism
<Q, I, delta, q0, F>
Q: {s1, s2, s3}
I: {i1, i2}

delta:
d(s1, i1)=s2
d(s1, i2)=s2
d(s2, i1)=s3
d(s2, i2)=s1
d(s3, i1)=s3
d(s3, i2)=s2

q0: s1
F: s3
'''

# mealy
input_alphabet = ['i0', 'i1']
output_alphabet = ['a', 'b']

random_mealy = generate_random_mealy_machine(num_states=3, input_alphabet=input_alphabet, output_alphabet=output_alphabet,
                                  compute_prefixes=False, ensure_minimality=True)
random_mealy.visualize(path="LearnedModel_mealy")

'''
2. prefix
s1: epsilon
s2: i0, i1
s2: i0

3.  
s1, s2: i0(b,a); i0,i1(bb,ab)
s1, s3: i1(a,b); i1,i1(aa,ba)
s2, s3: i0(a,b); i0,i1(ab,ba)

4. formalism
<Q, I, O, delta, lambda, q0>
Q: {s1, s2, s3}
I: {i0, i1}
O: {a, b}

state  input  next_state, output
s1     i1     s1,a
s1     i0     s3,b
s3     i0     s1,b
s3     i1     s2,b
s2     i0     s3,a
s2     i1     s2,a

delta:
d(s1, i1)=s1
d(s1, i0)=s3
d(s3, i0)=s1
d(s3, i1)=s2
d(s2, i0)=s3
d(s2, i1)=s2

lambda:
l(s1, i1)=a
l(s1, i0)=b
l(s3, i0)=b
l(s3, i1)=b
l(s2, i0)=a
l(s2, i1)=a

q0: s1

'''

# moore
random_moore = generate_random_moore_machine(num_states=3, input_alphabet=input_alphabet, output_alphabet=output_alphabet,
                                  compute_prefixes=False, ensure_minimality=True)
random_moore.visualize(path="LearnedModel_moore")

'''
2. prefix
s1: epsilon
s2: i1, i0
s3: i1

3. 
s1,s2: i1(a,b); i1,i0(aa,bb)
s1,s3: i0(b,a); i0,i1(ba,ab)
s2,s3: i1(b,a); i1,i1(ba,ab)

4. formalism
<Q, I, O, delta, lambda, q0>
Q: {s1, s2, s3}
I: {i0, i1}
O: {a, b}

delta: 
d(s1, i0)=s1
d(s1, i1)=s3
d(s3, i0)=s2
d(s3, i1)=s2
d(s2, i0)=s1
d(s2, i1)=s1

lambda:
l(s1)=b
l(s1)=a
l(s3)=a
l(s3)=a
l(s2)=b
l(s2)=b

q0: s1

What happens if there exist no distinguishing sequence between 2 states.
two same states can merge.

'''

'''
digraph learnedModel {
s1 [label="s1|o1", shape=record, style=rounded];
s2 [label="s2|o2", shape=record, style=rounded];
s3 [label="s3|o1", shape=record, style=rounded];
s4 [label="s4|o2", shape=record, style=rounded];
s1 -> s2 [label="i1"];
s1 -> s3 [label="i2"];
s2 -> s3 [label="i1"];
s2 -> s4 [label="i2"];
s3 -> s2 [label="i1"];
s3 -> s3 [label="i2"];
s4 -> s2 [label="i1"];
s4 -> s1 [label="i2"];
__start0 [shape=none, label=""];
__start0 -> s1 [label=""];
}
'''

'''
s1,s2: i1(o2,o1)
s1,s3: no
s1,s4: no
s2,s3: i1(o1,o2)
s2,s4: i1(o1,o2)
s3,s4: no


'''


