from abc import ABC, abstractmethod

class AnimalDeEstimacao(ABC):
    def __init__(self,especie,nome):
        self.__especie = especie
        self.__nome = nome

    def __str__(self):
        return f'O pet é {self.__especie}, e seu nome é {self.__nome}.'

class Cachorro(AnimalDeEstimacao):
    def __init__(self,nome):
        super().__init__('Cachorro',nome)

if __name__ == '__main__':

    doguinho = Cachorro('Puca') 
    print(doguinho)

