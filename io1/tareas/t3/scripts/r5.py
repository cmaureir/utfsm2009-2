# Restriccion 5
r = ""
c1 = (1,2,3)
c2 = (4,5,6)
c3 = (7,8,9)
for j in range(1, 6):
	r = ""
	for i in c1:
		for k in range(1,5):
			r += "X" + str(i) + str(j) + str(k) + " + ";
	print r + '< 1'

for j in range(1, 6):
	r = ""
	for i in c2:
		for k in range(1,5):
			r += "X" + str(i) + str(j) + str(k) + " + ";
	print r + '< 1'

for j in range(1, 6):
	r = ""
	for i in c3:
		for k in range(1,5):
			r += "X" + str(i) + str(j) + str(k) + " + ";
	print r + '< 1'
