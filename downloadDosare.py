import xml.etree.ElementTree as ET
import datetime as dt
import re
import io

iddosar = 1
idparte = 1
idpers = 1

# f = open("dosar_TOT.sql", "w")
p = io.open("dbStructure/parti_TOT.sql", mode="w", encoding="utf-8")
pers = io.open("dbStructure/pers_TOT.sql", mode="w", encoding="utf-8")
f = io.open("dbStructure/dosar_TOT.sql", mode="w", encoding="utf-8")

# tree = ET.parse('C:/Users/Gabi/Desktop/dosare.xml')
tree = ET.parse('dosare.xml')

dosare = tree.getroot()[0][0][0]

f.write('INSERT INTO Dosar (id,nrDosar,instanta,anDosar,materie,obiect,stadiu,dataInreg,dataModif) VALUES \n\n')
p.write('INSERT INTO Parti (id,idPersoana,idDosar,calitate) VALUES \n\n')
pers.write('INSERT IGNORE INTO Persoane (id,nume) VALUES\n\n')

for dosar in dosare:
	d = nr = inst = an = 0
	materie = ""
	obiect = ""
	stadiu = ""
	data = ""
	dtmodif = ""

	for item in dosar:
		numeit = item.tag[21:]
		val = item.text
		findpattern = '%Y-%m-%dT%H:%M:%S'
		pattern = '%Y-%m-%d %H:%M:%S'

		if(val == None):
			val = ''
		if (numeit == 'numar'):
			d = val.split('/')
			nr = int(re.search(r'\d+', d[0]).group())
			inst = int(re.search(r'\d+', d[-2]).group())
			an = int(re.search(r'\d+', d[-1]).group())

		if (numeit == 'data'):
			data = dt.datetime.strptime(val[:19], findpattern).strftime(pattern)
		if (numeit == 'dataModificare'):
			dtmodif = dt.datetime.strptime(val[:19], findpattern).strftime(pattern)
		# if (numeit == 'departament'):
		if (numeit == 'obiect'):
			obiect = val
		if (numeit == 'stadiuProcesualNume'):
			stadiu = val
		if (numeit == 'categorieCazNume'):
			materie = val
		if (numeit == 'parti'):
			for parte in item:
				nume = ""
				calit = ""
				for eleme in parte:
					nm_elem = eleme.tag[21:]
					valoare = eleme.text
					if(valoare == None):
						valoare = ""
					valoare = valoare.replace('"', "'")
					valoare = valoare.replace('”', "'")
					valoare = valoare.replace('“', "'")
					valoare = valoare.replace('„', "'")
					if(nm_elem == 'nume'):
						nume = valoare
					if(nm_elem == 'calitateParte'):
						calit = valoare
				pers.write('('+ str(idpers) +',"'+ nume +'"),\n')
				p.write('('+ str(idparte) +','+ str(idpers) +','+ str(iddosar) +',"'+ calit +'"),\n')
				idpers += 1
				idparte += 1


	f.write(u'('+ str(iddosar) +','+ str(nr) +","+ str(inst) +","+ str(an) +',"'+ materie +'","')
	f.write(obiect)
	f.write('","'+ stadiu +'","'+ data +'","'+ dtmodif +'"),\n')
	iddosar += 1


f.write(" UPDATE Dosar SET IDComplet = ((id%8) + 1);")