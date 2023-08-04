kontynuowac = True
while kontynuowac:
    lista = []
    for i in range(0, 5):
        lista.append(int(input("Podaj liczbe: ")))    
        lista.sort()
        lista.reverse()
    print(lista)

    decyzja = input("Czy chcesz kontynować? [T/N]")

    if decyzja.upper() == 'N':
        kontynuowac = False

    else:
        print("\n______________________\n")

print("Koniec")