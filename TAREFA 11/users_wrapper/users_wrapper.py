import requests

BASE_URL = "http://localhost:8000/users/"


def list():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"erro": True, "mensagem": str(e)}



def read(user_id):
    try:
        response = requests.get(f"{BASE_URL}/{user_id}")
        if response.status_code == 404:
            return {"erro": True, "mensagem": "Usuário não encontrado"}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"erro": True, "mensagem": str(e)}



def create(nome, email, telefone):
    try:
        payload = {
            "name": nome,
            "username": nome,
            "email": email,
            "phone": telefone
        }

        response = requests.post(BASE_URL, json=payload)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"erro": True, "mensagem": str(e)}



def update(user_id, nome=None, email=None, telefone=None):
    try:
        payload = {}

        if nome:
            payload["nome"] = nome
        if email:
            payload["email"] = email
        if telefone:
            payload["telefone"] = telefone

        response = requests.put(f"{BASE_URL}/{user_id}", json=payload)

        if response.status_code == 404:
            return {"erro": True, "mensagem": "Usuário não encontrado"}

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"erro": True, "mensagem": str(e)}



def delete(user_id):
    try:
        response = requests.delete(f"{BASE_URL}/{user_id}")

        if response.status_code == 404:
            return {"erro": True, "mensagem": "Usuário não encontrado"}

        return {"mensagem": "Usuário deletado com sucesso"}

    except requests.exceptions.RequestException as e:
        return {"erro": True, "mensagem": str(e)}