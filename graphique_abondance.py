# Script Python - Visualisation de l'abondance des espèces
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/site_espece_abondance.csv")
pivot = data.pivot_table(values="Abondance", index="Espece", columns="Site", fill_value=0)

pivot.plot(kind="bar")
plt.title("Abondance des espèces par site")
plt.ylabel("Nombre d'individus")
plt.tight_layout()
plt.savefig("results/figures/diversite_sites.png")

print("Graphique enregistré dans results/figures/.")
