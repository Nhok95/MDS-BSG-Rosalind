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
    
    def overlap_and_merge(self, other: object, k: int) -> bool:
        if self.__eq__(other):
            return False
        else:
            suffix_other = other.dna[k:]
            preffix_other = other.dna[:len(other.dna)-k]

            if self.dna.startswith(suffix_other):
                self.dna = other.dna[:k] + self.dna
                return True

            elif self.dna.endswith(preffix_other):
                self.dna += other.dna[len(other.dna)-k:]
                return True


fastaList = []

with open('rosalind_long.txt', 'r') as f:
    
    content = f.read().split(">")[1:]
    
    for element in content:

        subelements = element.split("\n")

        fasta = Fasta(subelements[0])
        for dna in subelements[1:]:
            fasta.add_dna(dna)

        fastaList.append(fasta)


fasta_superstr = Fasta("Fasta_Superstring")
fasta_superstr.add_dna(fasta.dna)

fastaStack = [x for x in fastaList if x != fasta]

while fastaStack:

    other = fastaStack.pop()
    fasta_integrated = False

    for value in range(len(other.dna)//2):


        if (fasta_superstr.overlap_and_merge(other, value)):
            fasta_integrated = True
            break

    if (not fasta_integrated):
        fastaStack.insert(0, other)


f = open("output.txt", "w")
f.write(f'{fasta_superstr.dna}\n')
f.close()
