import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

def deletar_produto(termo):
    db = get_database()
    colecao = db['estoque']
    
    # Busca primeiro para garantir o que esta sendo deletado
    query = { "produto": { "$regex": termo, "$options": "i" } }
    produto = colecao.find_one(query)

    if produto:
        print(f"\nATENCAO: Voce vai deletar o produto abaixo:")
        print(f"   Nome: {produto['produto']}")
        print(f"   Preco: R$ {produto['preco_venda']}")
        
        # Trava de seguranca
        confirmacao = input("\nTem certeza? Digite 'SIM' para apagar: ")
        
        if confirmacao == 'SIM':
            colecao.delete_one({"_id": produto["_id"]})
            print("Produto deletado com sucesso do banco.")
        else:
            print("Operacao cancelada.")
            
    else:
        print("Produto nao encontrado.")

if __name__ == "__main__":
    nome = input("\nNome do produto para DELETAR: ")
    deletar_produto(nome)