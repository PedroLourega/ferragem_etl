import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.database import get_database

if __name__ == "__main__":
    db = get_database()
    
    result = db['estoque'].delete_many({})
    print(f"  Limpeza concluída!! \n N: {result.deleted_count} itens removidos. O banco está vazio.")