lista = []
cand1 = input("come si chiama il 1 candidato?")
cand2 = input("come si chiama il 2 candidato?")
lista.append (cand1)
lista.append (cand2)
lista.sort ()
print (lista)

voti1 = int(input ("quanti voti ha avuto "+ cand1 + "?"))
voti2 = int(input ("quanti voti ha avuto "+ cand2 + "?"))
voti =[]
voti.append (voti1)
voti.append (voti2)
if voti1 > voti2:
    print("ha vinto " + cand1)
 
elif  voti1 == voti2:
    print("pareggio")

elif  voti1 < voti2:
    print("ha vinto " + cand2)

else :
    print("c'è qualquadra che non cosa")

voti.reverse ()
print(voti)