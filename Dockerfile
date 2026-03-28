# On part d'une image Python 3.10 propre
FROM python:3.10-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système pour TTS et audio
RUN apt-get update && apt-get install -y \
    espeak-ng \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer les librairies Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier ton code
COPY main.py .

# Dossier pour les fichiers PDF en entrée et audio en sortie
RUN mkdir /input /output

# Lancer le script
CMD ["python", "main.py"]