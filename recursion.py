import numpy as np
import itertools
from itertools import combinations_with_replacement

# redo everything with prob = 0 if it's not in the list. rewrite the F() method. the logic on final method is right but needs to be reworked.
# write the code for graph builder
# test it 
# make everything in numpy


class Vertex:
    def __init__(self, delta, list, children):
        self.list = list 
        self.children = children
        self.delta = delta # should be the same as len(self.children)
        self.type = (delta, self.list)

        # self.lists = [] # list of possible probability vectors, empty to initial


v = Vertex([1,2])

full_list 



def p(v, h):
    prob = 1
    L = v.list

    if h not in L:
        return 0

    for vi in v.children:
        prob *= (1 - p(vi, h))
    
    Z = 0

    for g in L:
        prob_g = 1
        for vi in v.children:
            prob_g *= (1 - p(vi, g))
        Z += prob_g


def get_x(v):
    x = []

    for vi in v.children:
        x_vi = []
        for h in v.list:
            x_vi_h = p(vi, h)
            x_vi.append(x_vi_h)
        x.append(x_vi)
    return x


# v fixed
def F(x):
    # x is a list of list, each list is a probability vector

    probs = []
    for h in v.list:
        p = 1
        for 

         


    # probs = []
    # for h in v.list:
    #     probs.append(p(v, h))
    # return probs


    
    
    # for each h in L(v), let's calculate x(v_i, h) for all children i of v 
    # feed this into p(v, h) to get back F(x)



# remove all the colored nodes and subtrees (pruning)
# do we need to perform the algorithm on the removed nodes and subtrees?

# initialize S_1

num_iter = 100

# here the iterations over all possible types of delta and L are hard coded
possible_deltas = range(2)
possible_lists = [[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]]
prod = list(itertools.product(possible_deltas, possible_lists))

# adding v as an argument

def S(delta, L, v, r):
    num_colors = len(L)
    lst = []
    if delta == 0:
        distr = []
        for i in range(num_colors):
            distr.append(1/num_colors)
            lst.append(distr)
        return lst
    
    for k in range(r-1): # iteration of recursion
        num_children = len(v.children)

        # confirm comb_with_replace gives you what you want
        combs = list(combinations_with_replacement(prod, num_children))

        for comb in combs:

            S_sets = []

            for tup in comb:
                S_tup = S(tup[0], tup[1], v, r-1)
                S_sets.append(S_tup)
            
            # get all combos x(v1, -), x(v2, -) from the sets S_tup

            if len(S_sets) == 1:
                for x_i in S_sets[0]:
                    p_v_xi = F(x_i)
                    lst.append(p_v_xi)


            elif len(S_sets) == 2: 
                # make sure everything is lists and not tuples
                # make sure this product behaves how you want
                prod = list(itertools.product(S_sets[0], S_sets[1]))
                for x_i in prod:
                    p_v_xi = F(x_i)
                    lst.append(p_v_xi)
        
    return lst

            

    


