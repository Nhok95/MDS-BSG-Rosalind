with open('rosalind_revc.txt', 'r') as f:
    dna_string = f.readline()

reverse_dna = dna_string[::-1]

reverse_compl_dna = ""
for s in reverse_dna:
    if s == 'A':
        reverse_compl_dna += 'T'

    elif s == 'T':
        reverse_compl_dna += 'A'
        
    elif s == 'G':
        reverse_compl_dna += 'C'

    elif s == 'C':
        reverse_compl_dna += 'G'

f = open("output.txt", "w")
f.write(f"{reverse_compl_dna}\n")
f.close()