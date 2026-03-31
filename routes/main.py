from flask import Blueprint, render_template
from utils.helpers import PRODUTOS, get_produto_by_id

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