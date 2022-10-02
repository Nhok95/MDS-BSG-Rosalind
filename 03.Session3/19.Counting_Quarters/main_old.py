with open('rosalind_cntq.txt', 'r') as f:
    n = int(f.readline().strip())
    newick = f.readline()

memo = [1] + [None for _ in range(n)]

f = open("output.txt", "w")

for i in range(1, n+1):
    memo[i] = i * memo[i-1]

print(memo)

qt = int(memo[n]/(memo[n-4]*memo[4]))

f.write(f"{qt%1000000}\n")

f.close()