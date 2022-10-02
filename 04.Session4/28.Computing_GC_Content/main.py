class Fasta:

    label = None
    dna = ""
    gc = None

    def __init__(self, label):
        self.label = label[1:]

    def __str__(self):
        return f"Fasta {self.label}: {self.dna}; gc: {str(self.gc)}"

    def add_dna(self, dna_string):
        self.dna += dna_string

    def calculate_gc_content(self):
        gc = (self.dna.count('C') + self.dna.count('G'))*100 / len(self.dna) 
        self.gc = round(gc, 5)

fasta_dict = {}

with open('rosalind_gc.txt', 'r') as f:
    lines = f.readlines()

    label = ""
    for line in lines:
        if line[0] == '>':
            label = line.strip()
            fasta_dict[label] = Fasta(label)
        else:
            fasta_dict[label].add_dna(line.strip())


max_label = ""
max_value = 0
for _, fasta in fasta_dict.items():
    
    fasta.calculate_gc_content()
    
    if fasta.gc > max_value:
        max_value = fasta.gc
        max_label = fasta.label


f = open("output.txt", "w")
f.write(f"{max_label}\n{max_value}")
f.close()
