# Lista de produtos (Para evitar criar painel de admin agora, mantemos em memória)
# Lembre-se de colocar as imagens na pasta static/img/produtos/ (ex: 1.jpg, 2.jpg)
PRODUTOS = [
    {"id": 1, "nome": "Carregador Turbo 200W", "preco": 99.90, "imagem": "1.jpg"},
    {"id": 2, "nome": "Luz da Galáxia", "preco": 119.90, "imagem": "2.jpg"},
    {"id": 3, "nome": "Caixa de Som", "preco": 119.90, "imagem": "3.jpg"},
    {"id": 4, "nome": "Aspirador de Pó", "preco": 99.90, "imagem": "4.jpg"},
    {"id": 5, "nome": "Power Bank", "preco": 119.90, "imagem": "5.jpg"},
    {"id": 6, "nome": "Fone Bluetooth", "preco": 99.90, "imagem": "6.jpg"},
    {"id": 7, "nome": "Projetor Android", "preco": 299.90, "imagem": "7.jpg"},
    {"id": 8, "nome": "Massageador", "preco": 99.90, "imagem": "8.jpg"},
    {"id": 9, "nome": "Cabo USB-C 2m", "preco": 69.90, "imagem": "9.jpg"},
    {"id": 10, "nome": "Luminária Smart", "preco": 99.90, "imagem": "10.jpg"},
    {"id": 11, "nome": "Óculos Polarizado", "preco": 119.90, "imagem": "11.jpg"},
    {"id": 12, "nome": "Lâmpada Smart", "preco": 89.90, "imagem": "12.jpg"},
]

def get_produto_by_id(produto_id):
    # Busca um produto específico pelo ID
    for p in PRODUTOS:
        if p["id"] == int(produto_id):
            return p
    return None