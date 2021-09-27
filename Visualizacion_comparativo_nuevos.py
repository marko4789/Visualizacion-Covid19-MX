import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset_casos = pd.read_csv("Datos/comparativo_casos_nuevos.csv")
dataset_muertes = pd.read_csv("Datos/comparativo_muertes_nuevas.csv")

dias = np.arange(585)
casos = dataset_casos.iloc[:, 1]
casos_prom = dataset_casos.iloc[:, 3]
muertes = dataset_muertes.iloc[:, 1]
muertes_prom = dataset_muertes.iloc[:, 3]

plt.title("Covid-19 MX - Comparativo casos-muertes diarias")
plt.suptitle("13 de Enero - 25 de Septiembre 2021", fontsize = 10)
plt.xlabel("Días")
plt.ylabel("Numero de casos-muertes")
plt.plot(dias, casos_prom, color = "green", label = "Promedio diario de casos")
plt.scatter(dias, casos, color = "blue", label = "Casos nuevos diarios", alpha=0.5)
plt.plot(dias, muertes_prom, color = "orange", label = "Promedio diario de muertes")
plt.scatter(dias, muertes, color = "red", label = "Muertes nuevas diarias", alpha=0.5)
plt.legend()
#plt.semilogy()
#plt.grid(True)
plt.show()