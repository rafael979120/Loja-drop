
import os

class Config:
    # Chave de segurança do Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_super_segura_aqui'
    
    # Caminho absoluto para o banco de dados
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(BASE_DIR, 'database.db')
    
    # ⚠️ IMPORTANTE: CREDENCIAIS DO MERCADO PAGO ⚠️
    # Pegue essas chaves no painel de desenvolvedor do Mercado Pago (Suas integrações)
    MP_ACCESS_TOKEN = "APP_USR-6584368994453792-032522-86a29190c868cab7d5cb22e810dd52a9-762251450"
    MP_PUBLIC_KEY = "APP_USR-b954e92b-3021-4e53-9d6f-dec5ac70b276"