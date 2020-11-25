print("calcolatore di veicoli")


sommatoria = 0
numeroVeicoli = 0
lista = []

while True:
	veicoliperOra = int(input("inserisci il numero di veicoli nelle ore (scrivi 0 quando finisci di inserire i veicoli)"))
	lista.append (veicoliperOra)
	if len(lista)== 1:
		print ("ore 2")

	elif len(lista)== 2:
		print ("ore 3")
	elif len(lista)== 3:
		print ("ore 4")
	elif len(lista)== 4:
		print ("ore 5")
	elif len(lista)== 5:
		print ("ore 6")
	elif len(lista)== 6:
		print ("ore 7")
	elif len(lista)== 7:
		print ("ore 8")
	elif len(lista)== 8:
		print ("ore 9")
	elif len(lista)== 9:
		print ("ore 10")
	elif len(lista)== 10:
		print ("ore 11")
	elif len(lista)== 11:
		print ("ore 12")
	elif len(lista)== 12:
		print ("ore 13")
	elif len(lista)== 13:
		print ("ore 14")
	elif len(lista)== 14:
		print ("ore 15")
	elif len(lista)== 15:
		print ("ore 16")
	elif len(lista)== 16:
		print ("ore 17")
	elif len(lista)== 17:
		print ("ore 18")
	elif len(lista)== 18:
		print ("ore 19")
	elif len(lista)== 19:
		print ("ore 20")
	elif len(lista)== 20:
		print ("ore 21")
	elif len(lista)== 21:
		print ("ore 22")
	elif len(lista)== 22:
		print ("ore 23")
	elif len(lista)== 23:
		print ("ore 24")
	else:
		break
	if veicoliperOra  < 0:
		print("hai inseritoun valore errato " )
	elif veicoliperOra == 0:
		break
	else:
		numeroVeicoli += 1
		sommatoria += veicoliperOra

print ("numero di veicoli: " ,sommatoria)
