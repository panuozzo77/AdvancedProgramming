'''
Goal: Write a generator function that produces a sequence of factorials.

Description: Create a generator function called myGenerator(n) that takes an integer n (where n >= 1) as input.
This function should act as an iterator that yields the first n factorials. The first time next() is called
on the generator, it should yield 1! (which is 1). The second time, it should yield 2! (which is 2), and so on, up to n!


Concepts Demonstrated: Using yield in a function to turn it into a generator
, producing values one at a time, and iteration using next()


Bonus Challenge: Define the generator function recursively
. This might involve writing an auxiliary recursive function and using yield from to delegate parts of the operation to the recursive calls.
yield from treats the expression provided as a subiterator, passing yielded values directly to the caller.
Values sent via send() and exceptions from throw() are also passed to the subiterator if it supports them
'''

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def myGenerator(n):
    for i in range(1, n+1):
        yield fact(i)

def myGenerator2():
   while True:
       n = yield
       yield fact(n)

if __name__ == '__main__':
    for x in myGenerator(5):
        print(x)
    print()

    generator = myGenerator2()
    generator.send(5)
    print(next(generator))
