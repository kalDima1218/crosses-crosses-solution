n = 25
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
field = list(map(int, input("Состояние поля: ").split(" ")))#4 12 1 7 15 2 5 20
xf = []
for i in range(len(field)):
	xf1 = 0
	for j in range(len(field)):
		if j != i:
			xf1^=a[field[j]]
	xf.append(xf1)
for i in range(len(field)):
	for j in cases[field[i]]:
		if j[0] ^ xf[i] == 0:
			for k in range(len(field)):
				if k == i:
					print(j[1], end=" ")
				else:
					print(field[k], end=" ")
			print()
