# 1. Definição da Classe (O Molde/Projeto)
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca      # Atributo
        self.modelo = modelo    # Atributo
        self.ligado = False     # Atributo com valor inicial

    def ligar(self):            # Método (Comportamento)
        if self.ligado == False:
            self.ligado = True
            print(f"O {self.modelo} está ligado! Vrummm!")
        else: print(f"O {self.modelo} já estava ligado! Vruuuuuummm!")

    def desligar(self):         # Método (Comportamento)
        if self.ligado == True:
            self.ligado = False
            print(f"O {self.modelo} está desligado!")
        else: print(f"O {self.modelo} já estava desligado!")

# 2. Programa Principal (Uso da Classe)
if __name__ == "__main__":
    # Instanciando objetos (Criando os carros reais)
    meu_carro = Carro("Toyota", "Corolla")
    carro_do_professor = Carro("Ford", "Mustang")

    # Acessando dados e executando ações
    print(f"Meu carro é um {meu_carro.modelo}")
    carro_do_professor.ligar()
    carro_do_professor.ligar()
    carro_do_professor.desligar()
    carro_do_professor.desligar()
    meu_carro.desligar()
