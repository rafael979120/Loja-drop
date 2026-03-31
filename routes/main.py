from flask import Blueprint, render_template, request
from utils.helpers import PRODUTOS, get_produto_by_id
from models.db import get_db_connection

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', produtos=PRODUTOS)

@main_bp.route('/produto/<int:produto_id>')
def produto(produto_id):
    prod = get_produto_by_id(produto_id)
    if not prod:
        return render_template('erro.html', mensagem="Produto não encontrado."), 404
    return render_template('produto.html', produto=prod)

@main_bp.route('/checkout/<int:produto_id>')
def checkout(produto_id):
    prod = get_produto_by_id(produto_id)
    if not prod:
        return render_template('erro.html', mensagem="Produto não encontrado."), 404
    return render_template('checkout.html', produto=prod)

# Páginas de retorno de pagamento e legais
@main_bp.route('/sucesso')
def sucesso(): return render_template('sucesso.html')

@main_bp.route('/erro')
def erro(): return render_template('erro.html', mensagem="Houve um problema com a sua requisição.")

@main_bp.route('/privacidade')
def privacidade(): return render_template('privacidade.html')

@main_bp.route('/termos')
def termos(): return render_template('termos.html')

@main_bp.route('/contato')
def contato(): return render_template('contato.html')
# --- PAINEL DE CONTROLE SECRETO ---
@main_bp.route('/painel_secreto')
def painel_secreto():
    # Sistema de segurança simples: só entra quem tiver a senha na URL
    senha = request.args.get('senha')
    
    # Você pode trocar 'rafael123' pela senha que você quiser!
    if senha != 'rafael123': 
        return "Acesso Negado. Senha incorreta.", 403

    # Se a senha estiver certa, busca os pedidos no banco de dados
    conn = get_db_connection()
    # Pega todos os pedidos, do mais novo pro mais velho
    pedidos = conn.execute('SELECT * FROM pedidos ORDER BY id DESC').fetchall()
    conn.close()

    return render_template('admin.html', pedidos=pedidos)