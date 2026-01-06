import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega as var do .env
load_dotenv()

def get_database():
    """
    Func que conecta ao MongoDB e retorna o objeto.
    """
    connection_string = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")
    
    if not connection_string:
        raise ValueError("Erro: A variável MONGO_URI não foi encontrada no arquivo .env")

    # Cria a conexão c o cloud
    client = MongoClient(connection_string)
    
    # Retorna o banco de dados 
    return client[db_name]