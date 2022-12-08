lines = []
with open('1-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
lines.append('')
print(lines)

cal_list = []
cal_curr = 0
for line in lines:
	if line == '':
		cal_list.append(cal_curr)
		cal_curr = 0
	else:
		cal_curr += int(line)

total = 0
maxi = max(cal_list)
total += maxi
cal_list.remove(maxi)
maxi = max(cal_list)
total += maxi
cal_list.remove(maxi)
maxi = max(cal_list)
total += maxi
cal_list.remove(maxi)
print(total)
