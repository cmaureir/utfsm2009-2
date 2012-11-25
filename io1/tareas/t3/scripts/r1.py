# Restriccion 1
r1 = "";
r2 = "";
c1 = (1,2,8,9)
c2 = (3,4,5,6,7)
for j in range(1,6):
	for k in range(1,5):
		for i in c1:
			r1 += "X" + str(i) + str(j) + str(k) + " + ";

for j in range(1,6):
	for k in range(1,5):
		for i in c2:
			r2 += "X" + str(i) + str(j) + str(k) + " + ";

print r1 + '= 4'
print r2 + '= 5'	
