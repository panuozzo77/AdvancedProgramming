f"""

- Scrivere la classe ClasseB che ha il metodo di istanza contaVarClasse(self, t, n) che:
    - prende in input un tipo t e un intero n
    - restituisce il numero di variabili di classe di tipo t delle prime n classi della gerarchia formata dalla classe
      in cui self è istanza e dalle sue superclassi, le prime n secondo l'ordine indicato in __mro__. Se il numero di 
      classi nella suddetta gerarchia è minore di n allora vengono considerate tutte le classi della gerarchia.
    
    -NB: gli attributi di classe o istanza di classe o modulo sono mantenuti in un dizionario detto __dict__ che è a sua
     volta un attributo dell'oggetto.
    - vars({object}) restituisce il __dict__ per il modulo, classe o istanza dotata di __dict__.
"""

class ClasseA:
    a = int(1)
    b = int(2)
    c = float(1)
    d = str('someText')


class ClasseB(ClasseA):
    e = int(3)
    f = int(4)
    g = float(2)

     #seconda versione migliorata
    def contaVarClasse(self, t, n):
        number = 0
        fullmro = self.__class__.mro()
        if len(fullmro) < n:
            n = len(fullmro)
        for cls in fullmro[:n+1]:
            classVars = vars(cls)
            for k, _ in classVars.items():
                if type(classVars.get(k)) == t:
                    number += 1
        return number

    #prima versione, problema quando n è più grande del numero di superclassi
    def contaVarClasse2(self, t, n):
        number = 0
        classVars = vars(self.__class__)
        while n >= 0:
            for k, _ in classVars.items():
                if type(classVars.get(k)) == t:
                    number += 1
            n -= 1
            classVars = vars(type(self).__base__)
        return number


x = ClasseB()

print("Ci sono", x.contaVarClasse(int, 6), "elementi con lo stesso tipo di t")