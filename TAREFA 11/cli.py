import users_wrapper as users

while True:

    print("\n===== MENU =====")
    print("1 - Listar clientes")
    print("2 - Buscar cliente")
    print("3 - Criar cliente")
    print("4 - Atualizar cliente")
    print("5 - Deletar cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # LISTAR
    if opcao == "1":
        try:
            clientes = users.list()

            if clientes:
                print(f"\n--- {len(clientes)} clientes encontrados ---")

                for cliente in clientes:
                    print(
                        f"ID: {cliente.get('id')} | "
                        f"Nome: {cliente.get('nome')} | "
                        f"Email: {cliente.get('email')} | "
                        f"Telefone: {cliente.get('telefone', 'N/A')}"
                    )
            else:
                print("Nenhum cliente encontrado.")

        except Exception as e:
            print(f"Erro: {e}")

    # BUSCAR
    elif opcao == "2":
        try:
            cliente_id = input("ID do cliente: ")

            cliente = users.read(cliente_id)

            if cliente:
                print("\n--- Cliente encontrado ---")
                print(f"ID: {cliente.get('id')}")
                print(f"Nome: {cliente.get('nome')}")
                print(f"Email: {cliente.get('email')}")
                print(f"Telefone: {cliente.get('telefone', 'N/A')}")
            else:
                print("Cliente não encontrado.")

        except Exception as e:
            print(f"Erro: {e}")

    # CRIAR
    elif opcao == "3":
        try:
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")

            dados = {
                "nome": nome,
                "email": email,
                "telefone": telefone
            }

            resultado = users.create(dados)

            print("\nCliente criado com sucesso!")
            print(resultado)

        except Exception as e:
            print(f"Erro: {e}")

    # ATUALIZAR
    elif opcao == "4":
        try:
            cliente_id = input("ID do cliente: ")

            dados = {
                "nome": input("Novo nome: "),
                "email": input("Novo email: "),
                "telefone": input("Novo telefone: ")
            }

            resultado = users.update(cliente_id, dados)

            print("\nCliente atualizado!")
            print(resultado)

        except Exception as e:
            print(f"Erro: {e}")

    # DELETAR
    elif opcao == "5":
        try:
            cliente_id = input("ID do cliente: ")

            resultado = users.delete(cliente_id)

            print(resultado)

        except Exception as e:
            print(f"Erro: {e}")

    # SAIR
    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")