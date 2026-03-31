from flask import Flask
from config import Config
from models.db import init_db
from routes.main import main_bp
from routes.pagamento import pagamento_bp
from routes.webhook import webhook_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o banco de dados SQLite (Cria a tabela pedidos se não existir)
    init_db()

    # Registra as rotas (Blueprints)
    app.register_blueprint(main_bp)
    app.register_blueprint(pagamento_bp)
    app.register_blueprint(webhook_bp)

    return app

app = create_app()

if __name__ == '__main__':
    # Roda o servidor. '0.0.0.0' permite que o Render e outras plataformas exponham a porta.
    app.run(debug=True, host='0.0.0.0', port=5000)