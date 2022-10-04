from operator import index

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

dna_list = []
with open('rosalind_cset.txt', 'r') as f:
    
    for line in f.readlines():
        dna_list.append(line.strip())

#print(dna_list)

taxa = [x for x in range(len(dna_list[0]))]
#print(taxa)

conflict = set()

#print("----")

for x in range(len(dna_list)):

    A1 = []
    A2 = []

    base = dna_list[x]

    for i in range(len(base)):
        if base[i] == '1':
            A1.append(taxa[i])
        elif base[i] == '0':
            A2.append(taxa[i])

    #print(A1)
    #print(A2)

    for y in range(len(dna_list)):

        if x == y:
            pass
        else:
            B1 = []
            B2 = []
            dna = dna_list[y]

            for i in range(len(dna)):
                if dna[i] == '1':
                    B1.append(taxa[i])
                elif dna[i] == '0':
                    B2.append(taxa[i])
            
            l1 = len(intersection(A1,B1))
            l2 = len(intersection(A1,B2))
            l3 = len(intersection(A2,B1))
            l4 = len(intersection(A2,B2))

            if l1 == 0 or l2 == 0 or l3 == 0 or l4 == 0:
                pass
            else:
                #print(B1)
                #print(B2)

                pair = (x, y) if x > y else (y,x)

                conflict.add(pair)

                #print(l1,l2,l3,l4, f"conflict {pair}")

            

            #print()

    #print("----")

index = conflict.pop()[0]
del dna_list[index]

f = open("output.txt", "w")
for dna in dna_list:

    f.write(f"{dna}\n")

f.close()
