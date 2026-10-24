
# Automação Fiscal e Financeira

Projeto de automação desenvolvido com Python, n8n e inteligência artificial para apoiar a conciliação de notas fiscais e pagamentos, identificar divergências e gerar alertas por e-mail.

## Objetivo

Demonstrar como ferramentas de programação e automação podem reduzir tarefas manuais de conferência financeira, facilitando a identificação de pagamentos integrais, parciais, não realizados e excedentes.


## 🔄 Como funciona o workflow

1. **Recebimento:** o workflow é iniciado por um Webhook do n8n.
2. **Leitura dos dados:** os dados das notas fiscais e dos pagamentos são obtidos para análise.
3. **Conciliação:** os registros são organizados para identificar pagamentos integrais, parciais, ausentes ou excedentes.
4. **Análise com IA:** o modelo local Ollama auxilia na análise das informações.
5. **Verificação:** o workflow identifica pagamentos excedentes.
6. **Notificação:** quando necessário, o Gmail envia um alerta ao responsável pelo pagamento.
7. **Resposta:** o Webhook retorna uma confirmação do processamento.

**Observação:** o projeto utiliza dados fictícios e tem finalidade demonstrativa. As credenciais do Gmail e do Ollama devem ser configuradas individualmente no n8n.

# Automação Fiscal e Financeira

Projeto de automação desenvolvido com Python, n8n e inteligência artificial para apoiar a conciliação de notas fiscais e pagamentos, identificar divergências e gerar alertas por e-mail.

## Objetivo

Demonstrar como ferramentas de programação e automação podem reduzir tarefas manuais de conferência financeira, facilitando a identificação de pagamentos integrais, parciais, não realizados e excedentes.

## Funcionalidades

- Leitura de dados de notas fiscais e pagamentos em arquivo CSV.
- Conciliação de valores com Python e pandas.
- Classificação dos pagamentos conforme os valores da nota e do pagamento.
- Identificação de saldos pendentes e pagamentos excedentes.
- Integração de um workflow no n8n com webhook e requisição HTTP.
- Uso de IA para gerar uma análise textual dos dados.
- Envio de alerta por e-mail para pagamentos excedentes.
- Retorno de uma resposta ao sistema que aciona o webhook.

## Tecnologias utilizadas

- Python
- pandas
- n8n
- Ollama com modelo local de IA
- Gmail API
- GitHub

## Estrutura do projeto

```text
automacao-fiscal-financeira/
├── data/
│   └── notas_pagamentos.csv
├── docs/
│   └── conciliacao.md
├── n8n/
│   └── workflow.json
├── src/
│   └── conciliar_pagamentos.py
├── .gitignore
└── README.md
```


## Exemplo de conciliação

| Nota fiscal | Valor da nota | Valor pago | Resultado |
|---|---:|---:|---|
| NF001 | R$ 1.000,00 | R$ 1.000,00 | Pago integralmente |
| NF002 | R$ 1.500,00 | R$ 900,00 | Pagamento parcial |
| NF003 | R$ 800,00 | R$ 0,00 | Sem pagamento |
| NF004 | R$ 500,00 | R$ 650,00 | Pagamento excedente de R$ 150,00 |

Os dados apresentados são fictícios e utilizados apenas para demonstração.

## Como executar o script Python

**Pré-requisitos:** Python instalado e acesso ao terminal.

1. Clone o repositório e abra a pasta do projeto.
2. Instale a dependência:

   `pip install pandas`

3. Execute o script a partir da pasta raiz:

   `python src/conciliar_pagamentos.py`

O script lê o arquivo CSV de entrada, classifica os pagamentos e calcula os saldos pendentes e os valores excedentes.

## Workflow no n8n

O workflow recebe uma requisição pelo webhook, busca os dados do CSV, processa as informações, utiliza IA para produzir uma análise e verifica se há pagamento excedente. Quando o excedente é identificado, o fluxo encaminha um alerta por e-mail.

Para executar o workflow, é necessário configurar o n8n, o acesso ao modelo local do Ollama e as credenciais autorizadas do Gmail.

## Aprendizados

Este projeto reúne conhecimentos de análise de dados com Python, tratamento de arquivos CSV, lógica condicional, integração entre ferramentas, uso de modelos locais de IA, APIs e automação de notificações.

## Segurança

- Não utilize dados financeiros reais ou informações pessoais no repositório público.
- Não publique senhas, tokens, credenciais OAuth ou chaves de API.
- Configure as credenciais diretamente no ambiente do n8n.

## Autora

Projeto autoral desenvolvido para estudo e portfólio na área de automação fiscal e financeira.

