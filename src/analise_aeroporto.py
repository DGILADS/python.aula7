"""
Gerenciamento de Operações em um Aeroporto
Versão corrigida:
- Não trava na execução
- Gera gráficos para TODAS as distribuições
- Mostra um dashboard único
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Criar uma figura com vários gráficos (dashboard)
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
fig.suptitle("Dashboard - Operações do Aeroporto", fontsize=16)

# =====================================================
# 1. NORMAL – CHECK-IN
# =====================================================

media = 15
desvio = 5
checkin = np.random.normal(media, desvio, 1000)

axs[0, 0].hist(checkin, bins=30)
axs[0, 0].set_title("Normal - Tempos de Check-in")

media_calc = np.mean(checkin)
desvio_calc = np.std(checkin)
prob_extremo = 1 - stats.norm.cdf(25, media_calc, desvio_calc)

print("=== Check-in ===")
print("Média:", media_calc)
print("Desvio:", desvio_calc)
print("Probabilidade > 25 min:", prob_extremo)


# =====================================================
# 2. POISSON – EMERGÊNCIAS
# =====================================================

lambda_emerg = 2
emergencias = np.random.poisson(lambda_emerg, 100)

axs[0, 1].hist(emergencias, bins=8)
axs[0, 1].set_title("Poisson - Emergências")

prob_5 = stats.poisson.pmf(5, lambda_emerg)

print("\n=== Emergências ===")
print("Probabilidade de 5 no mês:", prob_5)


# =====================================================
# 3. BINOMIAL – SEGURANÇA
# =====================================================

n = 200
p = 0.02

deteccoes = np.random.binomial(n, p, size=100)

axs[1, 0].hist(deteccoes, bins=10)
axs[1, 0].set_title("Binomial - Detecção de Ameaças")

prob_3 = stats.binom.pmf(3, n, p)

print("\n=== Segurança ===")
print("Probabilidade de 3 detecções:", prob_3)


# =====================================================
# 4. BERNOULLI – BAGAGENS
# =====================================================

p_correto = 0.98
bagagens = stats.bernoulli.rvs(p_correto, size=1000)

axs[1, 1].bar(["Falha", "Sucesso"],
              [np.sum(bagagens == 0), np.sum(bagagens == 1)])
axs[1, 1].set_title("Bernoulli - Direcionamento de Bagagens")

print("\n=== Bagagens ===")
print("Taxa de acerto:", np.mean(bagagens))


# =====================================================
# 5. MULTINOMIAL – PORTÕES
# =====================================================

voos = 200
prob_portoes = [0.4, 0.35, 0.25]
portoes = np.random.multinomial(voos, prob_portoes)

axs[2, 0].bar(["Portão A", "Portão B", "Portão C"], portoes)
axs[2, 0].set_title("Multinomial - Alocação de Portões")

print("\n=== Portões ===")
print("Distribuição:", portoes)


# =====================================================
# 6. GEOMÉTRICA – FALHA DO SISTEMA
# =====================================================

p_falha = 0.05
falhas = np.random.geometric(p_falha, size=100)

axs[2, 1].hist(falhas, bins=15)
axs[2, 1].set_title("Geométrica - Dias até Falha")

print("\n=== Sistema de Bagagens ===")
print("Média dias até falha:", np.mean(falhas))


# Ajustar layout
plt.tight_layout()
plt.show()
