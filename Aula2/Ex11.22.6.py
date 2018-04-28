# Felipe Martins Gomes
# Comp 20
# Exercício 11.22.6
# Programa compilado com PyCharm 2018.1.2


def scalar_mult (s, v):
    tamanho = len(v)
    k = 0
    escalar = []
    while k < tamanho:
        escalar.append(s*v[k])
        k += 1
    return escalar

def test (a,b):
    if a == b:
        print("True")
    else:
        print("False")

a = 5
b = [1,2]
c = 3
d = [1, 0, -1]
e = 7
f = [3, 0, 5, 11, 2]

print("test(scalar_mult(5, [1, 2]) == [5, 10]")
mult1 = scalar_mult(a, b)
test(mult1, [5, 10])

print("test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3]")
mult2 = scalar_mult(c, d)
test(mult2, [3, 0, -3])

print("test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]")
mult3 = scalar_mult(e, f)
test(mult3, [21, 0, 35, 77, 14])