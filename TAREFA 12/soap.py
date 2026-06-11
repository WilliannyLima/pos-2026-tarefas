
import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

print("1 - Nome do País")
print("2 - Capital")
print("3 - Código Telefônico")

opcao = input("Escolha uma opção: ")
codigo = input("Digite o código do país (BR, US, FR...): ")

if opcao == "1":
    funcao = "CountryName"
    resultado = "m:CountryNameResult"

elif opcao == "2":
    funcao = "CountryCapital"
    resultado = "m:CountryCapitalResult"

elif opcao == "3":
    funcao = "CountryIntPhoneCode"
    resultado = "m:CountryIntPhoneCodeResult"

else:
    print("Opção inválida!")
    exit()

payload = f"""
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>{codigo}</sCountryISOCode>
        </{funcao}>
    </soap:Body>
</soap:Envelope>
"""

headers = {
    "Content-Type": "text/xml; charset=utf-8"
}

response = requests.post(url, headers=headers, data=payload)

xml = parseString(response.text)

valor = xml.getElementsByTagName(resultado)[0].firstChild.nodeValue

print("Resultado:", valor)
