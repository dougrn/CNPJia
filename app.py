# Arquivo: app.py
# Versão demonstrativa para Portfólio
# A lógica de segurança e tokens foi removida para esta demonstração pública.

from fastapi import FastAPI, HTTPException, Query
from contextlib import asynccontextmanager
import os
import sys

# Importação da engine (simulada neste repositório público)
from core_engine import AgenteBuscaInteligente, DatabaseConnector

# Variáveis Globais
sistema_busca = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação:
    1. Inicializa o Pool de Conexões com o PostgreSQL.
    2. Carrega os modelos de ML e Caches em memória RAM (L1).
    """
    global sistema_busca
    print("--- INICIALIZANDO SISTEMA (DEMO MODE) ---")
    
    # Simulação de inicialização de drivers
    db_conn = DatabaseConnector()
    sistema_busca = AgenteBuscaInteligente(db_conn)
    
    yield
    
    print("--- DESLIGANDO SISTEMA ---")
    # db_conn.close_pool()

app = FastAPI(
    title="Smart CNPJ Search API",
    description="Interface de busca em linguagem natural para Big Data.",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/search")
async def search_companies(q: str = Query(..., description="Digite sua busca em linguagem natural e.x: 'Padaria no centro'")):
    """
    Endpoint principal que processa a linguagem natural e retorna empresas.
    """
    if not sistema_busca:
        raise HTTPException(status_code=503, detail="Sistema inicializando...")
    
    # Chama a camada de inteligência
    try:
        resultado = sistema_busca.processar_intencao(q)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/company/{cnpj}")
async def get_company_details(cnpj: str):
    """
    Busca enriquecida de dados cadastrais por chave primária.
    """
    return sistema_busca.buscar_detalhes(cnpj)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)