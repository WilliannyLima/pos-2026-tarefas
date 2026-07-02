from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

oauth = OAuth(app)


oauth.register(
    name='suap',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url='https://suap.ifrn.edu.br/api/',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/', 
    fetch_token=lambda: session.get('suap_token')          
)


def get_usuario():
    resposta = oauth.suap.get('rh/meus-dados')
    return resposta.json()

def get_boletim(ano, periodo):
    url = f"ensino/meu-boletim/{ano}/{periodo}/"
    resposta = oauth.suap.get(url)
    if resposta.status_code == 200:
        return resposta.json().get("results", [])
    return []


@app.route('/')
def index():
    if 'suap_token' in session:
        return redirect(url_for('perfil'))
    return render_template('index.html')


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)

@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('perfil'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/perfil')
def perfil():
    if 'suap_token' not in session:
        return redirect(url_for('index'))

    usuario = get_usuario()
    return render_template('user.html', user_data=usuario)

@app.route('/boletim')
def boletim():
    if 'suap_token' not in session:
        return redirect(url_for('index'))

    usuario = get_usuario()
    ano = request.args.get("ano", "2026")
    periodo = request.args.get("periodo", "1")
    dados_boletim = get_boletim(ano, periodo)

    return render_template(
        "boletim.html",
        user_data=usuario,
        boletim=dados_boletim,
        ano_selecionado=int(ano),       
        periodo_selecionado=int(periodo) 
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)