class Fasta:

    label = None
    dna = ""

    def __init__(self, label):
        self.label = label

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Fasta):
            return self.dna == other.dna
        return False

    def __str__(self) -> str:
        return f"Fasta {self.label}: {self.dna}"

    def add_dna(self, dna_string):
        self.dna += dna_string
    
    def overlap(self, other: object, k: int) -> bool:
        if self.__eq__(other):
            return False
        else:
            length = len(self.dna)
            suffix = self.dna[length-k: length]

            return suffix == other.dna[0:k]


fastaList = []

with open('rosalind_grph.txt', 'r') as f:
    
    content = f.read().split(">")[1:]
    
    for element in content:

        subelements = element.split("\n")

        fasta = Fasta(subelements[0])
        for dna in subelements[1:]:
            fasta.add_dna(dna)

        fastaList.append(fasta)

f = open("output.txt", "w")

for fasta in fastaList:
    for fasta_other in fastaList:#for j in range(i+1, len(fastaList)):

        if (fasta.overlap(fasta_other, 3)):
            f.write(f'{fasta.label} {fasta_other.label}\n')

f.close()
        
