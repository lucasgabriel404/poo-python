# abc: biblioteca Abstract Base Classes
# ABC: Superclasse. A classe que herda dela não pode ter objeto instanciado
# abstractmethod:
#  Método decorador identificado pelo símbolo @
#  Carimba os métodos que as classes filhas devem escrever
from abc import ABC, abstractmethod
import math

# 1. A CLASSE ABSTRATA (O Conceito Geral)
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        """Este método é um contrato: toda forma DEVE saber calcular sua área."""
        pass

# 2. CLASSES CONCRETAS (A Implementação Real)
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

class Equilatero(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return (self.lado**2 * (3**0.5)) / 4


# 3. PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Criando instâncias das formas
    formas = [
        Quadrado(4),
        Circulo(3),
        Equilatero(5)
    ]

    print("--- Relatório de Áreas ---")
    for f in formas:
        # O programa não sabe se é quadrado ou círculo, 
        # ele apenas confia que a 'Forma' sabe calcular_area()
        print(f"Área da forma: {f.calcular_area():.2f}")
