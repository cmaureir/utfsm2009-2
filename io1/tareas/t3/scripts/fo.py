# Funcion objetivo
z = "";
for i in range(1,10):
	for j in range(1,6):
		for k in range(1,5):
			z += str(i*(j+k)) + " X" + str(i) + str(j) + str(k) + " + ";
print z
