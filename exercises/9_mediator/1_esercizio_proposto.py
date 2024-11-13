"""
Si considerino le classi Cane e Persona fornite nel file [mod.py](/exercises/9_mediator/mod.py) (nei file del team).
Scrivere la classe Casa che contiene due cani e una persona (la padrona dei cani).
- La classe Casa utilizza un mediatore per garantire che:
  - a. Quando almeno uno dei due cani abbaia, venga impostato a True un flag di allerta (variabile self.allerta nella bozza di \_\_init__ fornita in [esercizio2.py](???)).
  - b. Quando la padrona torna a casa, se il flag di allerta è True, verifica per ciascun cane se, tra l'ora in cui è tornata a casa e l'ora in cui il cane ha mangiato per l'ultima volta, sono trascorse più di 4 ore.
    - In tal caso, dà da mangiare al cane.
  - Se nessuno dei due cani ha abbaiato tra il momento in cui la padrona è uscita e quello in cui è tornata (il flag è False), allora non fa nulla al suo ritorno.

  - Nota Bene: Può succedere che:
    - il cane che abbaia non sia quello che ha fame,
    - oppure che abbaiano entrambi ma solo uno dei due abbia fame,
    - o ancora che almeno uno dei cani abbia abbaiato mentre nessuno dei due ha fame.
  - Suggerimenti:
    - Per ciascuno dei due punti, creare un callable: uno dei due deve essere associato ad entrambi i cani e l'altro deve essere associato alla padrona.
    - La differenza in ore tra due orari, ora1 e ora2, si calcola così: (ora1 - ora2).total_seconds() / 60 / 60.
"""

from datetime import datetime, timedelta
from mod import Cane, Persona, Mediator

class Casa:
    def __init__(self, cane1, cane2, persona):
        self.cane1 = cane1
        self.cane2 = cane2
        self.persona = persona
        self.allerta = False

        # Registriamo i callable per i cani e la persona
        mediator_pairs = [
            (self.cane1, self.cane_abbaia),
            (self.cane2, self.cane_abbaia),
            (self.persona, self.persona_torna_a_casa)
        ]

        # Creiamo il mediatore
        self.mediator = Mediator(mediator_pairs)

    def cane_abbaia(self, cane):
        print(f"{cane.nome} sta abbaiando!")
        self.allerta = True

    def persona_torna_a_casa(self, persona):
        ora_ritorno = persona.ora_ritorno
        print(f"{persona.nome} è tornata a casa alle {ora_ritorno.strftime('%H:%M')}.")

        if self.allerta:
            for cane in [self.cane1, self.cane2]:
                if (ora_ritorno - cane.oraUltimaPappa).total_seconds() / 3600 > 4:
                    print(f"Dà da mangiare a {cane.nome}.")
                    # Simuliamo che il cane mangi
                    cane.oraUltimaPappa = ora_ritorno  # Aggiorniamo l'ora dell'ultima pappa
                else:
                    print(f"{cane.nome} non ha fame.")
            # Reset del flag di allerta dopo che la padrona è tornata
            self.allerta = False
        else:
            print("Nessun cane ha abbaiato mentre era fuori casa.")


# Esempio di utilizzo
if __name__ == "__main__":
    ora_inizio = datetime.now()

    # Creazione dei cani e della persona
    cane1 = Cane("Fido", ora_inizio - timedelta(hours=5))
    cane2 = Cane("Rex", ora_inizio - timedelta(hours=3))
    persona = Persona("Alice")

    # Creazione della casa con i cani e la persona
    casa = Casa(cane1, cane2, persona)

    # Simuliamo l'uscita della padrona
    persona.esce()

    # Simuliamo che Fido abbaia
    cane1.abbaia()

    # Simuliamo il ritorno della padrona a casa
    persona.torna_a_casa(datetime.now())
