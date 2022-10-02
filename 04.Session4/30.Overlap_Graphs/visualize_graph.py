import networkx as nx
import matplotlib.pyplot as plt

with open('output.txt', 'r') as f:
    line = f.readline().split(" ")

    G = nx.read_edgelist(f, nodetype=str, create_using=nx.DiGraph)

    nx.draw(G, with_labels=True, font_weight="bold")
    plt.show()