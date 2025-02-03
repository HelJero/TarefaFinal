from abc import ABC, abstractmethod

# Classe abstrata para representar uma despesa genérica
class Despesa(ABC):
    def __init__(self, valor=0):	#Inicia a despesa com um valor de 0.
        self.valor = valor

    @abstractmethod
    def tipo(self):		#Método abstrato que será implementado nas subclasses para definir o tipo de despesa.
        pass

# Classes derivadas que representam tipos específicos de despesas
class Renda(Despesa):
    def tipo(self):		#Devolve o nome da despesa como 'Renda'.
        return "Renda"

class Eletricidade(Despesa):
    def tipo(self):		#Devolve o nome da despesa como 'Eletricidade'.
        return "Eletricidade"

class Agua(Despesa):
    def tipo(self):		#Devolve o nome da despesa como 'Água'.
        return "Água"

class Internet(Despesa):
    def tipo(self):		#Devolve o nome da despesa como 'Internet'.
        return "Internet"

class Combustivel(Despesa):
    def tipo(self):		#Devolve o nome da despesa como 'Combustíveis'.
        return "Combustíveis"

class Supermercado(Despesa):
    def tipo(self):		#Devolve o nome da despesa como 'Supermercado'.
        return "Supermercado"

# Função para garantir que o utilizador insere um valor numérico válido

def obter_valor(nome_despesa):    #Solicita ao utilizador um valor para a despesa e garante que seja um número positivo.
                                    #Se o utilizador inserir um valor inválido, pedirá a correção.
    while True:
        try:
            valor = float(input(f"Insira o valor da despesa de {nome_despesa} (€): "))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Por favor, introduza um número válido.")

print("=== Cálculo das Despesas Mensais ===")
print("")

# Criar lista de despesas e pedir ao utilizador os valores
despesas = [
    Renda(obter_valor("Renda")),
    Eletricidade(obter_valor("Eletricidade")),
    Agua(obter_valor("Água")),
    Internet(obter_valor("Internet")),
    Combustivel(obter_valor("Combustíveis")),
    Supermercado(obter_valor("Supermercado"))
]

# Calcular o total das despesas
total_despesas = sum(despesa.valor for despesa in despesas)

# Exibir resultados no ecrã
print("\n=== Resumo das Despesas ===")
print("")
for despesa in despesas:
    print(f"{despesa.tipo()}: €{despesa.valor:.2f}")
print("")
print(f"Total das despesas mensais: €{total_despesas:.2f}")

# Guardar os resultados num ficheiro
with open("despesas.txt", "w") as ficheiro:
    ficheiro.write("=== Resumo das Despesas Mensais ===\n")
    for despesa in despesas:
        ficheiro.write(f"{despesa.tipo()}: €{despesa.valor:.2f}\n")
    ficheiro.write(f"Total das despesas: €{total_despesas:.2f}\n")

print("\nOs dados foram guardados no ficheiro 'despesas.txt'.")

