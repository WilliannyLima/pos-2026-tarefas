import xml.etree.ElementTree as ET
import json

def parse_imobiliaria(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    imobiliaria = {"imovel": []}

    for imovel in root.findall("imovel"):
        imovel_dict = {
            "id": imovel.get("id"),
            "descricao": imovel.findtext("descricao"),
        }

        prop = imovel.find("proprietario")
        proprietario = {
            "nome": prop.findtext("nome"),
            "emails": [e.text for e in prop.findall("email")],
            "telefones": [t.text for t in prop.findall("telefone")]
        }

        end = imovel.find("endereco")
        endereco = {
            "rua": end.findtext("rua"),
            "bairro": end.findtext("bairro"),
            "cidade": end.findtext("cidade"),
            "numero": end.findtext("numero")
        }

        carac = imovel.find("caracteristicas")
        caracteristicas = {
            "tamanho": carac.findtext("tamanho"),
            "numQuartos": carac.findtext("numQuartos"),
            "numBanheiros": carac.findtext("numBanheiros")
        }

        imovel_dict["proprietario"] = proprietario
        imovel_dict["endereco"] = endereco
        imovel_dict["caracteristicas"] = caracteristicas

        imobiliaria["imovel"].append(imovel_dict)

    return imobiliaria

def main():
    input_file = "imobiliaria.xml"
    output_file = "imobiliaria.json"

    dados = parse_imobiliaria(input_file)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Arquivo '{output_file}' gerado com sucesso!")


if __name__ == "__main__":
    main()