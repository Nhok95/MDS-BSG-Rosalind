'''
Newick format is a way of representing trees even more concisely than using an adjacency list, 
especially when dealing with trees whose internal nodes have not been labeled.

First, consider the case of a rooted tree T. A collection of leaves v1,v2,…,vn of T are 
neighbors if they are all adjacent to some internal node u. Newick format for T is obtained by
iterating the following key step: delete all the edges {vi,u} from T and label u with 
(v1,v2,…,vn)u. This process is repeated all the way to the root, at which point a semicolon
signals the end of the tree.

A number of variations of Newick format exist. First, if a node is not labeled in T, then we 
simply leave blank the space occupied by the node. In the key step, we can write (v1,v2,…,vn) 
in place of (v1,v2,…,vn)u if the vi are labeled; if none of the nodes are labeled, we can write 
(,,…,).

A second variation of Newick format occurs when T is unrooted, in which case we simply select 
any internal node to serve as the root of T. A particularly peculiar case of Newick format arises
when we choose a leaf to serve as the root.

Note that there will be a large number of different ways to represent T in Newick format;

Given: A collection of n trees (n≤40) in Newick format, with each tree containing at most 200 nodes; 
each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n positive integers, for which the kth integer represents the distance between 
xk and yk in Tk.
'''
from Bio import Phylo
import io

with open('rosalind_nwck.txt', 'r') as f:
    trees = [i.split('\n') for i in f.read().strip().split('\n\n')]

f = open("output.txt", "w")

for newick_tree, pairs  in trees:

    x, y = pairs.split(" ")
    tree = Phylo.read(io.StringIO(newick_tree), "newick")
    
    #Phylo.draw(tree)
    #print(tree)

    clades = tree.find_clades()
    for clade in clades:
        clade.branch_length = 1  
    
    f.write(f"{tree.distance(x,y)} ")

f.write("\n")
f.close()