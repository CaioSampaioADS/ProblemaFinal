from Problemas.githubProjetoFinal.Models import Categoria, Estoque, Produto

class DaoCategoria:

    @classmethod
    def salvar(cls):

        with open('categoria.txt', 'w') as arq:
            for i in Categoria.categoria:
                arq.writelines(i)
                arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        Categoria.categoria = cls.categoria

class DaoEstoque:
    @classmethod
    def salvar(cls):
        with open('estoque.txt', 'w') as arq:
            for i in Estoque.estoque:
                arq.writelines(i['produto'].nome + "|" + i['produto'].preco + "|" + i['produto'].categoria + "|" + str(i['quantidade']))
                arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        Estoque.estoque.clear()
        for i in cls.estoque:
            Estoque.estoque.append({
                'produto': Produto(i[0], i[1], i[2]),
                'quantidade': i[3]
            })







Estoque.estoque.append({'produto': Produto('banana', '2', 'frutas'), 'quantidade': 5})
Estoque.estoque.append({'produto': Produto('maca', '3', 'frutas'), 'quantidade': 3})

DaoEstoque.salvar()
DaoEstoque.ler()


