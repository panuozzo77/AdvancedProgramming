"""
Scrivere un generatore che data una lista la restituisce al contrario (?)
"""

def reverse_gen(l):
    for item in reversed(l):
        yield item

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    for item in reverse_gen(my_list):
        print(item)