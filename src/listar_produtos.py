import sys
import os
import pymongo 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

def listar_todo_estoque():
    print("\nConectando ao banco para buscar catalogo...")
    
    try:
        db = get_database()
        colecao = db['estoque']
        
        # O list() força o download dos dados agora
        todos_produtos = list(colecao.find())

        if len(todos_produtos) > 0:
            print("\n" + "="*60)
            print(f"{'PRODUTO':<30} | {'PRECO':<10} | {'QTDE':<5} | {'CATEGORIA'}")
            print("="*60)

            for item in todos_produtos:
                nome = item.get('produto', '---')
                preco = item.get('preco_venda', 0.0)
                qtde = item.get('qtde', 0)
                categoria = item.get('categoria', '---')
                
                # garante que nao quebre se o preco for null
                if preco is None: preco = 0.0

                print(f"{nome:<30} | R$ {preco:<7.2f} | {qtde:<5} | {categoria}")
                
            print("-" * 60)
            print(f"Total de itens cadastrados: {len(todos_produtos)}")
        else:
            print("\nO estoque esta vazio.")
            
    except pymongo.errors.ServerSelectionTimeoutError:
        print("\n Erro: Tempo limite excedido!")
        print("Nao foi possivel conectar ao MongoDB. Verifique sua internet.")
    except Exception as e:
        print(f"\n Ocorreu um erro ao listar: {e}")

if __name__ == "__main__":
    listar_todo_estoque()