'''
•	Elaborar um programa que efetue a leitura de 20 valores inteiros em uma matriz A com 4 linhas e 5 colunas. Construir uma lista B para 4 elementos que seja formada pelo somatório dos elementos correspondentes de cada linha da matriz A. Construir também uma lista C para 5 elementos que seja formada pelo somatório dos elementos correspondentes de cada coluna da matriz A. Ao final o programa deve apresentar os elementos da lista B e da lista C.
'''

matrizA = []
listaB = []
listaC = []
num = 0

for lin in range(3):
    lista = []
    for col in range(3):
        lista.append(int(input("Digite um elemento da Matriz : ")))
    matrizA.append(lista)

for lin in range(3):
    listaB.append(sum(matrizA[lin]))

for lin in range(3):
    for col in range(3):
        num += matrizA[col][lin]
    listaC.append(num)

print("==== Matriz ====")
for i in range(len(matrizA)):
    print(matrizA[i])
print("\n==== Listas ====")
print(f"Lista B - Somatório de cada linha\n{listaB}")
print(f"\nLista C - Somatório de cada coluna\n{listaC}")

