'''
•	Escreva um programa que leia uma lista A com 10 elementos. Construir uma matriz C com três colunas, em que a primeira coluna da matriz C é formada pelos elementos da lista A somados com mais 5, a segunda coluna é formada pelo triplo de cada elemento correspondente da lista A e a terceira e última coluna deve ser formada pelos quadrados dos elementos correspondentes da lista A. Por fim, mostre os elementos da matriz C.
'''

listaA = []
matrizC = []

for i in range(10):
    listaA.append(int(input("Digite um elemento : ")))

for lin in range(10):
    lista = []
    for col in range(3):
        if(col==0):
            num = listaA[lin] + 5
            lista.append(num)
        if(col==1):
            num = listaA[lin] ** 3
            lista.append(num)
        if(col==2):
            num = listaA[lin] ** 4
            lista.append(num)
    matrizC.append(lista)

for i in range(len(matrizC)):
    print(matrizC[i])




