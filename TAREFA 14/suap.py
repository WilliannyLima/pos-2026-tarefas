import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {
    "username": user,
    "password": password
}

response = requests.post(
    api_url + "token/pair",
    json=data
)

token = response.json()["access"]

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    api_url + "ensino/meu-boletim/2025/1/",
    headers=headers
)

print(response.json())
boletim = response.json()
print("-" * 100)
print(f"{'Disciplina':45} {'N1':>5} {'N2':>5} {'N3':>5} {'N4':>5}")
print("-" * 100)

for disciplina in boletim["results"]:
    n1 = disciplina["nota_etapa_1"]["nota"]
    n2 = disciplina["nota_etapa_2"]["nota"]
    n3 = disciplina["nota_etapa_3"]["nota"]
    n4 = disciplina["nota_etapa_4"]["nota"]

    print(
        f"{disciplina['disciplina'][:45]:45} "
        f"{str(n1):>5} "
        f"{str(n2):>5} "
        f"{str(n3):>5} "
        f"{str(n4):>5}"
    )