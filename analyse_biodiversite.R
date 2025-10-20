# Analyse de la biodiversité - TP SNV
# Chargement des données
data <- read.csv("data/site_espece_abondance.csv")

# Calcul du nombre d'espèces par site
library(dplyr)
richesse <- data %>%
  group_by(Site) %>%
  summarise(nb_especes = n_distinct(Espece))

write.csv(richesse, "results/tableau_indices.csv", row.names = FALSE)

print("Analyse terminée : tableau des indices enregistré dans results/.")
