def natural(num1):
    if num1 <= 0: #assumindo que 0 não é natural
        return False
    return True

def fatorial(num1):
    if natural(num1):
        resultado = 1
        while num1 > 1:
            resultado *= num1
            num1 -= 1
    else:
        resultado = 'O fatorial só é definido para os números naturais!'

    return resultado

num = float(input("Digite um número: "))

print(f"O fatorial de {num} é: {fatorial(num)}")