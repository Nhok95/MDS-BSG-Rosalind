'''
Two unrooted binary trees T1 and T2 having the same n labeled leaves are considered to be 
equivalent if there is some assignment of labels to the internal nodes of T1 and T2 so 
that the adjacency lists of the two trees coincide. As a result, note that T1 and T2 must 
have the same splits; conversely, if the two trees do not have the same splits, then they 
are considered distinct.

Let b(n) denote the total number of distinct unrooted binary trees having n labeled leaves.

Given: A positive integer n (n≤1000).

Return: The value of b(n) modulo 1,000,000.
'''

with open('rosalind_cunr.txt', 'r') as f:
    n = int(f.readline())


def counting_unrooted_binary_trees(n, method="factorial_method"):

    if (method == "factorial_method"):
        return counting_by_adding(n)

    elif (method == "neighbor_joining"):
        return neighbor_joining_for_counting(n)

    else:
        return -1
'''
Using Neighbor Joining
Source: https://pages.cs.wisc.edu/~aasmith/biolec/trees.html
#Not implemented yet
* n: number of labeled leaves
'''
def neighbor_joining_for_counting(n):
    return -1

'''
Adding new branches
Source: http://www.cs.cornell.edu/courses/cs426/2003fa/Week10%20Phylogenetic%20Trees.pdf
-> Let U(n) be the number of unrooted trees with n labeled leaves
-> Given an unrooted tree with n leaves, an extra leaf can be
   added on any branch to make a tree with (n+1) leaves
-> n leaves
    => 2n-3 possible branches
    => U(n+1) = (2n-3)U(n)
    => U(n) = (2n-5)!!
* n: number of labeled leaves
'''
def counting_by_adding(n):
    value = (2*n)-5 # This value is always odd since 2*n is pair and -5 makes it odd
    if (n == 3): # base case (minimum # of labeled leaves to have an unrooted tree)
        return 1
    if (n > 3):
        return counting_by_adding(n-1) * value

bn = counting_unrooted_binary_trees(n)

result = bn % 1000000

f = open("output.txt", "w")
f.write(f"{result}\n")
f.close()