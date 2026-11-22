# ============================================================
# TP4 - Tracking d'expériences avec MLflow
# Objectif : entraîner et comparer 9 modèles de classification
# ============================================================

import mlflow
import mlflow.sklearn  # Sous-module permettant d'enregistrer des modèles scikit-learn
import joblib

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# Utiliser le serveur MLflow lancé sur le port 5000
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# ------------------------------------------------------------
# 1. Chargement du jeu de données
# ------------------------------------------------------------

# Le jeu de données Wine contient des caractéristiques chimiques
# permettant de classer des vins dans différentes catégories.
# X représente les caractéristiques et y les classes à prédire.
X, y = load_wine(return_X_y=True)


# ------------------------------------------------------------
# 2. Séparation des données en entraînement et test
# ------------------------------------------------------------

# 80 % des données servent à entraîner les modèles.
# 20 % servent à évaluer leurs performances.
#
# random_state=42 fixe la graine aléatoire pour obtenir
# la même séparation des données à chaque exécution.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------------------------
# 3. Définition des hyperparamètres à tester
# ------------------------------------------------------------

# n_estimators : nombre d'arbres dans la forêt aléatoire.
# max_depth    : profondeur maximale de chaque arbre.
#
# 3 valeurs pour chaque hyperparamètre donnent :
# 3 x 3 = 9 configurations à tester.
n_estimators_values = [50, 100, 200]
max_depth_values = [3, 6, 10]


# ------------------------------------------------------------
# 4. Entraînement et suivi des expériences avec MLflow
# ------------------------------------------------------------

# La double boucle teste toutes les combinaisons possibles.
for n_estimators in n_estimators_values:
    for max_depth in max_depth_values:

        # Chaque itération crée un run MLflow distinct.
        # Les paramètres, la métrique et le modèle de cette
        # configuration seront enregistrés dans ce run.
        with mlflow.start_run():

            # ----- Enregistrement des hyperparamètres -----

            # Ces valeurs seront visibles dans l'interface MLflow.
            mlflow.log_param("n_estimators", n_estimators)
            mlflow.log_param("max_depth", max_depth)

            # ----- Création du modèle -----

            # random_state=42 rend l'entraînement reproductible.
            modele = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                random_state=42
            )

            # ----- Entraînement du modèle -----

            # Le modèle apprend à partir des données d'entraînement.
            modele.fit(X_train, y_train)

            # ----- Évaluation du modèle -----

            # score() calcule l'accuracy sur les données de test.
            # L'accuracy correspond à la proportion de prédictions
            # correctes parmi l'ensemble des prédictions.
            accuracy = modele.score(X_test, y_test)

            # Enregistrement de l'accuracy dans MLflow.
            # Cette métrique servira à comparer les 9 runs.
            mlflow.log_metric("accuracy", accuracy)

            # ----- Enregistrement du modèle -----

            # Le modèle entraîné est enregistré comme artefact
            # du run, sous le nom "modele".
            mlflow.sklearn.log_model(modele,"modele",skops_trusted_types=["sklearn.tree._tree.Tree"]
)

            # Affichage du résultat dans le terminal.
            print(
                f"n_estimators={n_estimators}, "
                f"max_depth={max_depth}, "
                f"accuracy={accuracy:.4f}"
            )


# ------------------------------------------------------------
# Fin du TP : 9 runs ont été enregistrés dans MLflow
# ------------------------------------------------------------
print("Entraînement terminé : les 9 runs ont été enregistrés.")

# Après la boucle d'entraînement :
meilleur_modele = RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    random_state=42
)

meilleur_modele.fit(X_train, y_train)

joblib.dump(meilleur_modele, "modele_final.pkl")
print("Modèle exporté dans modele_final.pkl")