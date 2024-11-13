"""
Immaginiamo che un bambino venga iscritto alla scuola media. Il bambino può essere in uno dei seguenti stati:
a. iscritto: il bimbo è inizialmente iscritto al primo anno
b. alSecondoAnno: il bimbo è promosso al secondo anno
c. alTerzoAnno: il bimbo è promosso al terzo anno
d. diplomato: al termine del terzo, il bimbo consegue il diploma di scuola media.
La classe Bambino ha il metodo succ() per passare allo stato successivo, il metodo pred() per passare a quello
precedente (retrocesso in caso di debiti formativi non recuperati) e il metodo salta_anno() per saltare un anno (da
iscritto si salta al terzo anno e dal secondo anno al diploma). Lo stato iscritto non ha stati che lo precedono;
lo stato diplomato non ha stati che vengono dopo di esso.
La classe Bambino ha anche un metodo stampaStato() per stampare lo stato del bambino.
Scrivere la classe Bambino usando un approccio state-specific in cui lo stato del bambino è una proprietà. Non usare altre classi
oltre la classe Bambino.
"""

class Bambino:
    def __init__(self):
        self.stato = "iscritto"  # Stato iniziale

    def succ(self):
        if self.stato == "iscritto":
            self.stato = "alSecondoAnno"
            print("Il bambino è nello stato alSecondoAnno")
        elif self.stato == "alSecondoAnno":
            self.stato = "alTerzoAnno"
            print("Il bambino è nello stato alTerzoAnno")
        elif self.stato == "alTerzoAnno":
            self.stato = "diplomato"
            print("Il bambino è nello stato diplomato")
        elif self.stato == "diplomato":
            print("Il bambino si è già diplomato e non può avanzare in uno stato successivo")

    def pred(self):
        if self.stato == "alSecondoAnno":
            self.stato = "iscritto"
            print("Il bambino è tornato allo stato iscritto")
        elif self.stato == "alTerzoAnno":
            self.stato = "alSecondoAnno"
            print("Il bambino è tornato allo stato alSecondoAnno")
        elif self.stato == "diplomato":
            self.stato = "alTerzoAnno"
            print("Il bambino è tornato allo stato alTerzoAnno")
        elif self.stato == "iscritto":
            print("Il bambino è appena stato iscritto al I anno e non può tornare in uno stato precedente")

    def salta_anno(self):
        if self.stato == "iscritto":
            self.stato = "alTerzoAnno"
            print("Il bambino ha saltato l'anno e ora è al Terzo anno")
        elif self.stato == "alSecondoAnno":
            self.stato = "diplomato"
            print("Il bambino ha saltato l'anno e ora è diplomato")
        else:
            print(f"Il bambino è nello stato {self.stato} e non può saltare un anno")

    def stampaStato(self):
        print(f"Il bambino è nello stato {self.stato}")

"""IL programma deve stampare:

Il bambino e` nello stato  iscritto
Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente
Il bambino e` nello stato  alSecondoAnno
Il bambino e` nello stato  alTerzoAnno
Il bambino e` nello stato alTerzoAnno  e non puo` saltare un anno
Il bambino e` nello stato  diplomato
Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo
"""

# File di test
def main():
    bambino = Bambino()
    bambino.stampaStato()
    bambino.pred()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()
    bambino.stampaStato()
    bambino.salta_anno()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()

if __name__ == "__main__":
    main()
