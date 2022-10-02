with open('rosalind_rna.txt', 'r') as f:
    dna_string = f.readline()

rna_string = dna_string.replace('T', 'U')

f = open("output.txt", "w")
f.write(f"{rna_string}\n")
f.close()