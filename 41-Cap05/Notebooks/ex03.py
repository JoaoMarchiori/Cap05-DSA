# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

lista = []

def add():
    m = 4
    for c in range(2):
        elemento2 = input(f"Adicione o {m+1}° elemento: ")
        lista.append(elemento2)
        m += 1
    print(lista)



for c in range(4):
    elemento = input(f"Escreva o {c+1}° elemento: ")
    lista.append(elemento)

add()

