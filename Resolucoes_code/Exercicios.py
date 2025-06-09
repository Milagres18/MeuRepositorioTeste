def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = dado1 + dado2
    print("Resultado da concatenação:", resultado)

def repetir_texto():
    texto = input("Digite o texto: ")
    repeticoes = int(input("Digite o número de repetições: "))
    print("Resultado:", texto * repeticoes)

def operacoes_matematicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print("Resultado da soma:", soma)

def verificar_par_ou_impar():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print("A média das notas é:", round(media, 2))

def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    if palavra == palavra[::-1]:
        print("É um palíndromo
