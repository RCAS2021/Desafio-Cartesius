def encontra(digitos):
    n = len(digitos)
    for tam_A in range(1, n + 1):
        A = int(''.join(map(str, digitos[:tam_A])))
        A_str = str(A)
        A_len = len(A_str)
        
        pos = A_len
        numero = A + 1
        valid = True
        
        while pos < n:
            str_atual = str(numero)
            tam_atual = len(str_atual)
            if digitos[pos:pos + tam_atual] == list(map(int, str_atual)):
                pos += tam_atual
                numero += 1
            else:
                valid = False
                break
        
        if valid and pos == n:
            return A

if __name__ == '__main__':
    # Recebendo entrada
    digitos = list(map(int, input().split(' ')))
    n = digitos[0]
    digitos = digitos[1:]

    # Encontrar o menor A possível
    A = encontra(digitos)
    print(A)