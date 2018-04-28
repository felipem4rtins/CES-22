# Felipe Martins Gomes
# Comp 20
# Exercício 13.11.1
# Programa compilado com PyCharm 2018.1.2


entrada = open("Ex13.11.1.txt", "r")
arquivo = entrada.readlines()
entrada.close()

tamanho = len(arquivo)
tamanho -= 1

saida = open("saida13.1.1.txt", "w")
while tamanho >= 0:
    saida.write(arquivo[tamanho])
    tamanho -= 1

saida.close