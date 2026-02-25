# Gerenciamento de Operações em um Aeroporto

## Objetivo

Aplicar distribuições estatísticas para modelar operações aeroportuárias.

Distribuições utilizadas:

- Normal – Tempos de check-in
- Poisson – Emergências
- Binomial – Detecção de ameaças
- Bernoulli – Direcionamento de bagagens
- Multinomial – Alocação de portões
- Geométrica – Tempo até falha

## Como executar

1. Instalar dependências
   pip install -r requirements.txt

2. Executar análise
   python src/analise_aeroporto.py

3. Abrir o notebook
   notebooks/analise_aeroporto.ipynb

## Aplicação no negócio

- Dimensionamento de equipes de check-in
- Planejamento de recursos de emergência
- Avaliação da eficiência da segurança
- Monitoramento do sistema de bagagens
- Otimização da utilização de portõe
