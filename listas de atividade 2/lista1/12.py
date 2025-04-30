expressao = input("Digite dois valores inteiros separados por um operador +, -, * ou /: ")

if '+' in expressao:
    a, b = map(int, expressao.split('+'))
    resultado = a + b
elif '-' in expressao:
    a, b = map(int, expressao.split('-'))
    resultado = a - b
elif '*' in expressao:
    a, b = map(int, expressao.split('*'))
    resultado = a * b
elif '/' in expressao:
    a, b = map(int, expressao.split('/'))
    if b == 0:
        print("Divisão por zero não é permitida.")
        exit()
    resultado = a / b
else:
    print("Operador inválido.")
    exit()

print(f"O resultado da operação é {resultado}")