if __name__=="__main__":
    print("\nI test")
    l=[2,8, 6,'a',4, 1, 3]
    for n,x in enumerate(generaElementi(l),start=1):
        print("L'elemento generato dalla  invocazione {} di next e` {}".format(n,x))


    print("\nII test")
    l=[]
    for n,x in enumerate(generaElementi(l)):
        print("L'elemento generato dalla  invocazione {} di next e` {}".format(n,x))

    print("\nIII test")
    l=[2,8, 6, 1, 4, 5, 3]
    for n,x in enumerate(generaElementi(l),start=1):
        print("L'elemento generato dalla  invocazione {} di next e` {}".format(n,x))

"""Il programma deve stampare:
I test
L'elemento generato dalla  invocazione 1 di next e` 2
L'elemento generato dalla  invocazione 2 di next e` 6
L'elemento generato dalla  invocazione 3 di next e` 3
L'elemento generato dalla  invocazione 4 di next e` a

II test

III test
L'elemento generato dalla  invocazione 1 di next e` 2
L'elemento generato dalla  invocazione 2 di next e` 6
L'elemento generato dalla  invocazione 3 di next e` 3
L'elemento generato dalla  invocazione 4 di next e` 1
L'elemento generato dalla  invocazione 5 di next e` 8

"""
