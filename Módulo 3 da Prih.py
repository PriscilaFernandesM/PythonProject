#Tipos de dados padrão
#Tipos numéricos
inteiro = 10
flutuante = 5.5
#Tipo float (flutuante) tenho que usar ponto

#Operadores numéricos
soma = inteiro + flutuante
produto = inteiro * flutuante
#Não esquecer Divisão inteira	// (usar duas,para imprimir o resultado sem valores "quebrados" e usar ** é para exponenciação

#Tipo Booleano
verdadeiro = True
falso = False

#Exibir resultados
print("Soma: ", soma)
print("Produto: ", produto)
print("Verdadeiro: ", verdadeiro)
print("Falso: ", falso)

#Relação de precedência entre operadores
resultado = 2 + 3 * 4 ** 2 / (1 + 1)

print("Resultado: ", resultado)

resultado = 2 + 3  * (4 ** 2) / (1 + 1)

print("Resultado: ", resultado)

somaintfloat = 5 + 0.78
print("Soma: ", somaintfloat)

#Conversões de tipos de dados
# Leitura de dados como strings, as ""
idade_str = "25"
altura_str = "1.66"

#Conversão de tipos
idade = int(idade_str)
altura = float(altura_str)
#Convertendo string para int e float

#Processamento usando os novos tipos de dados
mensagem = "Idade:" + str(idade) + "Altura:" + str(altura)
print(mensagem)

#Prática

def soma_numeros(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
    print("Erro: entrada inválida")
    except Exception as e:
    print(f"Erro: {e}")
    return None
# Teste da função com números básicos
print(soma_numeros(10, 20))

# Teste da função com números inválidos, número e letra
print(soma_numeros(10, a))
##Saída: Erro: entrada inválida

# Teste de função com outros tipos de dados
print(soma_numeros(True,  3))
##Saída: 4, pois o True é considerado 1 em Phyton, teoricamente é um erro, deve ser tratada na função para evitar
##Vulnerável

# Teste de função com uma lista
print(soma_numeros([1, 2], 3))
#Saída: Erro: entrada inválida

#Para fazer a média de notas
## Solicitar ao usuário as notas, lembrando que pode ser número inteiro ou decimal, int float

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

#Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

#Mostrar o resultado
print(f"A média das notas é: {media}")

#Exercício

#Solicitar os dados
numero1 = input("Digite um número inteiro:")
nummero2 = input("Digite um número de ponto flutuante:")

#Converter para tipos corretos
numero1 = int(numero1)
def numero1
    try:
        numero1 = int(numero1)
        return numero1
    except TypeError:
        print("Número inteiro False")
        return None


nummero2 = float(nummero2)
def numero2
    try:
        nummero2 = float(nummero2)
        return nummero2
    except TypeError:
        print("Número de ponto flutuante False")
        return None

#Exibindo a mensagem
print("O número:", numero1 "é inteiro e o Número:", numero2 "é flutuante")

#Resposta do professor:
numero_inteiro = int(input("Digite um número inteiro: "))
numero_flutuante = float(input("Digite um número de ponto flutuante: "))
valor_booleano = input("Digite um valor booleano (True ou False): ")
valor_booleano = valor_booleano.lower()  # Converte para minúsculas para garantir que seja reconhecido como booleano
valor_booleano = valor_booleano == "true"  # Converte para tipo bool

