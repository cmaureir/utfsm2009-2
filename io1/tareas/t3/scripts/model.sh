#!/bin/sh
echo "! Funcion objetivo"
echo -n "MIN "
python fo.py | sed 's/+ $//'
echo "ST"
echo "! Restricciones"
echo "! Cada profesor imparte todas sus asignaturas:"
python r1.py | sed 's/+ </</' | sed 's/+ =/=/'
echo "! Cada profesor imparte como mucho una asignatura cada hora:"
python r2.py | sed 's/+ </</' | sed 's/+ =/=/'
echo "! Cada asignatura se imparte una sola vez:"
python r3.py | sed 's/+ </</' | sed 's/+ =/=/'
echo "! En cada curso y bloque se imparte como mucho una sola asignatura:"
python r4.py | sed 's/+ </</' | sed 's/+ =/=/'
echo "! En cada bloque, se enseña como mucho una asignatura de cada curso:"
python r5.py | sed 's/+ </</' | sed 's/+ =/=/'
echo "END"
echo "! Naturaleza"
python naturaleza.py | sed 's/+ </</' | sed 's/+ =/=/'
