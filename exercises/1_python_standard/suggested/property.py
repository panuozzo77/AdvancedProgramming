'''
è importante lavorare esclusivamente con attributi con _,
altrimenti se si usa solo 'x' si ha ricorsione infinita perché il setter chiama se stesso all'infinito
'''

class Test:

    def __init__(self):
        self._x = 10

    def get_x(self):
        print('Mi hai invocato!')
        return self._x

    def set_x(self, value):
        print('Imposto x a', value)
        self._x = value


    def del_x(self):
        print('Elimino x')
        del self._x

    x = property(get_x, set_x, del_x, 'Im the x property')

'''
Il nome delle funzioni usando i decoratori deve essere uguale al nome della variabile
altrimenti non le trova 
'''
class Test2:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        print('Mi hai invocato!')
        return self._x

    @x.setter
    def x(self, value):
        print('Imposto x a', value)
        self._x = value

    @x.deleter
    def x(self):
        print('Elimino x')
        del self._x

if __name__ == '__main__':
    c = Test2()
    print(c.x)
    c.x = 42
    print(c.x)
    del c.x