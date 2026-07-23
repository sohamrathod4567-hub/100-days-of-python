def add(*args):
    sum = 0
    for n in args:
        sum +=n
    return sum

print(add(3,4,5))

def calculate(n , **kwargs):
    print(kwargs)
    for key , values in kwargs.items():
        print(key, values)





calculate(2,add=3, multiply=5)
