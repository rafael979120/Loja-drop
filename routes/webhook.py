from flask import Blueprint, request, jsonify
import mercadopago
from config import Config
from models.db import get_db_connection

webhook_bp = Blueprint('webhook', __name__)
sdk = mercadopago.SDK(Config.MP_ACCESS_TOKEN)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    # O Mercado Pago avisa essa rota quando um pagamento é aprovado, recusado, etc.
    payment_id = request.args.get('data.id') or request.args.get('id')
    
    if payment_id:
        payment_info = sdk.payment().get(payment_id)
        payment = payment_info["response"]
        
        if payment.get("status") == "approved":
            pedido_id = payment.get("external_reference")
            if pedido_id:
                # Se aprovado, muda o status no nosso banco para 'pago'
                conn = get_db_connection()
                conn.execute('UPDATE pedidos SET status_pagamento = ? WHERE id = ?', ('pago', pedido_id))
                conn.commit()
                conn.close()
                
    return jsonify({"status": "recebido"}), 200