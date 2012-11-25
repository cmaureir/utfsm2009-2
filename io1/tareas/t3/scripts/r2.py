# Restriccion 2
r1 = "";
r2 = "";
c1 = (1,2,8,9)
c2 = (3,4,5,6,7)
for j in range(1,6):
	r1 = ""
	for i in c1:
		for k in range(1,5):
			r1 += "X" + str(i) + str(j) + str(k) + " + ";
	print r1 + '< 1'

for j in range(1,6):
	r2 = ""
	for i in c2:
		for k in range(1,5):
			r2 += "X" + str(i) + str(j) + str(k) + " + ";
	print r2 + '< 1'	
