import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

def atualizar_preco(nome_produto, novo_preco):
    db = get_database()
    colecao = db['estoque']
    
    # Padroniza o nome
    nome_padrao = nome_produto.strip().lower()
    
    print(f"\nTentando atualizar '{nome_padrao}' para R$ {novo_preco}...")

    filtro = { "produto": nome_padrao }

    # $set atualiza apenas o campo especifico
    novos_valores = { "$set": { "preco_venda": float(novo_preco) } }

    resultado = colecao.update_one(filtro, novos_valores)

    if resultado.matched_count > 0:
        print(f"Sucesso! O preco de '{nome_padrao}' foi atualizado.")
    else:
        print("Erro: Produto nao encontrado.")

if __name__ == "__main__":
    produto = input("Nome do produto: ")
    preco = input("Novo preco: ")
    atualizar_preco(produto, preco)