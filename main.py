import sys
import os
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# rotas
from src.adicionar_produto import adicionar_novo_produto
from src.buscar_produto import buscar_por_nome
from src.atualizar_produto import atualizar_preco
from src.deletar_produto import deletar_produto
from src.listar_produtos import listar_todo_estoque

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu
def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE FERRAGEM")
    print("="*40)
    print("1. Adicionar Produto (Manual)")
    print("2. Buscar Produto")
    print("3. Atualizar Preco")
    print("4. Deletar Produto")
    print("5. Recarregar Dados do CSV (ETL)")
    print("6. Ver Catalogo Completo")
    print("0. Sair")
    print("-" * 40)

def iniciar_sistema():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            adicionar_novo_produto()
            
        elif opcao == '2':
            termo = input("\nDigite o nome para buscar: ")
            buscar_por_nome(termo)
            
        elif opcao == '3':
            nome = input("\nNome do produto a atualizar: ")
            novo_preco = input("Novo preco: ")
            atualizar_preco(nome, novo_preco)
            
        elif opcao == '4':
            nome = input("\nNome do produto para EXCLUIR: ")
            deletar_produto(nome)
            
        elif opcao == '5':
            print("\nRodando processamento de carga (ETL)...")
            os.system("python src/etl_process.py")

        elif opcao == '6':
            listar_todo_estoque()
            
        elif opcao == '0':
            print("\nFechando o sistema. Ate mais!")
            break
            
        else:
            print("\nOpcao invalida!")
        
        input("\n[Pressione ENTER para voltar ao menu...]")
        limpar_tela()

if __name__ == "__main__":
    limpar_tela()
    iniciar_sistema()