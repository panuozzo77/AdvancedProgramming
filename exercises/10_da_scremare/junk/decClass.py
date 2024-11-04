from itertools import count


def add_version(cls):
    cls.version = 'placeholder'
    return cls

def count_instances(cls):
    cls.count = 0
    old_init = cls.__init__

    def new_init(self, *args, **kwargs):
        cls.count += 1
        old_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@count_instances
class C:
    pass

c = C()
d = C()
e = C()
print(c.count)

