import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

def adicionar_novo_produto():
    db = get_database()
    colecao = db['estoque']

    print("\n CADASTRO DE NOVO PRODUTO")
    print("-" * 30)
    
    # Coleta os dados do produto
    nome = input("Nome do Produto: ").strip()
    categoria = input("Categoria: ").strip().lower()
    
    # Validação do Preço
    while True:
        try:
            preco_input = input("Preço (ex: 12.50): ")
            # Troca , por . para não dar erro
            preco = float(preco_input.replace(',', '.')) 
            break
        except ValueError:
            print(" Erro: Digite um valor numérico válido (use ponto ou vírgula).")

    # Validacao da Qtde
    while True:
        try:
            qtde_input = input("Quantidade em estoque: ")
            qtde = int(qtde_input)
            break
        except ValueError:
            print(" Erro: A quantidade deve ser um número inteiro (sem vírgula).")

    # monta o Dict
    novo_produto = {
        "produto": nome.lower(), 
        "categoria": categoria,
        "preco_venda": preco,
        "qtde": qtde,
        "valor_total_estoque": preco * qtde
    }

    # envia para o db
    colecao.insert_one(novo_produto)
    
    print(f"\n Sucesso! '{nome}' foi adicionado ao estoque.")

if __name__ == "__main__":
    adicionar_novo_produto()