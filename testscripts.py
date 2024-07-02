import itertools
from itertools import combinations_with_replacement
import numpy as np

possible_deltas = range(2)
possible_lists = [[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]]

lst = [1,2,3,4,5,6,7,8]

prod = list(itertools.product(possible_deltas, possible_lists))

combs = list(combinations_with_replacement(prod, 2))

ar = np.array([7*i for i in range(9)])

l1 = [[1,2,3],[4,5]]
l2 = [[6],[7,8],[9]]
sets = [l1,l2]

for i in range(7):
    lst = []
    lst.append(i)

print(lst)



# order should not matter but we can double count anyways (e.g. [(d1, L1), (d2, L2)] vs [(d2, L2), (d1, L1)])
# so if v has 1 child:
# we get all possible tuples (del1, L1). For each of these x's in S(del1, L1, r-1), compute F(x) and add that to final list
# if v has two children: 
# get all possible combos (del1, L1), (del2, L2). compute S(del1, L1, r-1) = s1 and S(del2, L2, r-1) = s2
# Then make all possible vectors x = (x1, x2) where x1 in S1, x2 in S2 and compute F(x). Add F(x) to the final list.

