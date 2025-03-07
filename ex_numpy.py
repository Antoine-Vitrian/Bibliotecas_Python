import numpy as np
import matplotlib.pyplot as plt

vendas = np.random.randint(1000, 3000, 50)

meses = np.arange(1, 51)


plt.plot(meses, vendas, color = "#1eeffa") # cor linha do gráfico
plt.gca().set_facecolor("lightyellow") # cor gráfico
plt.ylabel("Vendas")
plt.xlabel("Meses")
plt.axis([0, 50, 0, max(vendas)+500])
plt.show()