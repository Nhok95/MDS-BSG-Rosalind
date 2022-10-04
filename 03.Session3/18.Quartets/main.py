with open('rosalind_qrt.txt', 'r') as f: #3367
    lines = f.readlines()

taxa = lines[0].strip().split(' ')  # taxa

#print(f"taxa: {taxa}")

quartets = set()

for line in lines[1:]:
    
    line = line.strip()
    C = []
    D = []

    #print(f"\n    line: {line}\n")

    for i in range(len(line)):
        if line[i] == '1':
            C.append(taxa[i])
        elif line[i] == '0':
            D.append(taxa[i])

    '''
    C = [1,3,5]
    D = [2,4]
    '''
    #print(f"    C: {C}")
    #print(f"    D: {D}")

    if len(C) >= 2 and len(D) >= 2: # Valid partial split

        for i in range(len(C)-1):
            for j in range(i+1, len(C)):
                for k in range(len(D)-1):
                    for l in range(k+1, len(D)):
                        #print(f"i: {i}; j: {j}; k: {k}; l: {l}")
                        
                        A = (C[i], C[j])
                        B = (D[k], D[l])
                        
                        
                        #print (f"   A: {A}")
                        #print (f"   B: {B}")

                        quartets.add((A, B) if A[0] < B[0] else (B, A))


#print("----") 
f = open("output.txt", "w")
for quartet in quartets:
    A, B = quartet
    result = f"{{{A[0]}, {A[1]}}} {{{B[0]}, {B[1]}}}"
    #print(result)
    f.write(f"{result}\n")

f.close()
