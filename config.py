import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'loja_tech_segura_123'
    
    # O código vai buscar magicamente as chaves que você acabou de colocar no Render
    MP_ACCESS_TOKEN = os.environ.get('MP_ACCESS_TOKEN')
    MP_PUBLIC_KEY = os.environ.get('MP_PUBLIC_KEY')
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(BASE_DIR, 'database.db')