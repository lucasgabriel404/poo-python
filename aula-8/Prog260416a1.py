import random

class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.__paginas_lidas = 0

    def ler_pagina(self):
        self.__paginas_lidas += 1
        print(f'Uma página foi lida... {self.__paginas_lidas} foram lidas no total...')

    def __str__(self):
        return f'Título: {self.titulo} - Autor: {self.autor}.'

if __name__ == "__main__":
    lista_livros = [Livro('Entrevista com vampiro','Anne Rice'), Livro('O morro dos ventos uivantes','Emily Bronte')]

    for livro in lista_livros:
        print(livro)
        for i in range(random.randint(1, 10)):
            livro.ler_pagina()

