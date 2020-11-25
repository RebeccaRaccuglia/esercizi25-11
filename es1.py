cand1 = input("come si chiama il 1 candidato?")
cand2 = input("come si chiama il 2 candidato?")
voti1 = int(input ("quanti voti ha avuto "+ cand1 + "?"))
voti2 = int(input ("quanti voti ha avuto "+ cand2 + "?"))
somma = voti1 + voti2
percvoti1= (voti1*100/somma)
percvoti2= (voti2*100/somma)
print ( percvoti1 , "%" , cand1)
print ( percvoti2 , "%" , cand2 )
if percvoti1 > percvoti2:
    print("ha vinto " + cand1)
 
elif  percvoti1 == percvoti2:
    print("pareggio")

elif  percvoti1 < percvoti2:
    print("ha vinto " + cand2)

else :
    print("c'è qualquadra che non cosa")