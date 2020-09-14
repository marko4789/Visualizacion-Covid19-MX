import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("comparativo_muertes_acumuladas.csv")

dias = np.arange(244)
muertes = dataset.iloc[:, 1]

plt.title("Covid-19 MX - Comparativo muertes acumuladas",)
plt.suptitle("13 de Enero - 12 de Septiembre 2020", fontsize = 10)
plt.xlabel("Días")
plt.ylabel("Numero de muertes")
plt.plot(dias, muertes, color = "red", label = "Número de muertes")
plt.legend()
plt.grid(True)
plt.show()