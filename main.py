# Script para cálculo do Índice de Massa Corporal (IMC)

# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para interpretar o IMC
def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidade"
    else:
        return "Valor inválido"

# Entrada de dados do usuário
peso = float(input("Informe seu peso em kg (ex: 70.5): "))
altura = float(input("Informe sua altura em metros (ex: 1.75): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Exibindo o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Sua Classificação: {interpretar_imc(imc)}")
