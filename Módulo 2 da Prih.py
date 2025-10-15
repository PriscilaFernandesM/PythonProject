# Declaração de variáveis para armazenar as dimensões do retângulo
largura = 5
altura = 3

# Cálculo da área usando as variavéis

area = largura * altura

#Exibir o resultado
print("A área do retângulo é", area)

#Declaração de uma variável para armazenar dados pessoais
nome = "Ana"
idade = 22
cidade = "São Paulo"

#Exibindo as informações
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)

#Declaração de uma variável contador
contador = 0

#USo de variável em loop para contar até 5
while contador < 5:
    print("Contador é:", contador)
    # Incrementado o valor do contador
    contador += 1


x = 10
print(x)
x = 20
print(x)

# Conceito de amarração Binding, variável e amarração de tipo
#Amarração de um inteiro a uma variável (número)
idade = 30
print("Idade:",idade)

#Amarração de uma string a mesma variável (escrita)
idade = "trinta"
print("Idade em palavras:",idade)

#Amarração de um float a uma nova variável (número quebrado por ponto)
altura = 1.75
print("Altura:",altura)

#Escopos
def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2  # a global será alterado
    print(f"Dentro da função,  variável  vale: {a}")
    return a * numero
#Defini a função que só a variável só funciona aqui dentro, no escopo local, os espacinhos com o def

a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")

#Constantes
#para que manter um valor no código que precisa ser constante, usa letra maiúscula, pois o python não tem
PI = 3.14159

#Usando a constante para cálculo
raio = 10
area = PI * (raio ** 2)

print("Área do círculo é:", area)

#Variáveis na prática
#Definir função para um número e um texto contantes, letras maiúsculas
def NUMERINHOTEXTINHO(numero, texto):
    print("Número:", numero)
    print("Texto:", texto)

#Fornecer os valores para a função, numero e string(texto, sempre colocar entre " " aspas)
numero_escolhido = 666
texto_escolhido = "Número inválido"

#Chamar a função de  NUMERINHOTEXTINHO com os valores
NUMERINHOTEXTINHO(numero_escolhido, texto_escolhido)
print(numero_escolhido, texto_escolhido)


