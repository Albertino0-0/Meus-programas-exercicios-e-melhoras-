import math

def mostrar_mensagem():  
    print("Bem-vindo à calculadora ")

mostrar_mensagem() 

try:
    qtd = int(input("Quantos números você quer usar? "))
    if qtd <= 0:
        print("Digite um número positivo!")
except ValueError:
    print("Erro: Digite um número válido!")

print("\nEscolha a operação:")
print("1 : Soma")
print("2 : Subtração")
print("3 : Multiplicação")
print("4 : Divisão")
print("5 : Percentagem")
print("6 : Raiz quadrada")
print("7 : Raiz cúbica")
print("8 : Elevação a potência")
print("9 : Operações com Pi")

operacao = input("Digite o número da operação: ")

if operacao == "1":
    resultado = 0  
    for i in range(qtd):
        num = int(input(f"Digite o {i+1}º número: "))
        resultado += num
    print(f"O resultado da soma é: {resultado}")

elif operacao == "2":
    resultado = int(input("Digite o 1º número: "))
    for i in range(1, qtd):
        num = int(input(f"Digite o {i+1}º número: "))
        resultado -= num
    print(f"O resultado da subtração é: {resultado}")

elif operacao == "3":
    resultado = 1  
    foi_multiplicado_por_zero = False  
    
    for i in range(qtd):
        num = int(input(f"Digite o {i+1}º número: "))
        
        if num == 0:
            print("Qualquer número multiplicado por 0 é igual a 0!")
            resultado = 0
            foi_multiplicado_por_zero = True
            break  
            
    if not foi_multiplicado_por_zero:
        print(f"O resultado da multiplicação é: {resultado}")
    else:
        print("O resultado da multiplicação é: 0")

elif operacao == "4":
    resultado = float(input("Digite o 1º número: "))
    erro_divisao = False
    
    for i in range(1, qtd):
        num = float(input(f"Digite o {i+1}º número: "))
        if num == 0:
            print("Impossível dividir por zero!")
            erro_divisao = True
            break   
        resultado /= num
        
    if not erro_divisao:
        print(f"O resultado da divisão é: {resultado}")

elif operacao == "5":
    print("\n--- Escolha o tipo de percentagem ---")
    print("1: Calcular X% de Y (Ex: 20% de 100)")
    print("2: Aumento de percentagem (Ex: 100 + 20%)")
    print("3: Desconto de percentagem (Ex: 100 - 20%)")
    tipo_perc = input("Escolhe (1, 2 ou 3): ")

    if tipo_perc == "1":
        percentagem = float(input("Digite a percentagem: "))
        numero = float(input("Digite o número: "))
        resultado = (percentagem / 100) * numero
        print(f"{percentagem}% de {numero} é: {resultado}")

    elif tipo_perc == "2":
        numero = float(input("Digite o número: "))
        percentagem = float(input("Digite a percentagem de aumento: "))
        resultado = numero + (numero * percentagem / 100)
        print(f"{numero} + {percentagem}% = {resultado}")

    elif tipo_perc == "3":
        numero = float(input("Digite o número: "))
        percentagem = float(input("Digite a percentagem de desconto: "))
        resultado = numero - (numero * percentagem / 100)
        print(f"{numero} - {percentagem}% = {resultado}")

    else:
        print("Opção inválida!")

elif operacao == "6":
    numero = float(input("Digite o número para calcular a raiz quadrada: "))
    
    if numero < 0:
        print("Erro: Não é possível calcular raiz quadrada de número negativo!")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é: {resultado}")

elif operacao == "7":
    numero = float(input("Digite o número para calcular a raiz cúbica: "))
    resultado = numero ** (1/3)
    print(f"A raiz cúbica de {numero} é: {resultado}")

elif operacao == "8":
    print("\n--- Escolha o tipo de elevação ---")
    print("1 : Um número elevado a um expoente (Ex: 2³)")
    print("2 : Múltiplos números elevados")
    tipo_elev = input("Escolhe (1 ou 2): ")
    
    if tipo_elev == "1":
        numero = float(input("Digite o número: "))
        expoente = float(input("Digite o expoente: "))
        resultado = numero ** expoente
        print(f"{numero}^{expoente} = {resultado}")
    
    elif tipo_elev == "2":
        resultado = 1
        for i in range(qtd):
            numero = float(input(f"Digite o {i+1}º número: "))
            expoente = float(input(f"Digite o expoente para {numero}: "))
            resultado *= numero ** expoente
        print(f"O resultado da multiplicação das potências é: {resultado}")
    
    else:
        print("Opção inválida!")

elif operacao == "9":
    print("\n--- Escolha a operação com Pi ---")
    print("1 : Área de um círculo (π × r²)")
    print("2 : Perímetro de um círculo (2 × π × r)")
    print("3 : Área de uma esfera (4 × π × r²)")
    print("4 : Volume de uma esfera ((4/3) × π × r³)")
    print("5 : Volume de um cilindro (π × r² × h)")
    
    tipo_pi = input("Escolha (1 a 5): ")
    
    if tipo_pi == "1":
        raio = float(input("Digite o raio: "))
        resultado = math.pi * (raio ** 2)
        print(f"Área do círculo: {resultado}")
    
    elif tipo_pi == "2":
        raio = float(input("Digite o raio: "))
        resultado = 2 * math.pi * raio
        print(f"Perímetro do círculo: {resultado}")
    
    elif tipo_pi == "3":
        raio = float(input("Digite o raio: "))
        resultado = 4 * math.pi * (raio ** 2)
        print(f"Área da esfera: {resultado}")
    
    elif tipo_pi == "4":
        raio = float(input("Digite o raio: "))
        resultado = (4/3) * math.pi * (raio ** 3)
        print(f"Volume da esfera: {resultado}")
    
    elif tipo_pi == "5":
        raio = float(input("Digite o raio: "))
        altura = float(input("Digite a altura: "))
        resultado = math.pi * (raio ** 2) * altura
        print(f"Volume do cilindro: {resultado}")
    
    else:
        print("Opção inválida!")

else:
    print("Operação inválida!")
