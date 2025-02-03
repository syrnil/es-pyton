import random

# Funzione per generare il numero di armate
def leggi_armate():
    scelta = input("Come vuoi impostare il numero di armate? (input/casuale/file): ").strip().lower()
    
    if scelta == 'input':
        # Input manuale dell'utente
        while True:
            try:
                attaccante = int(input("Quante armate vuoi per l'attaccante (tra 7 e 12)? "))
                difensore = int(input("Quante armate vuoi per il difensore (tra 7 e 12)? "))
                if 7 <= attaccante <= 12 and 7 <= difensore <= 12:
                    return attaccante, difensore
                else:
                    print("I numeri devono essere tra 7 e 12.")
            except ValueError:
                print("Inserisci un numero valido.")
                
    elif scelta == 'casuale':
        # Numeri casuali tra 7 e 12
        attaccante = random.randint(7, 12)
        difensore = random.randint(7, 12)
        print(f"Armata attaccante: {attaccante}, Armata difensore: {difensore}")
        return attaccante, difensore
    
    elif scelta == 'file':
        # Lettura da file "armate.txt"
        try:
            with open('armate.txt', 'r') as file:
                attaccante, difensore = map(int, file.readline().split())
                if 7 <= attaccante <= 12 and 7 <= difensore <= 12:
                    return attaccante, difensore
                else:
                    print("I numeri nel file devono essere tra 7 e 12.")
                    return leggi_armate()  # Richiediamo di nuovo la scelta
        except FileNotFoundError:
            print("Il file armate.txt non esiste.")
            return leggi_armate()  # Richiediamo di nuovo la scelta
        except ValueError:
            print("Il formato del file non è corretto.")
            return leggi_armate()  # Richiediamo di nuovo la scelta
    else:
        print("Scelta non valida, riprova.")
        return leggi_armate()

# Funzione per lanciare i dadi
def lancia_dadi(n):
    return sorted([random.randint(1, 6) for _ in range(n)], reverse=True)

# Funzione principale di simulazione del combattimento
def combattimento():
    attaccante, difensore = leggi_armate()

    while attaccante >= 1 and difensore >= 1:
        print(f"\nAttaccante ha {attaccante} armate, Difensore ha {difensore} armate.")
        
        while True:
            try:
                attacco = int(input(f"Quante armate vuoi usare per attaccare (max 3, disponibile {attaccante})? "))
                difesa = int(input(f"Quante armate vuoi usare per difendere (max 3, disponibile {difensore})? "))
                if 1 <= attacco <= 3 and 1 <= difesa <= 3 and attacco <= attaccante and difesa <= difensore:
                    break
                else:
                    print("Valori non validi, riprova.")
            except ValueError:
                print("Inserisci numeri validi.")
        
        # Lancio dei dadi
        dadi_attaccante = lancia_dadi(attacco)
        dadi_difensore = lancia_dadi(difesa)

        print(f"Dadi attaccante: {dadi_attaccante}")
        print(f"Dadi difensore: {dadi_difensore}")

        # Confronto dei dadi
        num_confronti = min(len(dadi_attaccante), len(dadi_difensore))
        armate_annientate_attaccante = 0
        armate_annientate_difensore = 0

        for i in range(num_confronti):
            if dadi_attaccante[i] > dadi_difensore[i]:
                armate_annientate_difensore += 1
            else:
                armate_annientate_attaccante += 1

        # Aggiornamento armate
        attaccante -= armate_annientate_attaccante
        difensore -= armate_annientate_difensore

        print(f"Il difensore ha perso {armate_annientate_difensore} armate.")
        print(f"L'attaccante ha perso {armate_annientate_attaccante} armate.")

    if attaccante > 0:
        print("\nL'attaccante ha vinto!")
    elif difensore > 0:
        print("\nIl difensore ha vinto!")
    else:
        print("\nÈ finito in pareggio!")

# Esecuzione del programma
combattimento()
