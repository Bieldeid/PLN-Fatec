import numpy as np

ex1 = np.arange(1,11)
print(ex1)

ex2 = np.random.random( (300, 200, 3) )
print(ex2)

ex3 = np.random.randint(1,11,(20, 3), dtype=np.uint8)
print (ex3)

ex4 = np.arange(12).reshape(3,4)
print(ex4)
print(ex4.T)

ex51 = np.array([1])
ex52 = np.array([1])
print("Soma : ", ex51 + ex52)
print("Subtração : ", ex51 - ex52)
print("Multiplicação : ", ex51 * ex52)
print("Divisão: ", ex51 / ex52)

ex6 = np.arange(1,21)
print(ex6[1::2])

ex7 = np.random.randint(1,101, (2))
print(ex7)

for x in ex7:
    if x > 50:
        print(x)

ex8 = np.random.rand(10);
print(ex8)

media = np.mean(ex8)
mediana = np.median(ex8)
desvio_padrao = np.std(ex8)

print("Média: ", media)
print("Mediana: ", mediana)
print("Desvio: ", desvio_padrao)
