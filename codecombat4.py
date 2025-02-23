import random

# Funzione per lanciare i dadi in modo casuale
def lancia_dado(n_dadi, faccia_dado):
    return sum(random.randint(1, faccia_dado) for _ in range(n_dadi))

# Funzione per creare un personaggio casuale
def crea_personaggio(classe):
    if classe == 'Guerriero':
        vita = random.randint(100, 120)
        energia = random.randint(8, 10)
        difesa = random.randint(4, 8)
        attacco = lancia_dado(2, 6)
        abilita = lancia_dado(1, 6)
    elif classe == 'Mago':
        vita = random.randint(70, 90)
        energia = random.randint(14, 18)
        difesa = random.randint(3, 5)
        attacco = lancia_dado(1, 20)
        abilita = lancia_dado(1, 8)
    elif classe == 'Ladro':
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(3, 5)
        attacco = lancia_dado(3, 4)
        abilita = lancia_dado(1, 4)
    elif classe == 'Chierico':
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(4, 6)
        attacco = lancia_dado(1, 12)
        abilita = lancia_dado(1, 6)
    
    return {
        'classe': classe,
        'vita': vita,
        'energia': energia,
        'difesa': difesa,
        'attacco': attacco,
        'abilita': abilita
    }

# Funzione per creare un party
def crea_party():
    classi = ['Guerriero', 'Mago', 'Ladro', 'Chierico']
    return [crea_personaggio(classe) for classe in classi]

# Funzione per eseguire l'attacco
def esegui_turno(personaggio, avversario):
    if personaggio['energia'] < 2:
        # Riposa e recupera energia al massimo
        personaggio['energia'] = 10 if personaggio['classe'] in ['Mago', 'Chierico'] else 8
        print(f"{personaggio['classe']} riposa e recupera energia.")
        return False

    # Esegui attacco
    danno = personaggio['attacco'] - avversario['difesa']
    if danno > 0:
        avversario['vita'] -= danno
        personaggio['energia'] -= 2
        print(f"{personaggio['classe']} attacca {avversario['classe']} causando {danno} danni.")
    else:
        print(f"{personaggio['classe']} non riesce a danneggiare {avversario['classe']}.")

    # Attiva l'abilità speciale se necessario
    if personaggio['abilita'] == 6:
        if personaggio['classe'] == 'Guerriero':
            berserk(personaggio)
        elif personaggio['classe'] == 'Mago':
            concentrazione_assoluta(personaggio)
        elif personaggio['classe'] == 'Ladro':
            pugnali_acidi(personaggio, avversario)
        elif personaggio['classe'] == 'Chierico':
            favore_degli_dei(personaggio)

    return True

# Funzioni per le abilità speciali
def berserk(personaggio):
    risultato = lancia_dado(1, 6)
    print(f"Guerriero attiva Berserk con risultato {risultato}")
    if risultato >= 5:
        print("Guerriero attacca di nuovo!")
    elif risultato >= 3:
        personaggio['vita'] -= int(personaggio['vita'] * 0.2)
        print("Guerriero perde il 20% della vita.")
    else:
        personaggio['vita'] -= int(personaggio['vita'] * 0.2)
        print("Guerriero perde il 20% della vita.")

def concentrazione_assoluta(personaggio):
    risultato = lancia_dado(1, 6)
    print(f"Mago lancia la sua abilità con risultato {risultato}")
    if risultato >= 5:
        aumento = lancia_dado(1, 4)
        personaggio['attacco'] += aumento
        print(f"Mago aumenta l'attacco di {aumento} punti!")

def pugnali_acidi(personaggio, avversario):
    risultato = lancia_dado(2, 4)
    print(f"Ladro lancia pugnali acidi con risultato {risultato}")
    if risultato == 7 or risultato == 8:
        avversario['difesa'] = max(0, int(avversario['difesa'] * 0.75))
        print(f"Ladro riduce la difesa dell'avversario del 25%.")

def favore_degli_dei(personaggio):
    risultato = lancia_dado(2, 6)
    print(f"Chierico lancia la sua abilità con risultato {risultato}")
    personaggio['vita'] += risultato
    print(f"Chierico cura se stesso di {risultato} punti vita.")

# Funzione per verificare la vittoria
def verifica_vittoria(party):
    for personaggio in party:
        if personaggio['vita'] > 0:
            return False
    return True

# Funzione per eseguire il combattimento
def combattimento(party_1, party_2):
    turno = 0
    partita_in_corso = True
    while partita_in_corso:
        print(f"\nTurno {turno + 1}")
        # Esegui gli attacchi tra i due party
        for i in range(4):
            if esegui_turno(party_1[i], party_2[i]):
                if verifica_vittoria(party_2):
                    print("Partita finita! Il party 1 ha vinto!")
                    partita_in_corso = False
                    break

            if esegui_turno(party_2[i], party_1[i]):
                if verifica_vittoria(party_1):
                    print("Partita finita! Il party 2 ha vinto!")
                    partita_in_corso = False
                    break
        
        turno += 1

# Crea i due partiti
party_1 = crea_party()
party_2 = crea_party()

# Esegui il combattimento
combattimento(party_1, party_2)
