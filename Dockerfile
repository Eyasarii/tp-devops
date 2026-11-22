# Utiliser une image Python légère basée sur Python 3.11
FROM python:3.11-slim

# Configurer les variables d'environnement :
# PYTHONDONTWRITEBYTECODE : empêche la création des fichiers .pyc
# PYTHONUNBUFFERED : affiche directement les logs dans le terminal
# APP_VERSION : définit la version de l'application
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_VERSION=1.0.0

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python sans conserver le cache pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet dans le conteneur
# Cela inclut notamment le code de l'API et le modèle modele_final.pkl
COPY . .

# Créer un utilisateur non privilégié et lui attribuer les droits sur /app
RUN useradd --create-home appuser && chown -R appuser /app

# Exécuter l'application avec cet utilisateur pour renforcer la sécurité
USER appuser

# Exposer le port utilisé par l'API FastAPI
EXPOSE 8000

# Démarrer l'application avec Uvicorn
# app.main:app correspond au fichier app/main.py et à l'objet FastAPI nommé app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]