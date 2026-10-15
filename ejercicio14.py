print('Serie de Fibonacci')
ter = int(input('Ingrese cuantos terminos quiere: '))
a = 0
b = 1

for i in range(ter):
    print(a)
    a, b = b, a + b