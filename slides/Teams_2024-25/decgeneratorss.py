class T:
    var0=10

class ClasseP(T):
    var1=2
    var2=8
    var4=7
    def __init__(self,a):
        self.varP=a
    
class ClasseM(T):
    var1=2
    var3=5
    var4=6
    var6="ann"
    def __init__(self,a):
        self.varM=6

        
@decFact(int)
class Classe(ClasseP,ClasseM):
    var1=6
    var5="pop"
    def __init__(self,a):
        self.varM=3
        self.varP=10
    def f(self):
        pass
    def g():
        pass
        

oggetto=Classe(3)

print("Prima stampo i valori di tutte le variabili di classe:")
print("var0:",Classe.var0)
print("var1:",Classe.var1)
print("var2:",Classe.var2)
print("var3:",Classe.var3)
print("var4:",Classe.var4)
print("var5:",Classe.var5)
print("var6:",Classe.var6)

print("\nOra invoco il metodo riportaVariabiliDiClasse per scandire le variabili di classe di tipo int")
for var in Classe.riportaVariabiliDiClasse():
    print("Nome  della variabile di classe: {}. Valore della variabile: {}. Classe in cui e` definita la variabile: {}.".format(var[0],var[1],var[2].__name__))



print("\nModifichiamo il valore di var1 e var4")
Classe.var1=11
Classe.var4=13
print("Prima stampo i valori di tutte le variabili di classe:")
print("var0:",Classe.var0)
print("var1:",Classe.var1)
print("var2:",Classe.var2)
print("var3:",Classe.var3)
print("var4:",Classe.var4)
print("var5:",Classe.var5)
print("var6:",Classe.var6)

print("\nOra invoco il metodo riportaVariabiliDiClasse per scandire le variabili di classe di tipo int")
for var in oggetto.riportaVariabiliDiClasse():
    print("Nome della variabile di classe: {}. Valore della variabile: {}. Classe in cui e` definita la variabile: {}.".format(var[0],var[1],var[2].__name__))

"""Il programma deve stampare:

Prima stampo i valori di tutte le variabili di classe:
var0: 10
var1: 6
var2: 8
var3: 5
var4: 7
var5: pop
var6: ann

Ora invoco il metodo riportaVariabiliDiClasse per scandire le variabili di classe di tipo int
Nome  della variabile di classe: var1. Valore della variabile: 6. Classe in cui e` definita la variabile: Classe.
Nome  della variabile di classe: var2. Valore della variabile: 8. Classe in cui e` definita la variabile: ClasseP.
Nome  della variabile di classe: var4. Valore della variabile: 7. Classe in cui e` definita la variabile: ClasseP.
Nome  della variabile di classe: var3. Valore della variabile: 5. Classe in cui e` definita la variabile: ClasseM.
Nome  della variabile di classe: var0. Valore della variabile: 10. Classe in cui e` definita la variabile: T.

Modifichiamo il valore di var1 e var4
Prima stampo i valori di tutte le variabili di classe:
var0: 10
var1: 11
var2: 8
var3: 5
var4: 13
var5: pop
var6: ann

Ora invoco il metodo riportaVariabiliDiClasse per scandire le variabili di classe di tipo int
Nome della variabile di classe: var1. Valore della variabile: 11. Classe in cui e` definita la variabile: Classe.
Nome della variabile di classe: var4. Valore della variabile: 13. Classe in cui e` definita la variabile: Classe.
Nome della variabile di classe: var2. Valore della variabile: 8. Classe in cui e` definita la variabile: ClasseP.
Nome della variabile di classe: var3. Valore della variabile: 5. Classe in cui e` definita la variabile: ClasseM.
Nome della variabile di classe: var0. Valore della variabile: 10. Classe in cui e` definita la variabile: T.
"""
