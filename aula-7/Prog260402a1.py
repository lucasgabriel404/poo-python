class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Atributo PÚBLICO
        self.__saldo = saldo_inicial    # Atributo PRIVADO (encapsulado)

    # Método PÚBLICO: Qualquer um pode chamar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__registrar_operacao("Depósito") # Chama um método privado
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    # Método PÚBLICO: Qualquer um pode chamar
    def retirar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                self.__registrar_operacao("Retirada") # Chama um método privado
                print(f"Retirada de R$ {valor:.2f} realizado.")
            else:
                print(f"O valor ({valor:.2f}) é maior do que o saldo ({self.__saldo:.2f})")
        else:
            print("Valor da retirada inválido.")

    # Método PRIVADO: Só a própria classe usa internamente
    def __registrar_operacao(self, tipo):
        print(f"Log interno: Operação de {tipo} registrada no sistema.")

    # Método PÚBLICO para acessar o dado privado (Getter)
    def consultar_saldo(self):
        return f"Saldo atual de {self.titular}: R$ {self.__saldo:.2f}"

def consiste(ini: int, fim: int):
    if ini > fim: ini, fim = fim, ini
    erro = True
    while erro:
        try:
            prompt = f"Número no intervalo [{ini} - {fim}]:"
            num = int(input(prompt))
            if ini <= num <= fim: erro = False
        except ValueError: erro = True
        if erro: print("Número errado! Digite novamente!")
    return num

def movimentos(correntista):
    while True:
        print("Entre com o número do orrentista entre 1 e 4")
        print("Se entrar com 0, o programa termina")
        NumCorrentista = consiste(0,4)
        if NumCorrentista == 0: break
        else: NumCorrentista -= 1
        print(correntista[NumCorrentista].consultar_saldo())
        while True:
            valor = consiste(-10000,10000)
            if valor<0: correntista[NumCorrentista].retirar(valor*(-1))
            elif valor>0: correntista[NumCorrentista].depositar(valor)
            else: break
            print(correntista[NumCorrentista].consultar_saldo())
    print("Fim dos movimentos!!!")

# --- Programa Principal ---
if __name__ == "__main__":

    # Lista de correntistas
    correntista =   [ContaBancaria("Antonio", 1000.00),
                     ContaBancaria("Rogério", 100.00),
                     ContaBancaria("Machado", 500.00),
                     ContaBancaria("Ramos", 2000.00)]
    
    # Chama movimentos
    movimentos(correntista)
    
    # 3. Tentativa de acesso direto ao PRIVADO:
    # print(correntista[0].__saldo) # Isso causaria um AttributeError!
    # corentista[1].__registrar_operacao("Fraude") # Isso também falha!
