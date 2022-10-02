class Fasta:

    label = None
    dna = ""
    counter = 0

    def __init__(self, label):
        self.label = label

    def add_dna(self, dna_string):
        self.dna += dna_string

    def reverse_complement(self):
        reverse_dna = self.dna[::-1]

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

        return reverse_compl_dna

    def hamming_distance(self, other_dna: str):

        length = len(self.dna)
        if length != len(other_dna):
            return -1

        distance = 0
        for i in range(len(self.dna)):
            if self.dna[i] != other_dna[i]:
                distance += 1

        return distance

fastaDict = {}

with open('rosalind_corr.txt', 'r') as f:
    
    content = f.read().split(">")[1:]

    for element in content:

        subelements = element.split("\n")

        fasta = Fasta(subelements[0])
        for dna_slice in subelements[1:]:
            fasta.add_dna(dna_slice)

        if fasta.reverse_complement() in fastaDict:
            fastaDict[fasta.reverse_complement()].counter += 1
        
        elif fasta.dna in fastaDict:
            fastaDict[fasta.dna].counter += 1
        
        elif fasta.dna not in fastaDict:
            fasta.counter += 1 
            fastaDict[fasta.dna] = fasta
        
        
f = open("output.txt", "w")
        
for base in fastaDict.values():

    for fasta in fastaDict.values():
        if base == fasta:
            pass
        elif base.counter > 1:
            pass
        elif fasta.counter > 1:

            if base.hamming_distance(fasta.dna) == 1:
                f.write(f"{base.dna}->{fasta.dna}\n")

            elif base.hamming_distance(fasta.reverse_complement()) == 1:
                f.write(f"{base.dna}->{fasta.reverse_complement()}\n")

f.close()