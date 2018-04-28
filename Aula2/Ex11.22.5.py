# Felipe Martins Gomes
# Comp 20
# Exercício 11.22.5
# Programa compilado com PyCharm 2018.1.2


def add_vectors (u, v):
    L = len(u)
    soma = []
    k = 0
    while k < L:
        soma.append(u[k]+v[k])
        k += 1
    return soma

def test (a,b):
    if a == b:
        print("True")
    else:
        print("False")

soma1 = add_vectors([1,1],[1,1])
soma2 = add_vectors([1, 2], [1, 4])
soma3 = add_vectors([1, 2, 1], [1, 4, 3])

print("test(add_vectors([1, 1], [1, 1]) == [2, 2])")
test(soma1, [2,2])

print("test(add_vectors([1, 2], [1, 4]) == [2, 6]")
test(soma2,[2, 6])

print("test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])")
test(soma3, [2, 6, 4])