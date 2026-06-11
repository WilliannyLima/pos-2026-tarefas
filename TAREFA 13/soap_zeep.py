import zeep

# define a URL do WSDL
wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# solicita o número
numero = int(input("Digite um número inteiro: "))

# faz a chamada do serviço
result = client.service.NumberToWords(
    ubiNum=numero
)

# imprime o resultado
print(result)