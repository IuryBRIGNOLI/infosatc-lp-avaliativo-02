n1 = input("Digite uma marca de roupa ")
n2 = input("Digite uma marca de roupa ")
n3 = input("Digite uma marca de roupa ")
n4 = input("Digite uma marca de roupa ")
n5 = input("Digite uma marca de roupa ")

lista = [n1,n2,n3,n4,n5]
print(lista)

n6 = input("Digite uma marca para saber a posição na lista ")


print("A posicao da marca {} é ".format(n6),lista.index(n6))

