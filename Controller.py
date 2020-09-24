from Models import Categoria, Estoque, Produto, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
        else:
            print('A categoria já existe em nossa base de dados, por favor digite outra')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()

        print("")
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        #TODO: colocar sem categoria nos produtos com a categoriaRemover

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                try:
                    x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                    print('Categoria alterada com sucesso')
                except:
                    print('Erro')
            else:
                print('A categoria para qual está alterando já existe')
        else:
            print('A categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()

        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) == 0:
            produto = Produto(nome,preco, categoria)
            DaoEstoque.salvar(produto, quantidade)
            print('Produto cadastrado com sucesso')
        else:
            print('Produto já existe em estoque')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()

        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del  x[i]
                    break
        else:
            print('O produto que deseja remover não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
            print('produto removido com sucesso')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()

        est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.produto.nome == novoNome, x))
            if len(est) == 0:
                x = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x),x))
            else:
                print('Produto já cadastrado')
        else:
            print('O produto que deseja alterar não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
            print('produto alterado com sucesso')

a = ControllerEstoque()
a.alterarProduto('banana', 'jabuticaba', '3', 'fruta', '5')