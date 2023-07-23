# APRENDENDO A UTILIZAR O PACOTE brasil-data
from brdata import xpi
from brdata import fundamentus

# XPI
# Coletando dados ad análise da XPI para uma determinada ação:

# acao = xpi.analise('PLPL3')
# print(acao)

# Fundamentus
# Coletando tabela do resultado da busca no Fundamentus
# (equivalente a página https://www.fundamentus.com.br/resultado.php)

# dados = fundamentus.resultados()
# print(dados)

balanco, demonstrativo = fundamentus.balanco_historico("mglu3")

print(demonstrativo)
