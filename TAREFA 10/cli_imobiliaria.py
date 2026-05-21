import json

with open("imobiliaria.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

imoveis = dados["imovel"]

while True:
    print("\n===== MENU IMOBILIÁRIA =====")

    for imovel in imoveis:
        print(f"ID: {imovel['id']} - {imovel['descricao']}")

    escolha = input("\nDigite o ID do imóvel (ou 0 para sair): ")

    if escolha == "0":
        print("Saindo...")
        break

    encontrado = None
    for imovel in imoveis:
        if imovel["id"] == escolha:
            encontrado = imovel
            break

    if encontrado:
        print("\n===== DETALHES DO IMÓVEL =====")

        print(f"Descrição: {encontrado['descricao']}")

        print("\nProprietário:")
        print(f"Nome: {encontrado['proprietario']['nome']}")

        for tel in encontrado['proprietario']['telefones']:
            print(f"Telefone: {tel}")

        for email in encontrado['proprietario']['emails']:
            print(f"Email: {email}")

        print("\nEndereço:")
        end = encontrado['endereco']
        print(f"Rua: {end['rua']}")
        print(f"Bairro: {end['bairro']}")
        print(f"Cidade: {end['cidade']}")
        print(f"Número: {end['numero']}")

        print("\nCaracterísticas:")
        car = encontrado['caracteristicas']
        print(f"Tamanho: {car['tamanho']}")
        print(f"Quartos: {car['numQuartos']}")
        print(f"Banheiros: {car['numBanheiros']}")

    else:
        print("ID não encontrado!")