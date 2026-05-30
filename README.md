# Contrôleur Vocal Spotify (Mode Hybride : API & Clavier)

Ce script Python vous permet de contrôler la lecture de Spotify par la voix. Vous pouvez dire des commandes comme Play, Pause, Suivant, Précédent ou Recommencer en utilisant le microphone de votre ordinateur.

Le script fonctionne de deux façons selon votre configuration. Il peut être en Mode Officiel ou Mode Local.

---

## Comment ça fonctionne ? (2 Modes disponibles)

1. **Mode Officiel (Avec API)** : Utilise l'API de Spotify pour contrôler votre musique à distance sur n'importe quel appareil connecté. Cela nécessite un abonnement Spotify Premium.
2. **Mode Local (Sans API)** : Si vous n'avez pas de clés API ou de compte Premium, le script simule automatiquement les touches multimédias de votre clavier pour contrôler l'application Spotify ouverte en tâche de fond sur votre ordinateur.

---

## Prérequis & Installation

### 1. Installer les dépendances
Installez les bibliothèques nécessaires en exécutant cette commande dans votre terminal :
```bash
pip install speech_recognition spotipy python-dotenv pyaudio keyboard
```

### 2. Configuration (Optionnelle - Pour le Mode Officiel uniquement)
Si vous souhaitez utiliser l'API officielle :
* **Compte Spotify Premium** : Requis pour modifier la lecture à distance via l'API.
* **Identifiants API** : Créez une application sur le [Dashboard Spotify Developer](https://developer.spotify.com/dashboard).
* **Fichier d'environnement** : Créez un fichier nommé `.env` à la racine du projet et remplissez-le :
  ```env
  SPOTIPY_CLIENT_ID="VOTRE_CLIENT_ID"
  SPOTIPY_CLIENT_SECRET="VOTRE_CLIENT_SECRET"
  SPOTIPY_REDIRECT_URI="http://localhost:8080"
  ```

*Note : Si le fichier `.env` est manquant ou incomplet, le script changera automatiquement en **Mode Local** sans planter.*

---

## Utilisation

Lancez simplement votre script principal :
```bash
python "Nouveau Python Script.py"
```

Le script se met à l'écoute de votre micro :
* **Vérifiez les logs au démarrage** pour voir si vous êtes en version `[OK] Version Officielle` ou `[INFO] Mode Local`.
* **Commandes vocales** : Prononcez des phrases contenant des mots-clés comme *"Spotify"*, *"Musique"*, *"Pause"*, *"Skip"* ou *"Suivante"* pour contrôler votre musique.