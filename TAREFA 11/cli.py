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

    if opcao == "1":
        try:
            clientes = users.list()
            
            
            if isinstance(clientes, list):
                if len(clientes) > 0:
                    print(f"\n--- {len(clientes)} clientes encontrados ---")
                    for cliente in clientes:
                        print(f"ID: {cliente.get('id')} | Nome: {cliente.get('nome')} | Email: {cliente.get('email')} | Telefone: {cliente.get('telefone', 'N/A')}")
                else:
                    print("Nenhum cliente encontrado.")
            else:
                
                print(f"Erro: {clientes.get('mensagem', 'Erro desconhecido')}")
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            print("Verifique se a API está rodando em http://localhost:8000")

   
    elif opcao == "2":
        try:
            cliente_id = input("ID do cliente: ")
            
           
            if not cliente_id.isdigit():
                print("Erro: ID deve ser um número válido!")
                continue
            
            cliente = users.read(int(cliente_id))
            
           
            if cliente and 'erro' not in cliente:
                print("\n--- Cliente encontrado ---")
                print(f"ID: {cliente.get('id')}")
                print(f"Nome: {cliente.get('nome')}")
                print(f"Email: {cliente.get('email')}")
                print(f"Telefone: {cliente.get('telefone', 'N/A')}")
            else:
                print(f"Cliente com ID {cliente_id} não encontrado.")
        except ValueError:
            print("Erro: ID inválido!")
        except Exception as e:
            print(f"Erro ao buscar cliente: {e}")
            print("Verifique se a API está rodando em http://localhost:8000")

 
    elif opcao == "3":
        try:
            nome = input("Nome: ")
            
            if not nome.strip():
                print("Erro: Nome não pode estar vazio!")
                continue
            
            email = input("Email: ")
            if not email.strip():
                print("Erro: Email não pode estar vazio!")
                continue
            
            telefone = input("Telefone: ")
            
            cliente = users.create(nome, email, telefone)
            
            
            if cliente and 'erro' not in cliente:
                print("\n✅ Cliente criado com sucesso!")
                print(f"ID: {cliente.get('id')}")
                print(f"Nome: {cliente.get('nome')}")
                print(f"Email: {cliente.get('email')}")
                print(f"Telefone: {cliente.get('telefone', 'N/A')}")
            else:
                print(f"❌ Erro ao criar cliente: {cliente.get('mensagem', 'Erro desconhecido')}")
        except Exception as e:
            print(f"Erro ao criar cliente: {e}")
            print("Verifique se a API está rodando em http://localhost:8000")

    
    elif opcao == "4":
        try:
            cliente_id = input("ID do cliente: ")
            
            
            if not cliente_id.isdigit():
                print("Erro: ID deve ser um número válido!")
                continue
            
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            
            
            if not nome and not email and not telefone:
                print("Erro: Informe pelo menos um campo para atualizar!")
                continue
            
            cliente = users.update(int(cliente_id), nome, email, telefone)
            
            
            if cliente and 'erro' not in cliente:
                print("\n✅ Cliente atualizado com sucesso!")
                print(f"ID: {cliente.get('id')}")
                print(f"Nome: {cliente.get('nome')}")
                print(f"Email: {cliente.get('email')}")
                print(f"Telefone: {cliente.get('telefone', 'N/A')}")
            else:
                print(f"❌ Erro ao atualizar cliente: {cliente.get('mensagem', 'Cliente não encontrado')}")
        except ValueError:
            print("Erro: ID inválido!")
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            print("Verifique se a API está rodando em http://localhost:8000")

   
    elif opcao == "5":
        try:
            cliente_id = input("ID do cliente: ")
            
            
            if not cliente_id.isdigit():
                print("Erro: ID deve ser um número válido!")
                continue
            
            
            confirmar = input(f"Tem certeza que deseja deletar o cliente ID {cliente_id}? (s/N): ")
            
            if confirmar.lower() == 's':
                resultado = users.delete(int(cliente_id))
                
                
                if resultado and 'erro' not in resultado:
                    print(f"✅ {resultado.get('mensagem', 'Cliente deletado com sucesso!')}")
                else:
                    print(f"❌ Erro ao deletar cliente: {resultado.get('erro', 'Cliente não encontrado')}")
            else:
                print("Operação cancelada.")
        except ValueError:
            print("Erro: ID inválido!")
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            print("Verifique se a API está rodando em http://localhost:8000")

    
    elif opcao == "0":
        print("\nEncerrando o programa...")
        print("Até mais! 👋")
        break

    else:
        print("Opção inválida! Digite um número de 0 a 5.")