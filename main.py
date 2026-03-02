import random


class Domanda:

    def __init__(self, testoDomanda: str, livelloDifficolta: int, rispostaCorretta: str, rispostaErrata1: str, rispostaErrata2: str, rispostaErrata3: str):
        self.testoDomanda = testoDomanda
        self.livelloDifficolta = livelloDifficolta
        self.rispostaCorretta = rispostaCorretta
        self.rispostaErrata1 = rispostaErrata1
        self.rispostaErrata2 = rispostaErrata2
        self.rispostaErrata3 = rispostaErrata3

    def stampaDomanda(self):
        listaRisposte = [self.rispostaCorretta, self.rispostaErrata1, self.rispostaErrata2, self.rispostaErrata3]
        random.shuffle(listaRisposte)
        domanda = f"Livello {self.livelloDifficolta} ) {self.testoDomanda}\n"
        i = 1
        for risposta in listaRisposte:
            domanda += f"{i}. {risposta}\n"
            i = i+1

        return domanda, listaRisposte



def leggiFile(nomeFile,domandeDizionario):
    with open(nomeFile, "r") as file:
        parametriDomanda = []
        for riga in file:
            if riga.strip() != "":
                parametriDomanda.append(riga.strip())

            if len(parametriDomanda) == 6:
                livello = int(parametriDomanda[1])
                domanda = Domanda(parametriDomanda[0],livello,parametriDomanda[2],parametriDomanda[3],parametriDomanda[4],parametriDomanda[5])
                if livello not in domandeDizionario:
                    domandeDizionario[livello] = []
                domandeDizionario[livello].append(domanda)
                parametriDomanda = []

        return domandeDizionario



def trovaLivelloMassimo(dizionario):
    livelloMassimo =0
    for key in dizionario:
        if (key > livelloMassimo):
            livelloMassimo = key
    return livelloMassimo

def player(nomeFile, nuovo_punteggio, nickname):
    punteggi = {}
    with open(nomeFile, "r", encoding="utf-8") as f:
        for riga in f:
            parti = riga.strip().split()
            nome = parti[0]
            punteggi[nome] = int(parti[1])
            if nickname in punteggi:
                punteggi[nickname] = nuovo_punteggio
            else:
                punteggi[nickname] = nuovo_punteggio
    punteggi_ordinati = sorted(punteggi.items(), key=lambda x: x[1], reverse=True)
    with open(nomeFile, "w", encoding="utf-8") as f:
        for nome, punteggio in punteggi_ordinati:
            f.write(f"{nome} {punteggio}\n")

domandeDizionario = {}
nomeFile = "domande.txt"
domande = leggiFile(nomeFile, domandeDizionario)
d_ordinato = dict(sorted(domande.items()))
livelloCorrente = 0
livelloMassimo = trovaLivelloMassimo(d_ordinato)
punteggio = 0
for livelloCorrente in range(0,livelloMassimo+1):

        domandeCorrente = d_ordinato[livelloCorrente]
        d = random.choice(domandeCorrente)
        rispostaCorretta = d.rispostaCorretta
        domanda, listaRisposte = d.stampaDomanda()
        print(domanda)
        rispostaUtente = input("Inserisci la risposta: ")
        if rispostaUtente.isdigit():
            indice = int(rispostaUtente)
            if 0<= indice <= 4:
                rispostaUtenteScritta = listaRisposte[indice-1]
            else:
                print("Numero non valido! Risposta considerata sbagliata.")
                break

        if(rispostaCorretta.lower() == rispostaUtenteScritta.lower()):
            print(f"Risposta corretta!")
            punteggio +=1
            livelloCorrente += 1

        else:
            ##totale punteggi e inserire nickname e salvarlo in file (uscire dal ciclo) RETURN
            print(f"Risposta sbagliata! La risposta corretta era: {rispostaCorretta}")
            print(f" Hai totalizzato {punteggio} punti!")
            nickname = input("Inserisci il tuo nickname: ")
            player("punti.txt", punteggio, nickname)
            break

        if (rispostaCorretta.lower() == rispostaUtente.lower() and livelloCorrente-1 == livelloMassimo):
            print(f"Hai totalizzato {punteggio} punti!")
            nickname = input("Inserisci il tuo nickname: ")
            player("punti.txt",punteggio,nickname)
            break







