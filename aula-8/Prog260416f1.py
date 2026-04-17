class RelogioDigital:
    def __init__(self):
        self.__horas = 0
        self.__minutos = 0

    def exibe_horario(self):
        print(f'{self.__horas:02}:{self.__minutos:02}')
    
    def mudar_horario(self):
        new_horas = self.__consiste(0,23,'horas')
        new_minutos = self.__consiste(0,59,'minutos')

        self.__horas = new_horas
        self.__minutos = new_minutos

        print(f'Horário alterado!')

    def __consiste(self,ini: int, fim: int, variavel:str):
        if ini > fim: ini, fim = fim, ini
        num = fim + 1
        erro = True
        while erro:
            try:
                prompt = f"Digite o novo valor para {variavel} [{ini} - {fim}]:"
                num = int(input(prompt))
                if ini <= num <= fim: erro = False
            except ValueError: erro = True
            if erro: print("Número inválido! Digite novamente!")
        
        return num

if __name__ == '__main__':
    relogio = RelogioDigital()

    relogio.exibe_horario()

    relogio.mudar_horario()

    relogio.exibe_horario()