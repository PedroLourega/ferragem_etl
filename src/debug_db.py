import sys
import os
import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

def espiar_banco():
    db = get_database()
    colecao = db['estoque']
    
    # Cont
    total = colecao.count_documents({})
    print(f"\n Total de documentos no banco: {total}")
    
    if total > 0:
        
        item = colecao.find_one()
        
        print("\n ESTRUTURA DO PRIMEIRO ITEM SALVO:")
        print("-" * 40)
        
        pprint.pprint(item) 
        print("-" * 40)
        
    else:
        print("O banco está realmente vazio.")

if __name__ == "__main__":
    espiar_banco()