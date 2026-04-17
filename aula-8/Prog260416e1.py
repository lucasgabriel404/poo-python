class Usuario:
    def __init__(self,senha):
        self.__senha = str(senha)

    def mudar_senha(self):
        senha_antiga = str(input('Digite a senha Antiga: '))

        if senha_antiga == self.__senha:
            nova_senha = str(input('Digite a nova senha: '))

            self.__senha = nova_senha

            print(f'Senha alterada com sucesso!')

            return

        print(f'Senha antiga inválida.')

if __name__ == '__main__':
    usuario1 = Usuario(123456)
    usuario1.mudar_senha()
            


    
