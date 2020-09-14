import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("comparativo_casos_nuevos.csv")

dias = np.arange(244)
casos = dataset.iloc[:, 1]
casos_prom = dataset.iloc[:, 3]

plt.title("Covid-19 MX - Comparativo casos nuevos",)
plt.suptitle("13 de Enero - 12 de Septiembre 2020", fontsize = 10)
plt.xlabel("Días")
plt.ylabel("Numero de casos")
plt.plot(dias, casos_prom, color = "red", label = "Promedio diario")
plt.scatter(dias, casos, color = "blue", label = "Casos nuevos diarios", alpha=0.5)
plt.legend()
#plt.grid(True)
plt.show()