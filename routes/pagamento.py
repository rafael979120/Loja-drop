from flask import Blueprint, request, redirect, url_for
import mercadopago
from config import Config
from models.db import get_db_connection
from utils.helpers import get_produto_by_id

pagamento_bp = Blueprint('pagamento', __name__)

# Inicializa SDK Mercado Pago
sdk = mercadopago.SDK(Config.MP_ACCESS_TOKEN)

@pagamento_bp.route('/processar_pagamento', methods=['POST'])
def processar_pagamento():
    produto_id = request.form.get('produto_id')
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')
    email = request.form.get('email')
    endereco = request.form.get('endereco')

    produto = get_produto_by_id(produto_id)
    if not produto:
        return redirect(url_for('main.erro'))

    # 1. Salva o pedido no banco como 'pendente'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (produto_id, nome_produto, preco, nome_cliente, cpf, telefone, email, endereco)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (produto['id'], produto['nome'], produto['preco'], nome, cpf, telefone, email, endereco))
    pedido_id = cursor.lastrowid
    conn.commit()

    # 2. Cria a preferência de pagamento no Mercado Pago
    preference_data = {
        "items": [{
            "title": produto['nome'],
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": float(produto['preco'])
        }],
        "payer": {
            "name": nome,
            "email": email,
            "identification": {"type": "CPF", "number": cpf}
        },
        "back_urls": {
            "success": request.host_url + "sucesso",
            "failure": request.host_url + "erro",
            "pending": request.host_url + "sucesso"
        },
        "auto_return": "approved",
        "external_reference": str(pedido_id) # Conecta a venda do MP com o ID do nosso banco
    }

    try:
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        
        # Atualiza o pedido com o ID da preferência gerada
        cursor.execute('UPDATE pedidos SET mp_preference_id = ? WHERE id = ?', (preference['id'], pedido_id))
        conn.commit()
        conn.close()

        # 3. Redireciona o usuário direto para a tela de pagamento do Mercado Pago
        return redirect(preference['init_point'])
        
    except Exception as e:
        print(f"Erro ao criar preferência: {e}")
        return redirect(url_for('main.erro'))