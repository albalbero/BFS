'''
Questo codice trova l'uscita di un labirinto usando l'algoritmo BFS creato da me.
Per funzionare:
- ogni riga del labirinto deve corrispondere a una riga del file di input
- i muri devono essere scritti con #
- gli spazi senza muri devono essere scritti con .
- l'inizio e la fine devono essere contrassegnsti rispettivamente con S e E
'''

from collections import deque
import time

# conto il numero di righe e colonne del labirinto
def contatore_r_c(f):
    righe = 0
    while f.readline() != "":
        righe += 1
    f.seek(0)
    colonne = len(list(map(str, f.readline().split())))
    return righe, colonne

# controllo se ci sono sia S che E
def controllo(matrice):
    entrata = False
    uscita = False
    for riga in matrice:        
        if 'S' in riga:
            entrata = True
        if 'E' in riga:
            uscita = True
        if entrata and uscita:
            break            
    return entrata, uscita
    
# allargo la matrice con # attorno
def allargo_matrice(matrice, linee, colonne):
    temp = []
    for linea in matrice:
        linea.insert(0, '#')
        linea.append('#')
    for i in range(colonne + 2):
        temp.append('#')
    matrice.insert(0, temp)
    matrice.insert(linee + 1, temp)
    return matrice

# trovo la posizione di S
def trovo_entrata(matrice):
    for i in range(len(matrice)):
        for z in range(len(matrice[i])):
            if matrice[i][z] == 'S':
                x_iniziale = z
                y_iniziale = i
                return x_iniziale, y_iniziale

# tempo di riferimento
def tempo():
    return(time.time())


# --------------------------- separatore delle funzioni dal codice ---------------------------


with open("input.txt", "r") as f_in, open("output.txt", "w", encoding="UTF-8") as f_out:

    inizio = tempo()

    righe, colonne = contatore_r_c(f_in)

    f_in.seek(0) # riporta il puntatore a leggere la prima riga

    # creo la matrice come variabile
    matrice = []
    for i in range(righe):
        riga = list(map(str, f_in.readline().split()))
        matrice.append(riga)

    entrata, uscita = controllo(matrice)

    if not entrata:
        f_out.write("Manca l'entrata")
        quit()
    if not uscita:
        f_out.write("Manca l'uscita")
        quit()

    matrice = allargo_matrice(matrice, righe, colonne) # allargo la matrice

    # creo una matrice copia con tutti None
    matrice2 = [[None for _ in riga] for riga in matrice]

    # aggiungo la posizione di S alla coda (così non mi da l'errore pop from entry list
    x_iniziale, y_iniziale = trovo_entrata(matrice)

    posy = y_iniziale # Y = riga
    posx = x_iniziale # X = colonna
    coda = deque([[posy, posx]])
    matrice2[posy][posx] = 0
    
    # creo la lista strada per dire tutti i passaggi che ho fatto
    strada = [] # la metto fuori perché se non c'è nessuna uscita non mi dà errore
    
    # finché la coda ha qualcosa
    while coda:
        
        # vado nella casella prima in coda
        pos = coda.popleft()
        posy = pos[0]
        posx = pos[1]
    
        # prima controllo se la casella che devo controllare è l'uscita
        if matrice[posy][posx] == 'E':
            
            # mi salvo le posizioni finali
            posy_finale = posy
            posx_finale = posx
            
            coda_reverse = deque([[posy, posx]]) # coda_reverse mi fa fare un BFS ma al contrario
            strada.append([posy, posx]) # aggiungo la pos iniziale che sarà quella finale
            while matrice2[posy][posx] != 0: 
                pos = coda_reverse.popleft()
                posy = pos[0]
                posx = pos[1]
                
                # aggiungo le caselle vicine alla coda (uso elif perché so già che sono entrambe lunghe uguali))
                if matrice[posy-1][posx] != '#' and matrice2[posy-1][posx] == matrice2[posy][posx] - 1: # N
                    strada.append([posy-1, posx])
                    coda_reverse.append([posy-1, posx])
        
                elif matrice[posy][posx+1] != '#' and matrice2[posy][posx+1] == matrice2[posy][posx] - 1: # E
                    strada.append([posy, posx+1])
                    coda_reverse.append([posy, posx+1])
        
                elif matrice[posy+1][posx] != '#' and matrice2[posy+1][posx] == matrice2[posy][posx] - 1: # S
                    strada.append([posy+1, posx])
                    coda_reverse.append([posy+1, posx])
                            
                elif matrice[posy][posx-1] != '#' and matrice2[posy][posx-1] == matrice2[posy][posx] - 1: # O
                    strada.append([posy, posx-1])
                    coda_reverse.append([posy, posx-1])
            
            
                                    
        # altrimenti aggiungo le caselle vicine in coda
        if matrice[posy-1][posx] != '#' and matrice2[posy-1][posx] == None: # N
            coda.append([posy-1, posx])
            matrice2[posy-1][posx] = matrice2[posy][posx] + 1

        if matrice[posy][posx+1] != '#' and matrice2[posy][posx+1] == None: # E
            coda.append([posy, posx+1])
            matrice2[posy][posx+1] = matrice2[posy][posx] + 1

        if matrice[posy+1][posx] != '#' and matrice2[posy+1][posx] == None: # S
            coda.append([posy+1, posx])
            matrice2[posy+1][posx] = matrice2[posy][posx] + 1

        if matrice[posy][posx-1] != '#' and matrice2[posy][posx-1] == None: # O
            coda.append([posy, posx-1])
            matrice2[posy][posx-1] = matrice2[posy][posx] + 1

    if strada == []:
        f_out.write("Non c'è nessuna uscita")
    else:
        strada.reverse()
        f_out.write("Uscita trovata con " + str(matrice2[posy_finale][posx_finale]) + " passi\n")
        
        # per la rappresentazione grafica (modifico i None in #)
        for row in range(len(matrice2)):
            for col in range(len(matrice2[0])):
                if matrice[row][col] == '.':
                    matrice2[row][col] = ' '
                elif matrice[row][col] == 'S':
                    matrice2[row][col] = 'S'
                elif matrice[row][col] == 'E':
                    matrice2[row][col] = 'E'
                else:
                    matrice2[row][col] = '#'
                
        # guardo se la cella è nella lista strada (se è la strada giusta)
        for el in strada:
            if matrice2[el[0]][el[1]] == ' ':
                matrice2[el[0]][el[1]] = '·'
        for row in matrice2:
            f_out.write(' '.join(row) + "\n")

    fine = tempo()

    f_out.write("tempo impiegato = " + str(fine - inizio))