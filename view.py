from Controller import ControllerCategoria, ControllerEstoque, ControllerFornecedor, ControllerCliente, ControllerFuncionario

if __name__ == "__main__":
    local = int(input("Digite 1 para acessar ( Categorias )\n"
              "Digite 2 para acessar ( Estoque )\n"
              "Digite 3 para acessar ( Fornecedor )\n"
              "Digite 4 para acessar ( Cliente )\n"
              "Digite 5 para acessar ( Funcionario )\n"))

    if local == 1:
        while True:
            decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                "Digite 2 para remover uma categoria\n"
                                "Digite 3 para alterar uma categoria\n"
                                "Digite 4 para sair\n"))

            if decidir == 1:
                categoria = input("Digite a categoria que deseja cadastrar\n")
                cat = ControllerCategoria()
                cat.cadastraCategoria(categoria)
            elif decidir == 2:
                categoria = input("Digite a categoria que deseja remover\n")
                cat = ControllerCategoria()
                cat.removerCategoria(categoria)
            elif decidir == 3:
                categoria = input("Digite a categoria que deseja alterar\n")
                novaCategoria = input("Digite a categoria para qual deseja alterar\n")
                cat = ControllerCategoria()
                cat.alterarCategoria(categoria, novaCategoria)
            else:
                break

    elif local == 2:
        while True:
            decidir = int(input("Digite 1 para cadastrar um produto\n"
                                "Digite 2 para remover um produto\n"
                                "Digite 3 para alterar um produto\n"
                                "Digite 4 para sair\n"))

            if decidir == 1:
                nome = input("Digite o nome do produto: \n")
                preco = input("Digite o preco do produto: \n")
                categoria = input("Digite a categoria do produto: \n")
                quantidade = input("Digite a quantidade do produto: \n")
                cat = ControllerEstoque()
                cat.cadastrarProduto(nome, preco, categoria, quantidade)
            elif decidir == 2:
                produto = input("Digite o produto que deseja remover: \n")
                cat = ControllerEstoque()
                cat.removerProduto(produto)
            elif decidir == 3:
                nomeAlterar = input("Digite o nome do produto que deseja alterar: \n")
                nome = input("Digite o novo nome do produto: \n")
                preco = input("Digite o novo preco do produto: \n")
                categoria = input("Digite a nova categoria do produto: \n")
                quantidade = input("Digite a nova quantidade do produto: \n")
                cat = ControllerEstoque()
                cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)
            else:
                break

    elif local == 3:
        while True:
            decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                "Digite 2 para remover um fornecedor\n"
                                "Digite 3 para alterar um fornecedor\n"
                                "Digite 4 para sair\n"))

            if decidir == 1:
                nome = input("Digite o nome do fornecedor: \n")
                cnpj = input("Digite o cnpj do fornecedor: \n")
                telefone = input("Digite o telefone do fornecedor: \n")
                categoria = input("Digite a categoria fornecida: \n")
                cat = ControllerFornecedor()
                cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
            elif decidir == 2:
                fornecedor = input("Digite o fornecedor que deseja remover: \n")
                cat = ControllerFornecedor()
                cat.removerFornecedor(fornecedor)
            elif decidir == 3:
                nomeAlterar = input("Digite o nome do fornecedor que deseja alterar: \n")
                novoNome = input('Digite o novo nome do fornecedor: \n')
                novoCnpj = input('Digite o novo cnpj do fornecedor: \n')
                novoTelefone = input('Digite o novo telefone do fornecedor: \n')
                novoCategoria = input('Digite a nova categoria fornecida: \n')

                cat = ControllerFornecedor()
                cat.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria)
            else:
                break

    elif local == 4:
        while True:
            decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                "Digite 2 para remover um cliente\n"
                                "Digite 3 para alterar um cliente\n"
                                "Digite 4 para sair\n"))

            if decidir == 1:
                nome = input("Digite o nome do cliente: \n")
                telefone = input("Digite o telefone do cliente: \n")
                cpf = input("Digite o cpf do cliente: \n")
                email = input("Digite o email do cliente: \n")
                endereco = input("Digite o endereço do cliente: \n")
                cat = ControllerCliente()
                cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
            elif decidir == 2:
                cliente = input("Digite o cliente que deseja remover: \n")
                cat = ControllerCliente()
                cat.removerCliente(cliente)
            elif decidir == 3:
                nomeAlterar = input("Digite o nome do cliente que deseja alterar: \n")
                novoNome = input("Digite o novo nome do cliente: \n")
                novoTelefone = input("Digite o novo telefone do cliente: \n")
                novoCpf = input("Digite o novo cpf do cliente: \n")
                novoEmail = input("Digite o novo email do cliente: \n")
                novoEndereco = input("Digite o novo endereço do cliente: \n")

                cat = ControllerCliente()
                cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
            else:
                break

    elif local == 5:
        while True:
            decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                "Digite 2 para remover um funcionario\n"
                                "Digite 3 para alterar um funcionario\n"
                                "Digite 4 para sair\n"))

            if decidir == 1:
                clt = input("Digite a clt do funcionario: \n")
                nome = input("Digite o nome do funcionario: \n")
                telefone = input("Digite o telefone do funcionario: \n")
                cpf = input("Digite o cpf do funcionario: \n")
                email = input("Digite o email do funcionario: \n")
                endereco = input("Digite o endereço do funcionario: \n")
                cat = ControllerFuncionario()
                cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
            elif decidir == 2:
                funcionario = input("Digite o funcionario que deseja remover: \n")
                cat = ControllerFuncionario()
                cat.removerFuncionario(funcionario)
            elif decidir == 3:
                nomeAlterar = input("Digite o nome do funcionario que deseja alterar: \n")
                novoClt = input("Digite a nova clt do funcionario: \n")
                novoNome = input("Digite o novo nome do funcionario: \n")
                novoTelefone = input("Digite o novo telefone do funcionario: \n")
                novoCpf = input("Digite o novo cpf do funcionario: \n")
                novoEmail = input("Digite o novo email do funcionario: \n")
                novoEndereco = input("Digite o novo endereço do funcionario: \n")

                cat = ControllerFuncionario()
                cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
            else:
                break
