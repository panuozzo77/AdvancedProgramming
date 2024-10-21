# g prima di essere decorata e` una funzione che restituisce una stringa formata da 4 ripetizioni del primo argomento, se  c'e` almeno un argomento,
# altrimenti restituisce una stringa vuota. Fornisci la funzione decora
@decora
def g(*args, **kwargs):
    """funzione da decorare"""
    if len(args) + len(kwargs) == 0: return ""
    if len(args) != 0:
        return args[0] * 4

    return kwargs[list(kwargs)[0]] * 4


print("invoco g(1,2,\"3\")")
try:
    g(1, 2, "3")
except TypeError:
    print("g e` stata invocata con uno o piu` argomenti non di tipo stringa")
print("\ninvoco g()")
print(g())
print("\ninvoco g(\"3\",\"2\",k=5)")
try:
    g("3", "2", k=5)
except TypeError:
    print("g e` stata invocata con uno o piu` argomenti non di tipo stringa")
print("\ninvoco g(\"il\",\"risultato\",k=\"e`\")")
print(g("il", "risultato", k="e`"))

"""
Il programma deve stampare:

invoco g(1,2,"3")
g e` stata invocata con uno o piu` argomenti non di tipo stringa

invoco g()


invoco g("3","2",k=5)
g e` stata invocata con uno o piu` argomenti non di tipo stringa

invoco g("il","risultato",k="e`")
il risultato e` ilililil

"""