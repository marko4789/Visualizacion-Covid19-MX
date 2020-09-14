import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset_casos = pd.read_csv("comparativo_casos_acumulados.csv")
dataset_muertes = pd.read_csv("comparativo_muertes_acumuladas.csv")

dias = np.arange(244)
casos = dataset_casos.iloc[:, 1]
muertes = dataset_muertes.iloc[:, 1]

plt.title("Covid-19 MX - Comparativo casos-muertes acumuladas")
plt.suptitle("13 de Enero - 12 de Septiembre 2020", fontsize = 10)
plt.xlabel("Días")
plt.ylabel("Numero de casos-muertes")
plt.plot(dias, casos, color = "blue", label = "Número de casos")
plt.plot(dias, muertes, color = "red", label = "Número de muertes")
plt.legend()
plt.grid(True)
plt.show()