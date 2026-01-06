# Sistema de Gestão de Estoque e ETL (Ferragem)

Sistema desenvolvido em Python para automação de processos de dados (ETL) e gerenciamento de estoque via banco de dados NoSQL na nuvem.

O projeto resolve o problema de migração de planilhas locais para um sistema centralizado, tratando inconsistências de formatação (como moedas e separadores) e oferecendo uma interface de linha de comando para manipulação dos dados.

## Tecnologias Usadas

* **Python 3:** Linguagem principal.
* **Pandas:** Biblioteca para extração e tratamento de dados do CSV.
* **MongoDB Atlas:** Banco de dados NoSQL em nuvem.
* **PyMongo:** Driver de conexão com o banco de dados.
* **Python-dotenv:** Gerenciamento de variáveis de ambiente e segurança.

## Estrutura e Funcionalidades

O projeto foi modularizado para separar a lógica de conexão, as regras de ETL e as operações de usuário.

### 1. Processamento de Dados (ETL)
Arquivo: `src/etl_process.py`
* **Extração:** Lê arquivos `.csv` brutos.
* **Transformação:**
    * Corrige problemas de encoding.
    * Trata separadores de CSV (ponto e vírgula vs vírgula).
    * Converte strings de moeda (R$) para float.
    * Padroniza textos para minúsculo (facilita buscas).
    * Calcula o valor total do estoque por item.
* **Carga:** Realiza inserção em lote (Bulk Insert) no MongoDB.

### 2. Banco de Dados
Arquivo: `src/database.py`
* Gerencia a conexão segura com o MongoDB Atlas.
* Utiliza variáveis de ambiente para não expor credenciais no código.

### 3. Interface de Usuário (CRUD)
Arquivo: `main.py`
Menu interativo que integra os scripts de manipulação:
* **Adicionar (`adicionar_produto.py`):** Insere novos itens com validação de tipo (float/int).
* **Buscar (`buscar_produto.py`):** Realiza consultas utilizando Regex para buscas parciais e case-insensitive.
* **Atualizar (`atualizar_produto.py`):** Altera preços utilizando operadores atômicos (`$set`).
* **Deletar (`deletar_produto.py`):** Remove itens com confirmação de segurança prévia.
* **Listar (`listar_produtos.py`):** Exibe o catálogo completo em formato tabular.

## Autor <br>

**Pedro Henrique Lourega Rodrigues** <br>
Estudante de Análise e Desenvolvimento de Sistemas <br>
GitHub: [@PedroLourega](https://github.com/PedroLourega) <br>
