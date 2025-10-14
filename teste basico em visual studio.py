a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)

def soma(a ,b):
    return a + b
resultado = soma(3, 5)

print("A Soma é", resultado)


#Variavéis#
idade = 25
nome = "João"
altura = 1.75
#Exibir dados
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
#Manipular de dados
idade = 26
#Controle de Fluxo, usando estrutura condicional if e else
if idade >= 18:
    print(nome, "é maior de idade.")
else:
    print(nome, "é menor de idade")
