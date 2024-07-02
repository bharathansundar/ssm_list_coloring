import numpy as np
import itertools
from itertools import combinations_with_replacement
import graph_generator
from graph_generator import TreeNode

#TODO: implement graph/fixing colors/vertices with built in list/and children, tree as a function of depth
#Implement auto pruning of subtrees and colored leaves
#Write out small test cases and make sure S(-) behaves as expected. 

"""
Graph construction
"""

full_colors = ['R','G','B','Y'] 

depth = 3
v = TreeNode(depth, full_colors)
v.add_children(depth, full_colors)

print(v.colors)


"""
Algorithm
"""

def p(v, h):
    L = v.colors

    if h not in L:
        return 0 # keep zero probabilities so all prob. vectors have the same length
    
    p_h = np.prod([1 - p(vi, h) for vi in v.children])
    
    Z = 0

    for g in L:
        prob_g = np.prod([1 - p(vi, g)] for vi in v.children)
        Z += prob_g
    
    if Z == 0: 
        raise Exception("Z is zero, try a valid distribution")

    return p_h/Z

def p(v):
    lst = np.array([p(v,h) for h in full_colors])
    return lst


def F(x):

    # given x = [probability vectors] (distributions on the children), return p_h for all h and put it in one vector
    delt = len(x)
    Z = 0
    p_x = []

    # test this
    for j in range(len(full_colors)):
        # take the product over however many delta there are, fixing the color index j
        p = 1
        for i in range(delt):
            p *= (1-x[i][j])
        Z += p
        p_x.append(p)

    return np.array(p_x / Z)


possible_deltas = range(2)
possible_lists = [[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]]
prod = list(itertools.product(possible_deltas, possible_lists))

num_iter = 100


def S(delta, L, v, r):
    num_colors = len(L)
    lst = []
    if delta == 0:
        distr = []
        for i in range(num_colors):
            distr.append(1/num_colors) # initialize to the uniform when delta = 0
            lst.append(distr)
        return lst
    
    num_children = len(v.children)
    combs = list(combinations_with_replacement(prod, num_children))

    for k in range(r-1):
        final_lst = [] # rewrite the list of probabilities at each iteration, calculating based on S(-, r-1)
        for comb in combs:
            sets = []
            for tup in comb:
                s = S(tup[0], tup[1], v, r - 1)
                sets.append(s)

            if len(sets) == 1: # case where v has a single child
                possible_probs = sets[0]

                for prob in possible_probs:
                    final_lst.append(F(prob))

            elif len(sets) == 2: # case where v has 2 children
                possible_prob_combos = list(itertools.product(sets[0], sets[1]))

                for prob in possible_prob_combos:
                    final_lst.append(F(prob))
        
    return final_lst


        







    




