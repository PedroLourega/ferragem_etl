import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_database

CSV_path = 'data/estoque_bruto.csv'

def extrair_dados():
    try:
        df = pd.read_csv(CSV_path, sep=';', encoding='utf-8')
        return df
    except FileNotFoundError:
        # Corrigi apenas o nome da variavel aqui dentro para bater com a declarada (CSV_path)
        print(f"Erro, o arquivo '{CSV_path}' não foi localizado.")
        return None
    

def transformar_dados(df):
    print("Realizando a limpeza dos dados...")

    # Padroniza os nomes das colunas
    df.columns = [col.strip().lower() for col in df.columns]

    # Limpa o texto deixando tudo minusculo, facilitando nas consultas
    cols_texto = ['produto', 'categoria']
    for col in cols_texto:
        df[col] = df[col].astype(str).str.lower().str.strip()


    # Funcao auxiliar para limpar cada cel de preço
    def limpar_preco(valor):
        if isinstance(valor, str):
            # tira o R$, espaços e troca a virgula por "."
            valor = valor.replace('R$', '').replace(' ','').replace(',','.')
            return float(valor)
    
    # Aplica uma limpeza na coluna de preços
    df['preco_venda'] = df['preco_venda'].apply(limpar_preco)

    # Calculos extra de teste
    df['valor_total_estoque'] = df['preco_venda'] * df['qtde']

    dados_prontos = df.to_dict('records')

    print(f"{len(dados_prontos)} produtos processados e limpos")
    return dados_prontos
        

# Load
def carregar_dados(dados):
    print("Salvando dados no MongoDB")

    try:
        # Conexao ao db
        db = get_database()

        # Seleciona collection
        colecao = db['estoque']

        result = colecao.insert_many(dados)

        print(f'Sucesso!! {len(result.inserted_ids)} documentos inseridos no banco.')
    except Exception as e:
        print(f"XXX \n Erro ao salvar no banco: {e}")


if __name__ == "__main__":
    df = extrair_dados()
    
    if df is not None:
        dados_tratados = transformar_dados(df)
        carregar_dados(dados_tratados)