lines = []
with open('3-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
print(lines)


priorities = {}
for i in range(26):
	priorities[chr(i+65)] = i + 27
	priorities[chr(i+97)] = i + 1


score = 0
for i in range(0, len(lines), 3):
	a = set(c for c in lines[i])
	b = set(c for c in lines[i+1])
	c = set(c for c in lines[i+2])
	score += priorities[list(a.intersection(b, c))[0]]

print(score)

