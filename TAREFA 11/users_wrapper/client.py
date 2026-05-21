import requests

BASE_URL = "http://localhost:8000/users"


def safe_json(response):
    """Evita erro quando a resposta não é JSON"""
    try:
        return response.json()
    except Exception:
        return {
            "erro": "Resposta não é JSON",
            "status": response.status_code,
            "conteudo": response.text
        }


def list_users():
    """Lista todos os usuários"""
    response = requests.get(BASE_URL)
    return safe_json(response)


def read(user_id):
    """Busca um usuário específico pelo ID"""
    response = requests.get(f"{BASE_URL}/{user_id}")
    return safe_json(response)


def create(nome, email, telefone):
    """Cria um novo usuário"""
    data = {
        "name": nome,
        "email": email,
        "phone": telefone
    }

    response = requests.post(BASE_URL, json=data)
    return safe_json(response)


def update(user_id, nome, email, telefone):
    """Atualiza um usuário"""
    data = {
        "name": nome,
        "email": email,
        "phone": telefone
    }

    response = requests.put(f"{BASE_URL}/{user_id}", json=data)
    return safe_json(response)


def delete(user_id):
    """Remove um usuário"""
    response = requests.delete(f"{BASE_URL}/{user_id}")

    if response.status_code in [200, 202, 204]:
        return {"mensagem": "Usuário removido com sucesso"}

    return safe_json(response)