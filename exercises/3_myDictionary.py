class MyDictionary:
    def __init__(self):
        # Dictionary to store key-value pairs
        self.store = {}

    def __setitem__(self, key, value):
        # Set a key-value pair in the dictionary
        self.store[key] = value

    def __getitem__(self, key):
        # Retrieve the value for the given key
        if key not in self.store:
            raise KeyError(key)
        return self.store[key]

    def __delitem__(self, key):
        # Delete the key-value pair from the dictionary
        if key in self.store:
            del self.store[key]
        else:
            raise KeyError(key)

    def __eq__(self, other):
        # Compare two dictionaries by their key-value pairs
        if isinstance(other, MyDictionary):
            return self.store == other.store
        return False

    def __str__(self):
        # Custom string representation to match the expected output
        return '{' + ','.join(f"({k},{v})" for k, v in self.store.items()) + '}'

    def __repr__(self):
        return self.__str__()

"""Test per myDidictionary (si veda l'ultimo fascicolo di slide)."""

dic=MyDictionary()
dic["a"]='r'
dic["a"]='e'
print(dic['a'])
dic["b"]='d'
print(dic['b'])
dic["a"]=2
dic["c"]=4
print(dic['a'])
dic["b"]='f'
print(dic['b'])
dic["c"]=6
dic1=MyDictionary()
if dic==dic1:
        print ("ciao")
try:
        print(dic1["c"])
except KeyError as e:
        print("Errore: la chiave {} non e` presente nel dizionario".format(e))
print(dic1)
dic["a"]='r'
dic["a"]='e'
print(dic["a"])
del dic['a']
try:
        print(dic["a"])
except KeyError as e:
        print("Errore: la chiave {} non e` presente nel dizionario".format(e))
dic["b"]='d'

dic1["a"]=2
dic1["c"]=4
dic1["b"]='f'
dic1["c"]=6
print('dic:',dic)
print('dic1:',dic1)
if dic!=dic1:
        print("non sono uguali")
dic["a"]=2
dic["c"]=4
dic["b"]='f'
dic["c"]=6
print('dic:',dic)
print('dic1:',dic1)
if dic==dic1:
        print("sono uguali")
del dic["a"]
print(dic)




"""Il programma deve stampare:
e
d
2
f
Errore: la chiave 'c' non e` presente nel dizionario
{}
e
Errore: la chiave 'a' non e` presente nel dizionario
dic: {(b,d),(c,6)}
dic1: {(a,2),(c,6),(b,f)}
non sono uguali
dic: {(b,f),(c,6),(a,2)}
dic1: {(a,2),(c,6),(b,f)}
sono uguali
{(b,f),(c,6)}

"""