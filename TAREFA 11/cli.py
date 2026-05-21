import users_wrapper as users

while True:
    print("\n=== CRUD USERS ===")
    print("1 - Listar usuários")
    print("2 - Ler usuário")
    print("3 - Criar usuário")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        lista = users.list()

        for user in lista:
            print(f"{user['id']} - {user['name']}")

    elif opcao == "2":
        user_id = input("ID do usuário: ")

        user = users.read(user_id)

        print(user)

    elif opcao == "3":
        nome = input("Nome: ")
        email = input("Email: ")

        novo_usuario = {
            "name": nome,
            "email": email
        }

        resultado = users.create(novo_usuario)

        print(resultado)

    elif opcao == "4":
        user_id = input("ID do usuário: ")

        nome = input("Novo nome: ")
        email = input("Novo email: ")

        dados = {
            "name": nome,
            "email": email
        }

        resultado = users.update(user_id, dados)

        print(resultado)

    elif opcao == "5":
        user_id = input("ID do usuário: ")

        resultado = users.delete(user_id)

        print(resultado)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")