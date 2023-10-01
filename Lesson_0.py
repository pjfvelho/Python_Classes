
#Primeiro comando

print("Hello World")

# Fazer: Mudar a mensagem

print("Escrever a nova mensagem aqui!")


# Criar variáveis
num_anos = 4
dias_por_ano = 365 
horas_por_dia = 24
mins_por_hora = 60
segs_por_min = 60


# Calcular o número de sugundos em 4 anos
total_secs = segs_por_min * mins_por_hora * horas_por_dia * dias_por_ano * num_anos
print(total_secs)



# TODO: Set the value of the births_per_min variable
births_per_min = 250

# TODO: Set the value of the births_per_day variable
births_per_day = births_per_min * mins_per_hour * hours_per_day


#Conteúdo 2: Exemplo de estrutura condicional (if-else)

idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


#Conteúdo 3: Exemplo de loop for para listar números pares

for i in range(2, 11, 2):
    print(i)


#Conteúdo 4: Exemplo de função para calcular a média de uma lista de números

def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("A média dos números é:", media)


#Conteúdo 5: Exemplo de leitura e escrita em arquivos de texto

# Escrevendo em um arquivo
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")

# Lendo de um arquivo
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


# Definir função
def add_three(input_var):
    output_var = input_var + 3
    return output_var


# Run the function with 10 as input
new_number = add_three(10)

# Check that the value is 13, as expected
print(new_number)
