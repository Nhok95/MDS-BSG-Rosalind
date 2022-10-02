
with open('rosalind_dna.txt', 'r') as f:
    dna_string = f.readline()

counter_a = 0
counter_c = 0
counter_g = 0
counter_t = 0

for x in dna_string:
    if (x == 'A'):
        counter_a += 1

    if (x == 'C'):
        counter_c += 1

    if (x == 'G'):
        counter_g += 1

    if (x == 'T'):
        counter_t += 1

f = open("output.txt", "w")
f.write(f"{counter_a} {counter_c} {counter_g} {counter_t}\n")
f.close()