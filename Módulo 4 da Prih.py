#Variáveis: formas de atribuição
#Atribuição direta
a = 10
b = 20
#Múltiplas atribuições
x, y, z = 1, 2, 3
#Troca de valores entre variáveis
a, b = b, a
#Isso não dá escalabilidade para o código, é capacidade de generalizar as funções
#Exibir valores
print("a:", a)
print("b:", b)
print("x, y, z:", x, y, z)


##Programação em Python
#Uso da função eval e da clausula try-except
#Fazer função e ecapsulando, solictar dados para o usuário e exibir resultado
#Tomar cuidade com sintaxe

def calcular_expressao():
    #Solicitar ao usuário que insira uma expressão matemática
    expressao = input("Digite uma expressão matemática:")

    try:
        # Avaliar a expressão usando aval
        resultado = eval(expressao)
        print("O resultado da expressão é:", resultado)
    except Exception as e:
        print("Erro ao calcular expressão:", e)
        calcular_expressao()


print(calcular_expressao())

#Formatação de dados de saída
#oferece maneiras de formatar a saída
#é o que o usuário vê
# uso de 'print()', #metodo 'format()', e f-strings

nome = "João"
idade = 25
altura = 1.75

#Formnatação usando o f-string python 3.6+
saida_formatada = f"Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}m"
print(saida_formatada)

#Impressão de sequências
seq = [1, 2, 3]
print(seq)

#Para imprimir uma substring, por exemplo, basta utilizar os colchetes
# para indicar o intervalo de índices que deve ser impresso.

str = "Hello World"
print(str[0:4])
print(str[:2:8])
print(str[::-1])
print(str[8:2:-1])

#Atribuição, entrada e saída de dados na prática

nome = "Alice"
idade = 30
#Entrada de dados do usuário
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite sua peso em kg: "))
#Cálculo do IMC (Índice de massa coporal)
imc = peso / (altura ** 2)
#Saída de dados formatada
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Peso: {peso:.1f}")
print(f"IMC: {imc:.2f}")

#Teste de Supermercado
#Adicionando os itens como variáveis com valores
arroz = 15.99
feijao = 4.99
penne = 7.89

#Solicitar ao usuário a quantidade de cada item usando número inteiros
quantidade_arroz = int(input("Digite a quantidade de pacotes de arroz:"))
quantidade_feijao = int(input("Digite a quantidade de pacotes de feijão:"))
quantidade_penne = int(input("Digite a quantidade de pacotes de penne:"))

#Calcular o preço dos pacotes
preco_total = (arroz * quantidade_arroz) + (feijao * quantidade_feijao) + (penne * quantidade_penne)

#Saída com o valor total do pedido
print("Arroz: ", arroz)
print("Quantidade: ", quantidade_arroz)
print("=", {arroz * quantidade_arroz})

print("Feijão:", feijao)
print("Quantidade: ", quantidade_feijao)
print("=", {feijao * quantidade_feijao})

print("Penne:", penne)
print("Quantidade: ", quantidade_penne)
print("=", {penne * quantidade_penne})

print(f"O Valor total: {preco_total:.2f}")

