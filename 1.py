lines = []
with open('1-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
lines.append('')
print(lines)

cal_max = 0
cal_curr = 0
for line in lines:
	if line == '':
		cal_max = max(cal_curr, cal_max)
		cal_curr = 0
	else:
		cal_curr += int(line)

print(cal_max)
