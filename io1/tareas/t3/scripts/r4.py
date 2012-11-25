# Restriccion 4
r = "";
for j in range(1,6):
	for k in range(1,5):
		r = ""
		for i in range(1,10):
			r += "X" + str(i) + str(j) + str(k) + " + ";
		print r + '< 1'
