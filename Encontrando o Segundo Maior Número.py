# "id": 3
# "titulo": "Encontrando o Segundo Maior Número"
# "descricao": "Crie uma função que retorne o segundo maior número de uma lista. Considere que a lista pode ter números duplicados."


def segundo_maior(lista):
    maior = segundo = float('-inf')  # Inicializa com menor valor possível
    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif maior > num > segundo:
            segundo = num
    return segundo if segundo != float('-inf') else None

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Segundo maior número:", segundo_maior(numeros))
