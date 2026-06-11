# Marketing Performance Analytics

## Visão Geral

O Marketing Performance Analytics é um projeto desenvolvido para simular uma operação real de análise de campanhas digitais.

O objetivo é transformar dados de marketing em informações estratégicas para apoiar decisões de investimento em mídia paga.

A aplicação permite analisar campanhas por plataforma, tipo de campanha, indústria e país, utilizando Python, Pandas, Streamlit e Plotly.

---

## Objetivo de Negócio

Empresas investem milhões em campanhas digitais e precisam responder perguntas como:

* Qual plataforma gera melhor retorno?
* Qual tipo de campanha é mais eficiente?
* Qual segmento de mercado apresenta melhor desempenho?
* Em quais países o investimento apresenta maior retorno?
* Onde aumentar ou reduzir orçamento?

Este projeto busca responder essas perguntas por meio de análise de dados e visualização interativa.

---

## Dataset

Base utilizada:

Global Ads Performance Dataset

Contém informações simuladas de campanhas executadas em diferentes plataformas digitais.

### Dimensões

* Plataforma

  * Google Ads
  * Meta Ads
  * TikTok Ads

* Tipo de Campanha

  * Search
  * Shopping
  * Video
  * Display

* Indústria

  * E-commerce
  * EdTech
  * Fintech
  * Healthcare
  * SaaS

* País

  * Australia
  * Canada
  * Germany
  * India
  * UAE
  * UK
  * USA

---

## Principais Métricas

### Impressões

Quantidade de vezes que um anúncio foi exibido.

### Cliques

Quantidade de cliques recebidos.

### CTR

Click Through Rate.

Representa a taxa de clique.

Fórmula:

CTR = Cliques / Impressões

### CPC

Cost Per Click.

Representa o custo médio por clique.

Fórmula:

CPC = Investimento / Cliques

### Conversões

Quantidade de ações desejadas realizadas pelo usuário.

Exemplos:

* Compra
* Cadastro
* Lead
* Solicitação de orçamento

### CPA

Cost Per Acquisition.

Representa quanto custa gerar uma conversão.

Fórmula:

CPA = Investimento / Conversões

### Receita

Valor financeiro gerado pelas campanhas.

### ROAS

Return On Ad Spend.

Representa o retorno gerado para cada real investido.

Fórmula:

ROAS = Receita / Investimento

---

## Arquitetura do Projeto

```text
pipeline-campanhas-marketing/

├── dados
│   ├── bruto
│   └── tratado
│
├── docs
│
├── scripts
│   ├── 01_entender_base.py
│   ├── 02_converter_csv_para_xlsx.py
│   ├── 03_explorar_categorias.py
│   ├── 04_explorar_metricas.py
│   ├── 05_analise_plataformas.py
│   └── 06_analise_tipo_campanha.py
│
├── dashboards
│
├── automacoes
│
├── database
│
├── app.py
│
└── requirements.txt
```

---

## Pipeline de Dados

O pipeline segue as etapas abaixo:

### 1. Ingestão

Leitura do arquivo CSV original.

### 2. Exploração

Validação da estrutura da base:

* Colunas
* Tipos de dados
* Valores nulos
* Duplicidades

### 3. Análise

Cálculo de métricas e indicadores de marketing.

### 4. Visualização

Exibição dos resultados em dashboards interativos utilizando Streamlit.

### 5. Storytelling

Tradução dos dados em linguagem de negócio para facilitar a tomada de decisão.

---

## Funcionalidades

### Visão Executiva

Apresenta:

* Investimento Total
* Receita Total
* Conversões
* ROAS Global
* CTR Global
* CPA Global

### Análise por Plataforma

Comparação entre:

* Google Ads
* Meta Ads
* TikTok Ads

### Análise por Tipo de Campanha

Comparação entre:

* Search
* Shopping
* Video
* Display

### Análise por Indústria

Comparação entre segmentos de mercado.

### Análise por País

Comparação de desempenho entre diferentes regiões.

### Storytelling Executivo

Transforma indicadores técnicos em recomendações estratégicas.

### Dicionário de Métricas

Explica os principais conceitos utilizados no projeto.

---

## Tecnologias Utilizadas

* Python
* Pandas
* Streamlit
* Plotly
* Git
* GitHub

---

## Próximas Evoluções

### Banco de Dados

* SQLite
* PostgreSQL

### SQL

* Consultas analíticas
* Views
* Agregações

### APIs

Integração com fontes externas de marketing.

Exemplos:

* Google Ads API
* Meta Marketing API

### Automações

* Atualização automática de dados
* Agendamento de execução
* Alertas de performance

### Inteligência Artificial

Geração automática de insights e recomendações executivas.

---

## Autor

Lucas Vieira

Analista de Sistemas | Dados | Automação | Business Intelligence

Projeto desenvolvido para estudo de análise de campanhas digitais, visualização de dados e construção de pipelines analíticos.
