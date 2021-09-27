import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Datos/comparativo_muertes_nuevas.csv")

dias = np.arange(585)
muertes = dataset.iloc[:, 1]
muertes_prom = dataset.iloc[:, 3]

plt.title("Covid-19 MX - Comparativo muertes nuevas",)
plt.suptitle("13 de Enero - 25 de Septiembre 2021", fontsize = 10)
plt.xlabel("Días")
plt.ylabel("Numero de muertes")
plt.plot(dias, muertes_prom, color = "red", label = "Promedio diario")
plt.scatter(dias, muertes, color = "blue", label = "Muertes nuevas diarias", alpha=0.5)
plt.legend()
#plt.grid(True)
plt.show()