'''
A quartet AB|CD is consistent with a binary tree T if the quartet can be inferred from one of the 
splits of T (see “Quartets” for a description of inferring quartets from splits).

Let q(T) denote the total number of quartets that are consistent with T.

Given: A positive integer n (4≤n≤5000), followed by an unrooted binary tree T in Newick format on 
n taxa.

Return: The value of q(T) modulo 1,000,000.
'''

from Bio import Phylo
import networkx as nx
import io

with open('ex19.txt', 'r') as f:
    n = int(f.readline().strip())
    newick_tree = f.readline().strip()

tree = Phylo.read(io.StringIO(newick_tree), "newick")

Phylo.draw(tree)

#Newick(newick_tree)