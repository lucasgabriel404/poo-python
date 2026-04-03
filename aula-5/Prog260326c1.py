# 1. SUPERCLASSE (A base comum para todos)
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Salário: R$ {self.salario:.2f}")

# 2.1. SUBCLASSE (Especialização do funcionário)
class Gerente(Funcionario): # <--- Indica que Gerente HERDA de Funcionario
    def __init__(self, nome, salario, bonus):
        # O super() chama o construtor da Superclasse para preencher nome e salario
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_total(self):
        total = self.salario + self.bonus
        print(f"Total com bônus do Gerente: R$ {total:.2f}")

# 2.2. SUBCLASSE (Especialização do funcionário)
class Minion(Funcionario): # <--- Indica que Minion HERDA de Funcionario
    def __init__(self, nome, salario, bonus):
        # O super() chama o construtor da Superclasse para preencher nome e salario
        super().__init__(nome, salario)
        self.bonus = bonus/2

    def calcular_total(self):
        total = self.salario + self.bonus
        print(f"Total com bônus do Minion: R$ {total:.2f}")

# 3. PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Criando objetos da Subclasse
    g1 = Gerente("Antonio", 5000, 1500)
    m1 = Minion("Kevin",2500,1000)
    # Os objetos conseguem usar métodos da Superclasse (exibir_dados)
    # e métodos próprios (calcular_total)
    g1.exibir_dados()
    g1.calcular_total()
    m1.exibir_dados()
    m1.calcular_total()
