import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

def buscar_por_nome(termo):
    db = get_database()
    colecao = db['estoque']

    print(f" Buscando pelo com base em: {termo}...")

    query = {
        "produto": { "$regex": termo, "$options": "i"}
    }

    resultados = list(colecao.find(query))

    if len(resultados) > 0:
        print(f"Foram encontrados: {len(resultados)} produtos:\n")
        print("-" * 50)
        print(f"{'PRODUTO':<25} | {'PREÇO':<10} | {'ESTOQUE'}")
        print("-" * 50)
        
        for item in resultados:
            nome = item['produto']
            preco = item['preco_venda']
            qtde = item['qtde']

            print(f"{nome:<25} | R$ {preco:<7.2f} | {qtde} un")
        print("-" * 50)
    else:
        print("XXX \n Nenhum produto encontrado com esse nome...")

# MENU
if __name__ == "__main__":
    while True:
        termo_usuario = input("\n Digite o nome do produto (ou '0' para sair)")

        if termo_usuario == '0':
            break 
        buscar_por_nome(termo_usuario)