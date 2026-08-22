vazia = []
cheia = [1, 2, 3, 4]

def verificar(cheia):
    if len(cheia) == 0:
        return True
    else:
        return False

def maximo(cheia):
    if len(cheia) == 0:
        return "-1"
    else:
        return max(cheia)

def minimo(cheia):
    if len(cheia) == 0:
        return "-1"
    else:
        return min(cheia)

def medio(cheia):
    nums = len(cheia)
    soma = sum(cheia)
    if len(cheia) == 0:
        return "-1"
    else:
        meio = (soma/nums)
        return meio

print(verificar(cheia))
print(maximo(cheia))
print(minimo(cheia))
print(medio(cheia))