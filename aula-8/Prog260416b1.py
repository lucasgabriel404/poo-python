import random

class Termometro:
    def __init__(self,temperatura_atual):
        self.__temperatura_atual = temperatura_atual
    
    def ler_temperatura(self):
        print(f'A temperatura atual é {self.__temperatura_atual}ºC.')

    def mudar_temperatura(self,graus):
        self.__temperatura_atual += graus

if __name__ == "__main__":

    termometro = Termometro(25.5)
    
    termometro.ler_temperatura()

    termometro.mudar_temperatura(-5)

    termometro.ler_temperatura()

    termometro.mudar_temperatura(15)

    termometro.ler_temperatura()
