import matplotlib.pyplot as plt
import numpy as np

# Dados
x = [50, 40, 39]
y = np.random.randint(12, 23, size=3)  # 3 valores aleatórios entre 12 e 22

# Estilização do gráfico
plt.plot(
    x, y,
    marker='o',                 # Marcador nos pontos
    linestyle='--',             # Linha tracejada
    color="#700054",            # Cor do gráfico (roxo escuro)
    linewidth=2,                # Espessura da linha
    markerfacecolor='pink',     # Cor interna dos marcadores
    markeredgecolor='black',    # Borda dos marcadores
    markersize=8                # Tamanho dos marcadores
)

# Títulos e legendas
plt.xlabel('Valores X', fontsize=12)
plt.ylabel('Valores Y', fontsize=12)
plt.title('Gráfico de Linha Estilizado', fontsize=14, fontweight='bold')

# Grade
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Fundo
plt.gca().set_facecolor('#f0f0f0')  # cor de fundo do gráfico

# Mostrar gráfico
plt.tight_layout()
plt.show()
