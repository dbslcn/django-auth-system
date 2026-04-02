"""
curl -X POST 'https://url_supabase.supabase.co/rest/v1/profiles' \
-H "apikey: SUPABASE_CLIENT_ANON_KEY" \
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" \
-H "Content-Type: application/json" \
-H "Prefer: return=minimal" \
-d '{ "some_column": "someValue", "other_column": "otherValue" }'
"""
import httpx
import os
import logging
from dotenv import load_dotenv


logger = logging.getLogger(__name__)
# Carrega o .env antes de qualquer coisa
load_dotenv()

class SupabaseClient:
    def __init__(self):
        # Captura as variáveis
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")

        # Validação Crítica: Se as chaves não existirem, o programa para com aviso claro
        if not self.url or not self.key:
            logger.error("ERRO: SUPABASE_URL ou SUPABASE_KEY não encontradas no arquivo .env")

        self.headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        }

    def insert(self, table, data):
        """
        Insere dados na tabela especificada.
        'data' deve ser um dicionário Python.
        """
        endpoint = f"{self.url}/rest/v1/{table}"
        
        # Usando o bloco 'with' para gerenciar a conexão de forma eficiente
        with httpx.Client() as client:
            response = client.post(endpoint, headers=self.headers, json=data)
            
            # Levanta erro se o status for 4xx ou 5xx
            response.raise_for_status()
            
            # Como usamos 'return=minimal', o 201 não traz corpo.
            return logger.info(f"Sucesso! Status: {response.status_code}")

if __name__ == "__main__":
    try:
        client = SupabaseClient()
        
        # Exemplo de teste para a sua tabela login_history
        # Lembre-se: se a tabela tiver restrições (como user_id), o dado deve ser válido.
        teste_payload = {
            "username": "joao",
            "password_hash":"password"
            # Se a coluna user_id for obrigatória, adicione um UUID válido aqui
        }
        
        print(client.insert("profiles", teste_payload))
        
    except Exception as e:
        print(f"Erro na operação: {e}")