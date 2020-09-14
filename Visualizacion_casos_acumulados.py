import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("comparativo_casos_acumulados.csv")

dias = np.arange(244)
casos = dataset.iloc[:, 1]

plt.title("Covid-19 MX - Comparativo casos acumulados",)
plt.suptitle("13 de Enero - 12 de Septiembre 2020", fontsize = 10)
plt.xlabel("Días")
plt.ylabel("Numero de casos")
plt.plot(dias, casos, color = "blue", label = "Número de casos")
plt.legend()
#plt.grid(True)
plt.show()