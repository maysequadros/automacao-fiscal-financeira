# Módulo de Conciliação de Pagamentos

## Objetivo

Comparar os valores das notas fiscais com os valores pagos, identificando pagamentos integrais, parciais, ausentes e excedentes.

## Entrada de dados

## Entrada de dados

O arquivo `data/notas_pagamentos.csv` contém os seguintes campos:

- `nota`: identificador da nota fiscal.
- `fornecedor`: nome do fornecedor.
- `valor_nota`: valor total da nota fiscal.
- `valor_pago`: valor pago.
- `email_pagador`: endereço de e-mail do responsável pelo pagamento, utilizado no envio de alertas.

Os dados utilizados neste projeto são fictícios e destinados a testes.

## Regras de classificação

| Situação | Regra |
|---|---|
| Pago integralmente | Valor pago igual ao valor da nota |
| Sem pagamento | Valor pago igual a zero |
| Pagamento parcial | Valor pago menor que o valor da nota e maior que zero |
| Pagamento excedente | Valor pago maior que o valor da nota |

## Resultados calculados

- `status`: classificação do pagamento.
- `saldo_pendente`: valor que ainda falta pagar, limitado a zero quando não há saldo.
- `excedente`: valor pago além do valor da nota, limitado a zero quando não há excedente.

## Teste realizado

O script `src/conciliar_pagamentos.py` foi executado no PyCharm com quatro registros de teste.

| Nota | Status esperado | Saldo pendente | Excedente |
|---|---|---:|---:|
| NF001 | PAGO_INTEGRALMENTE | R$ 0,00 | R$ 0,00 |
| NF002 | PAGAMENTO_PARCIAL | R$ 600,00 | R$ 0,00 |
| NF003 | SEM_PAGAMENTO | R$ 800,00 | R$ 0,00 |
| NF004 | PAGAMENTO_EXCEDENTE | R$ 0,00 | R$ 150,00 |

**Resultado:** teste executado com sucesso, sem erros.

## Próximas melhorias

- Preparar o alerta por e-mail para pagamentos excedentes.
- Integrar a conciliação ao fluxo de automação no n8n.
- Documentar e testar o fluxo completo.
