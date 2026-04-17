class Calculadora:
    def somar(self,x,y):
        return x+y
    
    def subtrair(self,x,y):
        return x-y
    
    def multiplicar(self,x,y):
        return x*y
    
    def dividir(self,x,y):
        return x/y
    
if __name__=='__main__':
    calc = Calculadora()

    print(f'A soma é {calc.somar(1,8)}.')
    print(f'A subtração é {calc.subtrair(98,512)}.')
    print(f'A multiplicação é {calc.multiplicar(4,2)}.')
    print(f'A divisão é {calc.dividir(80,8)}.')