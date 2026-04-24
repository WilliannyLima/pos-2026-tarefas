from xml.dom import minidom

doc = minidom.parse("cardapio.xml")

pratos = doc.getElementsByTagName("prato")


print("=== CARDÁPIO ===")
for prato in pratos:
    prato_id = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.data
    print(f"{prato_id} - {nome}")


escolha = input("\nDigite o ID do prato para ver detalhes: ")

encontrado = False

for prato in pratos:
    if prato.getAttribute("id") == escolha:
        encontrado = True
        
        nome = prato.getElementsByTagName("nome")[0].firstChild.data
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.data
        preco = prato.getElementsByTagName("preco")[0].firstChild.data
        moeda = prato.getElementsByTagName("preco")[0].getAttribute("moeda")
        calorias = prato.getElementsByTagName("calorias")[0].firstChild.data
        tempo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.data
        
        print("\n=== DETALHES DO PRATO ===")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        print("Ingredientes:")
        
        ingredientes = prato.getElementsByTagName("ingrediente")
        for ing in ingredientes:
            print(f" - {ing.firstChild.data}")
        
        print(f"Preço: {preco} {moeda}")
        print(f"Calorias: {calorias}")
        print(f"Tempo de preparo: {tempo}")


if not encontrado:
    print("Prato não encontrado.")