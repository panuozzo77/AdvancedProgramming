'''
Un singleton, vogliamo un'unica istanza di un oggetto. Esiste solo un'istanza
'''

class Singleton:

    class __impl:
        '''Implementazione qui'''

        def spam(self):
            print("Spam!")

    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__impl()

        self.__dict__['Singleton_instance'] = Singleton.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)

if __name__ == '__main__':
    a = Singleton()
    a.spam()