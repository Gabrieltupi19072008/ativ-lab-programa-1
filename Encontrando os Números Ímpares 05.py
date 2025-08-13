#    "id": 5,
#    "titulo": "Encontrando os Números Ímpares",
#   "descricao": "Crie uma função que filtre uma lista de números e retorne apenas os números ímpares."


def encontrar_impares(lista):
    return [item for item in lista if item % 2]

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Números ímpares:", encontrar_impares(numeros))
