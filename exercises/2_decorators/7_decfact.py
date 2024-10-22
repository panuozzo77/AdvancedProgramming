"""
Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo per contare il numero
di invocazioni del metodo passato come parametro al decorator factory
"""

def countdecfact(meth):
    def countdecorator(a_class):
        a_class.numTimes = 0
        setattr(a_class, "old_meth", getattr(a_class, "meth1"))
        def newmeth(*args, **kwargs):
            a_class.numTimes = a_class.numTimes + 1
            getattr(a_class, "old_meth")(*args, **kwargs)
        setattr(a_class, "meth1", newmeth)
        @staticmethod
        def nTimes():
            return a_class.numTimes
        setattr(a_class, "nTimes", nTimes)
        return a_class
    return countdecorator

@countdecfact("meth1")
class MyClass:

    def meth1(self):
        print("sono meth1")

    def meth2(self):
        print("sono meth2")


"""
import functools

def fdecorator(funz):
    @functools.wraps(funz)
    def wrapper(lst, *args, **kwargs):
        def conv(a):
            try:
                return int(a)
            except Exception:
                return None  # Return None explicitly if conversion fails

        # Convert the list and filter out None values
        args = [conv(x) for x in lst if conv(x) is not None]
        return funz(*args, **kwargs)
    
    return wrapper

"""