# Felipe Martins Gomes
# Comp 20
# Exercício 8.19.10
# Programa compilado com PyCharm 2018.1.2


def reverse (palavra):
    tamanho = len(palavra)
    k = 0
    reversa = ""
    while k < tamanho:
        reversa += palavra[tamanho - 1 - k]
        k += 1
    return reversa

def eh_palindromo (palavra):
    reversa = reverse(palavra)
    if palavra == reversa:
        print("eh_palindromo({})".format(palavra))
    else:
        print("not eh_palindromo({})".format(palavra))

def test (palavra):
    eh_palindromo(palavra)

test("abba")
test("abab")
test("tenet")
test("banana")
test("straw warts")
test("a")
test(" ")