sommatoria = 0
numeroSoldi = 0

while True:
    StipCorrente = float(input('inserisci lo stipendio(scrivi -1 quando gli stipendi sono terminati): '))
    if StipCorrente StipCorrente < -1:
        print('hai inserito', StipCorrente,', non è un valore accettabile.')
    elif StipCorrente == -1:
        break
    else:
        numeroSoldi += 1
        sommatoria += StipCorrente

media = sommatoria / numeroSoldi
print("la media è", media)