# Automação Fiscal e Financeira

Projeto de estudo e desenvolvimento de uma automação para conferência de dados fiscais e financeiros, utilizando Python, n8n e inteligência artificial.

## Objetivo

Desenvolver um fluxo automatizado capaz de coletar dados fictícios de notas fiscais e pagamentos, organizar as informações, identificar possíveis divergências e gerar alertas para conferência humana.

O projeto busca demonstrar como ferramentas de automação podem auxiliar na redução de tarefas manuais e na organização de processos fiscais e financeiros.

## Funcionalidades planejadas

- Extração de dados de uma página HTML utilizando Python e BeautifulSoup.
- Envio dos dados para um workflow do n8n por meio de um Webhook.
- Consulta a um arquivo CSV com informações complementares.
- Cruzamento de dados de notas fiscais e pagamentos.
- Identificação de pagamentos pendentes e divergências de valores.
- Utilização de inteligência artificial para gerar explicações sobre as ocorrências.
- Geração de mensagens e respostas automatizadas.

## Tecnologias

- **Python:** coleta e extração de dados.
- **BeautifulSoup:** leitura de informações em páginas HTML.
- **n8n:** integração e automação do fluxo de trabalho.
- **JavaScript:** tratamento e organização de dados nos nós Code.
- **OpenAI:** apoio na geração de explicações em linguagem natural.
- **GitHub:** versionamento do código e documentação do projeto.
- **Google Colab:** execução e testes do notebook Python.

## Fluxo de funcionamento planejado

1. Coletar registros fiscais fictícios de uma página HTML.
2. Enviar os registros ao n8n por meio de um Webhook.
3. Consultar dados complementares em um arquivo CSV.
4. Combinar e organizar as informações.
5. Comparar os valores registrados e identificar possíveis divergências.
6. Gerar uma explicação e encaminhar um alerta para conferência.
7. Retornar o resultado da execução.

## Estrutura planejada

```text
automacao-fiscal-financeira/
├── README.md
├── .gitignore
├── docs/
│   └── index.html
├── data/
│   └── notas_pagamentos.csv
├── src/
│   └── extrair_dados.ipynb
└── n8n/
    └── workflow.json
```

A estrutura será criada e atualizada conforme o desenvolvimento avançar.

## Status do projeto

Em desenvolvimento.

As funcionalidades serão implementadas e testadas por etapas. A documentação será atualizada conforme cada parte do fluxo for concluída.

## Dados e limitações

O projeto utilizará dados fictícios para fins educacionais. Os alertas gerados servem como apoio à conferência e não substituem a validação dos documentos, dos registros contábeis ou das obrigações fiscais por um profissional responsável.

## Referência educacional

Projeto autoral inspirado em conceitos e práticas de automação estudados em desafios educacionais da DIO, com proposta e aplicação adaptadas para o contexto fiscal e financeiro.
