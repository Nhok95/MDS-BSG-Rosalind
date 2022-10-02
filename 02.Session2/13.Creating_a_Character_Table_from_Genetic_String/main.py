
dna_strings = []
with open('ex13.txt', 'r') as f:
    for line in f:
        dna_strings.append(line.strip())

f = open("output.txt", "w")

base = dna_strings[0]
for i in range(len(base)):
    cnt_0 = 0
    cnt_1 = 0
    row = ''
    for seq in dna_strings:
        
        if base[i] == seq[i]:
            row += '1'
            cnt_1 += 1
        else:
            row += '0'
            cnt_0 += 1
    if cnt_1>1 and cnt_0>1:
        f.write(f"{row}\n")

f.close()