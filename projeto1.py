'''
•	Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas. Construir uma lista B que seja formado pela soma de cada linha da matriz A. Ao final apresentar o somatório dos elementos da lista B.
'''

matrizA = []
listaB = []

for lin in range(8):
    linha = []
    for col in range(6):
        linha.append(int(input("Digite um elemento da Matriz : ")))
    matrizA.append(linha)

for lin in range(len(matrizA)):
    listaB.append(sum(matrizA[lin]))

print("\n=== Matriz ===")
for i in range(len(matrizA)):
    print(matrizA[i])

print("\nSomatório de cada linha")
print(listaB)
