with open('rosalind_hamm.txt', 'r') as f:
    dna1 = f.readline()
    dna2 = f.readline()

def hamming_distance(dna1, dna2):

    distance = 0
    
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1

    return distance

f = open("output.txt", "w")
f.write(f"{str(hamming_distance(dna1, dna2))}\n")
f.close()