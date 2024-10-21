import functools

def decf(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs)!=2:
            raise TypeError("function must have 2 arguments!")
        else:
            f_o=open("../risultato.txt", "a")
            res=function(*args, **kwargs)
            if res!=None:
                f_o.write(res)
            if args:
                f_o.write(str(args[0]))
            else:
                f_o.write(str(next(iter(kwargs.values()))))
            f_o.write("\n")
            f_o.close()
    return wrapper

@decf
def g(*args,**kwargs):
        return "io sono il risultato della funzione invocata con args={} e kwargs={}\n".format(args,kwargs)



print("invoco g(1,2,3)")
try:
        g(1,2,3)
except TypeError:
        print("g e` stata invocata con un numero di argomenti diverso da due")
print("\ninvoco g()")
try:
        g()
except TypeError:
        print("g e` stata invocata un numero di argomenti diverso da due")
print("\ninvoco g(3,2,k=5)")
try:
        g(3,2,k=5)
except TypeError:
        print("g e` stata invocata un numero di argomenti diverso da due")

print("\ninvoco g(1,2)")
g(1,2)
print("\ninvoco g(9,k=2)")
g(9,k=2)
print("\ninvoco g(j=6,k=3)")
g(j=6,k=3)



"""
Dopo aver eseguito il programma una volta, il file risultato.txt deve contenere le seguenti linee:

io sono il risultato della funzione invocata con args=(1, 2) e kwargs={}
1
io sono il risultato della funzione invocata con args=(9,) e kwargs={'k': 2}
9
io sono il risultato della funzione invocata con args=() e kwargs={'j': 6, 'k': 3}
6
"""

"""
Il programma deve stampare:

invoco g(1,2,3)
g e` stata invocata con un numero di argomenti diverso da due

invoco g()
g e` stata invocata un numero di argomenti diverso da due

invoco g(3,2,k=5)
g e` stata invocata un numero di argomenti diverso da due

invoco g(1,2)

invoco g(9,k=2)

invoco g(j=6,k=3)


"""