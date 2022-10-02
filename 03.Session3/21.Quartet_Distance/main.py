from utils import newick_tree

with open('ex21.txt', 'r') as f:
    taxa = f.readline().strip().split(" ")
    newick_tree_1 = f.readline().strip().replace(";","")
    newick_tree_2 = f.readline().strip().replace(";","")

print(newick_tree_1)

