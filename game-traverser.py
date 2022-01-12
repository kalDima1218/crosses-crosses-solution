from math import log10
n = 12
cases = {1:[[0, [0, 0]]]}
a = [-1 for i in range(n + 1)]
a[0] = 0
a[1] = 1

def dfs(v):
	if a[v] != -1: return a[v]
	b = [[dfs(v - 2), [0, v - 2]]]
	for i in range(2, v//2 + 1 + v%2):
		b.append([dfs(i - 2) ^ dfs(v - i - 1), [i - 2, v - i - 1]])
	a[v] = 0
	b.sort()
	cases[v] = b
	i = 0
	while i in range(len(b)):
		if a[v] == b[i][0]:
			a[v]+=1
			i = -1
		i+=1
	return a[v]

dfs(n)
#print(a[1:], end="\n\n")
for i in range(1, n + 1):
	if i != n - 1:
		print(i, ": ", cases[i][0], sep="", end="\n")
		for j in cases[i][1:]:
			print((2 + int(log10(i))) * " ", j)
		print()
