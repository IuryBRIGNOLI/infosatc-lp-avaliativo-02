n1 = input("Digite uma fruta ")
n2 = input("Digite outra fruta ")
n3 = input("Digite outra fruta ")
lista = [n1,n2,n3]
print(lista)

n4 = input("Escolha uma fruta para verificar ")

if n4 in lista:
    print("Sim, está na lista! ")
else:
    print("Não está na lista ")
