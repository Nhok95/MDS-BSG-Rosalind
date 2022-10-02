'''
Given a collection of n taxa, any subset S of these taxa can be seen as encoding a character that divides the taxa 
into the sets S and Sc; we can represent the character by S|Sc, which is called a split. Alternately, the character 
can be represented by a character array A of length n for which A[j]=1 if the jth taxon belongs to S and A[j]=0 if 
the jth taxon belongs to Sc (recall the "ON"/"OFF" analogy from “Counting Subsets”).

At the same time, observe that the removal of an edge from an unrooted binary tree produces two separate trees, each 
one containing a subset of the original taxa. So each edge may also be encoded by a split S|Sc.

A trivial character isolates a single taxon into a group of its own. The corresponding split S|Sc must be such that S
or Sc contains only one element; the edge encoded by this split must be incident to a leaf of the unrooted binary tree, 
and the array for the character contains exactly one 0 or exactly one 1. Trivial characters are of no phylogenetic 
interest because they fail to provide us with information regarding the relationships of taxa to each other. All other 
characters are called nontrivial characters (and the associated splits are called nontrivial splits).

A character table is a matrix C in which each row represents the array notation for a nontrivial character. That is, 
entry Ci,j denotes the "ON"/"OFF" position of the ith character with respect to the jth taxon.

Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. The columns of the character table should 
encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any 
given character, the particular subset of taxa to which 1s are assigned is arbitrary.
'''

from Bio import Phylo
import networkx as nx
import pylab
import io

with open('ex12.txt', 'r') as f:
    newick_tree = f.read().strip()

taxa = newick_tree.replace(';','').replace('(','').replace(')','').replace(',', ' ').split(" ")
taxa.sort()

print(taxa)


tree = Phylo.read(io.StringIO(newick_tree), "newick")
G = Phylo.to_networkx(tree)

f = open("output.txt", "w")

for e in G.edges():
    '''
    If node do not have name is not a leaf, we need both nodes of the edge to be Claudes
    (internal nodes) to produce 2 subtrees. We know that if we remove only 1 edge from a tree 
    we generate 2 subtrees.
    '''
    C = [1]*len(taxa)
    
    if (str(e[0].name) == 'None' and str(e[1].name) == 'None'):
        print(f"edge {e}")
        aux = G.copy()
        aux.remove_edge(e[0], e[1])

        components = [G.subgraph(c).copy() for c in nx.connected_components(aux)]
        print(f"component 1: {components[0]}")
        print(f"component 2: {components[1]}")

        for node in components[0].nodes():
            if ((str(node.name)) != 'None'):
                index = taxa.index(node.name)
                print(f"    node: {node.name}; index: {index}")
                C[index] = 0 # belongs to subset 0

        #nx.draw(aux, with_labels=True, font_weight="bold")
        #pylab.show()
        result = ''.join(map(str, C))

        print(result)
        f.write(f"{result}\n")

f.close()


