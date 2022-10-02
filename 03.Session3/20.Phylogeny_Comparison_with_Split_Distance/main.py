with open('ex20.txt', 'r') as f:
    taxa = [line.strip() for line in f.readline().split(" ")]
    newick1 = f.readline()
    newick2 = f.readline()

print(taxa)


