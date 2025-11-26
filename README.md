# **Smart CNPJ Search Engine (NLP \+ Vector DB) 🔍**

Um motor de busca de alta performance projetado para consultar bases de dados corporativas massivas (+50 milhões de registros) utilizando Linguagem Natural e Inteligência Artificial Híbrida.

## **🚀 O Desafio**

Consultar bases de dados legadas usando SQL tradicional (LIKE) é ineficiente para buscas imprecisas e falha quando o usuário não conhece a taxonomia exata (ex: códigos CNAE ou razão social correta).

**Cenário:** O usuário busca "Padaria no centro", mas o banco só entende CNAE=4721-1/02 e BAIRRO='CENTRO'.

## **💡 A Solução**

Desenvolvi uma arquitetura proprietária que atua como um *middleware* inteligente entre a intenção do usuário e o banco de dados PostgreSQL.

O sistema **não usa a IA para buscar no banco** (o que seria lento e caro). Em vez disso, utiliza LLMs (Large Language Models) apenas para **extração de entidades** e estruturação de query, delegando a busca pesada para uma combinação de **índices vetoriais (Embeddings)** e **busca textual otimizada**.

## **⚙️ Arquitetura Lógica**

### **O Fluxo "Waterfall":**

1. **NLP Parsing:** O sistema intercepta a pergunta natural.  
2. **Entity Resolution (IA):** Um agente extrai estruturadamente:  
   * Atividade: "Padaria" \-\> Convertido para vetor.  
   * Local: "Centro" \-\> Normalizado.  
3. **Cache L1:** Verificação de hashes em memória RAM (Latência \< 5ms).  
4. **Busca Híbrida:**  
   * *Fase 1:* Busca Vetorial (Embeddings) para identificar CNAEs compatíveis.  
   * *Fase 2:* Filtragem SQL otimizada (Estratégia "No-Join" para tabelas de bilhões de linhas).

## **🛠️ Stack Tecnológica**

* **Core:** Python 3.12  
* **API Gateway:** FastAPI (Assíncrono)  
* **Database:** PostgreSQL 16  
* **Extensions:** pgvector (Busca Semântica) \+ pg\_trgm (Fuzzy Matching)  
* **AI/NLP:** Google Gemini 1.5 Flash (Entity Resolution)  
* **Infraestrutura:** Docker & Connection Pooling (psycopg2)

## **⚠️ Nota sobre o Código**

Este repositório contém o **boilerplate arquitetural** do projeto para fins de demonstração de portfólio.

**Nota:** A lógica de orquestração ("core engine"), as chaves de API e as estratégias de indexação proprietárias foram ocultadas ou substituídas por stubs (classes simuladas) para proteção de propriedade intelectual.

## **📦 Como rodar (Demo)**

\# Clone o repositório  
git clone \[https://github.com/dougrn/cnpjia.git\](https://github.com/dougrn/cnpjia.git)

\# Instale as dependências  
pip install \-r requirements.txt

\# Inicie o servidor  
uvicorn app:app \--reload

Desenvolvido por Douglas  

Especialista em Engenharia de Dados e Sistemas Inteligentes.
