#"id": 4,
#    "titulo": "Encontrando os Números Pares",
#    "descricao": "Desenvolva uma função que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares."


def encontrar_pares(lista):
    # filter filtra apenas os números que satisfazem a condição do lambda
    return list(filter(lambda x: x % 2 == 0, lista))

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Números pares:", encontrar_pares(numeros))
