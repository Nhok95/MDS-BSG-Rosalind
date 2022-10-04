'''from Bio import Phylo
import networkx as nx
import pylab
import io

with open('ex14.txt', 'r') as f:
    newick_tree = f.read().strip()

tree = Phylo.read(io.StringIO(newick_tree), "newick")
print(tree)
Phylo.draw(tree)

G = Phylo.to_networkx(tree)

nx.draw(G, with_labels=True, font_weight="bold")
pylab.show()
'''

character_table = []
with open('ex14.txt', 'r') as f:
    taxa = f.readline().strip().split(" ")

    for line in f.readlines():
        character_table.append(line.strip())


print(taxa)
print(character_table)

output = []
for character_row in character_table:

    subset1 = set()
    subset2 = set()
    for x in character_row:
        if x == '0':
            subset1.add(taxa[x])
        elif x == '1':
            subset2.add(taxa[x])

    print()

