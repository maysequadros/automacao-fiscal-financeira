
import pandas as pd
from pathlib import Path

# Localiza a pasta principal do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho do arquivo CSV
arquivo = BASE_DIR / "data" / "notas_pagamentos.csv"

# Lê os dados
dados = pd.read_csv(arquivo)

# Exibe os registros no terminal
print(dados)
