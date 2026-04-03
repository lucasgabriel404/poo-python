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
    def saque(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__registrar_operacao("Saque") # Chama um método privado
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Valor de Saque inválido.")

    # Método PRIVADO: Só a própria classe usa internamente
    def __registrar_operacao(self, tipo):
        print(f"Log interno: Operação de {tipo} registrada no sistema.")

    # Método PÚBLICO para acessar o dado privado (Getter)
    def consultar_saldo(self):
        return f"Saldo atual de {self.titular}: R$ {self.__saldo:.2f}"

def movimento(contabancaria:ContaBancaria):
    while(True):
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Consultar Saldo')
        print('0 - Sair')
        opcao_selecionada = input('Digite a opção desejada: ')
        
        match opcao_selecionada:
            case '1':
                contabancaria.depositar(float(input('Digite o valor do depósito: ')))
            case '2':
                contabancaria.saque(float(input('Digite o valor do saque: ')))
            case '3':
                contabancaria.consultar_saldo()
            case '0':
                print("Desligando.")
                break
            case _:
                print("Opção Inválida.")



# --- Programa Principal ---
if __name__ == "__main__":
    minha_conta = ContaBancaria("Lucas", 500.00)

    # 1. Acesso Público: Funciona normalmente
    print(f"Titular: {minha_conta.titular}")
    
    # 2. Uso de métodos públicos:
    minha_conta.depositar(500)
    print(minha_conta.consultar_saldo())

    minha_conta.saque(500)
    print(minha_conta.consultar_saldo())

    movimento(minha_conta)



    # 3. Tentativa de acesso direto ao PRIVADO:
    #print(minha_conta.__saldo) # Isso causaria um AttributeError!
    #minha_conta.__registrar_operacao("Fraude") # Isso também falha!