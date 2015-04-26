import sqlite3
import hashlib
import signal
import sys

global i
global count


def signal_handler(signal, frame):
	print "Claves comprobadas hasta el momento: ", count
	print "Generando: ", i


def valido(patron):
	cadena = str(patron)
	lista = []
	for i in cadena:
		lista.append(int(i))
	if lista.count(1) > 1:
		return False
	if lista.count(2) > 1:
		return False
	if lista.count(3) > 1:
		return False
	if lista.count(4) > 1:
		return False
	if lista.count(5) > 1:
		return False
	if lista.count(6) > 1:
		return False
	if lista.count(7) > 1:
		return False
	if lista.count(8) > 1:
		return False
	if lista.count(9) > 0:
		return False
	if lista.count(0) >1:
		return False
	return True

con = sqlite3.connect('hashes.db')
cursor = con.cursor()
signal.signal(signal.SIGINT, signal_handler)

count = 0

for i in xrange (100,888):
	patron = '%04d' % i
	count = count + 1
	if valido(patron):
		#print patron
		h = hashlib.sha1(patron)
		t = (patron, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)

for i in xrange (1000,8888):
	patron = '%05d' % i
	count = count + 2
	if valido(patron):
		#print patron
		h = hashlib.sha1(patron)
		t = (patron, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)
	if valido(i):
		#print i
		h = hashlib.sha1(str(i))
		t = (i, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)
		

for i in xrange (10000,88888):
	patron = '%06d' % i
	count = count + 2
	if valido(patron):
		#print patron
		h = hashlib.sha1(patron)
		t = (patron, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)
	if valido(i):
		#print i
		h = hashlib.sha1(str(i))
		t = (i, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)


for i in xrange (100000,888888):
	patron = '%07d' % i
	count = count + 2
	if valido(patron):
		#print patron
		h = hashlib.sha1(patron)
		t = (patron, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)
	if valido(i):
		#print i
		h = hashlib.sha1(str(i))
		t = (i, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)

for i in xrange (1000000,8888888):
	patron = '%08d' % i
	count = count + 2
	if valido(patron):
		#print patron
		h = hashlib.sha1(patron)
		t = (patron, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)
	if valido(i):
		#print i
		h = hashlib.sha1(str(i))
		t = (i, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)

for i in xrange (10000000,88888888):
	patron = '%09d' % i
	count = count + 2
	if valido(patron):
		#print patron
		h = hashlib.sha1(patron)
		t = (patron, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)
	if valido(i):
		#print i
		h = hashlib.sha1(str(i))
		t = (i, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)

for i in xrange (100000000,888888888):
	count = count + 1
	if valido(i):
		#print i
		h = hashlib.sha1(str(i))
		t = (i, str(h.hexdigest()))
		cursor.execute('INSERT INTO Hashes (patron, hash) VALUES (?,?)', t)


con.commit()

print "Todas las passwords generadas, total passwords generadas: %s" % count
