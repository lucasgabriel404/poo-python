class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor

class CarrinhoCompras:
    def __init__(self):
        self.__lista_produtos = []

    def adiciona_produto(self,produto):
        self.__lista_produtos.append(produto)

    def exibe_valor_total(self):
        soma = 0
        for produto in self.__lista_produtos:
            soma += produto.valor

        print(f'O valor total dos produtos é R${soma:.2f}.')

if __name__=='__main__':

    carrinho = CarrinhoCompras()
    produto1 = Produto('Celular',200)
    produto2 = Produto('Teclado',350)
    produto3 = Produto('Monitor',650)

    carrinho.adiciona_produto(produto1)
    carrinho.adiciona_produto(produto2)
    carrinho.adiciona_produto(produto3)

    carrinho.exibe_valor_total()

