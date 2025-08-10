# "id": 2,
#    "titulo": "Encontrando o Maior Número",
#    "descricao": "Escreva uma função que receba uma lista de números e retorne o maior número encontrado nela.


def encontrar_maior(lista):
    maior = lista[0]
    posicao = 0
    for indice, numero in enumerate(lista):
        if numero > maior:
            maior = numero
            posicao = indice
    return maior, posicao

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

maior, posicao = encontrar_maior(numeros)
print(f"Maior número: {maior} (posição {posicao})")
