from abc import ABC, abstractmethod  # Importa as classes ABC e abstractmethod para definir classes abstratas

# Classe abstrata para representar uma despesa genérica
class Despesa(ABC):  # Classe base que representa uma despesa genérica, herdada por outras classes
    def __init__(self, valor=0):  # Inicia a despesa com um valor 0
        self.valor = valor  # Atribui o valor da despesa à instância

    @abstractmethod
    def tipo(self):  # Método abstrato que será implementado nas subclasses para definir o tipo de despesa
        pass  # Passa sem implementação aqui, será obrigatoriamente implementado nas subclasses

# Classes derivadas que representam tipos específicos de despesas
class Renda(Despesa):  # Classe derivada que representa a despesa de 'Renda'
    def tipo(self):  # Implementação do método 'tipo' para a classe 'Renda'
        return "Renda"  # Devolve o nome da despesa como 'Renda'

class Eletricidade(Despesa):  # Classe derivada que representa a despesa de 'Eletricidade'
    def tipo(self):  # Implementação do método 'tipo' para a classe 'Eletricidade'
        return "Eletricidade"  # Devolve o nome da despesa como 'Eletricidade'

class Agua(Despesa):  # Classe derivada que representa a despesa de 'Água'
    def tipo(self):  # Implementação do método 'tipo' para a classe 'Água'
        return "Água"  # Devolve o nome da despesa como 'Água'

class Internet(Despesa):  # Classe derivada que representa a despesa de 'Internet'
    def tipo(self):  # Implementação do método 'tipo' para a classe 'Internet'
        return "Internet"  # Devolve o nome da despesa como 'Internet'

class Combustivel(Despesa):  # Classe derivada que representa a despesa de 'Combustíveis'
    def tipo(self):  # Implementação do método 'tipo' para a classe 'Combustíveis'
        return "Combustíveis"  # Devolve o nome da despesa como 'Combustíveis'

class Supermercado(Despesa):  # Classe derivada que representa a despesa de 'Supermercado'
    def tipo(self):  # Implementação do método 'tipo' para a classe 'Supermercado'
        return "Supermercado"  # Devolve o nome da despesa como 'Supermercado'

# Função para garantir que o utilizador insere um valor numérico válido
def obter_valor(nome_despesa):  # Função que solicita o valor de uma despesa ao utilizador
    while True:  # Loop contínuo até o utilizador fornecer um valor válido
        try:
            valor = float(input(f"Insira o valor da despesa de {nome_despesa} (€): "))  # Solicita ao utilizador o valor da despesa
            if valor < 0:  # Verifica se o valor é negativo
                print("O valor não pode ser negativo. Tente novamente.")  # Informa o utilizador que o valor não pode ser negativo
            else:
                return valor  # Devolve o valor se for válido
        except ValueError:  # Captura erros de valor caso o utilizador insira um valor inválido
            print("Entrada inválida! Por favor, introduza um número válido.")  # Informa o utilizador sobre o erro

print("=== Cálculo das Despesas Mensais ===")  # Exibe o título do cálculo das despesas
print("")  # Linha em branco para separar o título do conteúdo

# Criar lista de despesas e pedir ao utilizador os valores
despesas = [
    Renda(obter_valor("Renda")),  # Cria uma instância de Renda com o valor obtido do utilizador
    Eletricidade(obter_valor("Eletricidade")),  # Cria uma instância de Eletricidade com o valor obtido
    Agua(obter_valor("Água")),  # Cria uma instância de Água com o valor obtido
    Internet(obter_valor("Internet")),  # Cria uma instância de Internet com o valor obtido
    Combustivel(obter_valor("Combustíveis")),  # Cria uma instância de Combustíveis com o valor obtido
    Supermercado(obter_valor("Supermercado"))  # Cria uma instância de Supermercado com o valor obtido
]

# Calcular o total das despesas
total_despesas = sum(despesa.valor for despesa in despesas)  # Soma todos os valores das despesas na lista 'despesas'

# Exibir resultados no ecrã
print("\n=== Resumo das Despesas ===")  # Exibe o título do resumo das despesas
print("")  # Linha em branco para separar o título do conteúdo
for despesa in despesas:  # Para cada despesa na lista de despesas
    print(f"{despesa.tipo()}: €{despesa.valor:.2f}")  # Exibe o tipo de despesa e o valor formatado com 2 casas decimais
print("")  # Linha em branco
print(f"Total das despesas mensais: €{total_despesas:.2f}")  # Exibe o total das despesas formatado com 2 casas decimais

# Guardar os resultados num ficheiro
with open("despesas.txt", "w") as ficheiro:  # Abre (ou cria) um arquivo chamado 'despesas.txt' no modo de escrita
    ficheiro.write("=== Resumo das Despesas Mensais ===\n")  # Escreve o título no arquivo
    for despesa in despesas:  # Para cada despesa na lista de despesas
        ficheiro.write(f"{despesa.tipo()}: €{despesa.valor:.2f}\n")  # Escreve o tipo e o valor da despesa no arquivo
    ficheiro.write(f"Total das despesas: €{total_despesas:.2f}\n")  # Escreve o total das despesas no arquivo

print("\nOs dados foram guardados no ficheiro 'despesas.txt'.")  # Informa o utilizador que os dados foram guardados no arquivo
