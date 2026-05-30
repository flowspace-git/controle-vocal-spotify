import os
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import keyboard 

load_dotenv()

r = sr.Recognizer()
r.pause_threshold = 2

MODE_API_ACTIF = True

try:
    scope = "user-modify-playback-state"
    # On vérifie d'abord si les variables existent dans l'environnement
    if not os.getenv("SPOTIPY_CLIENT_ID") or not os.getenv("SPOTIPY_CLIENT_SECRET"):
        raise ValueError("Clefs manquantes")
        
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.current_user() 
    print("[OK] Version Officielle : Connecte a l'API Spotify.")
except Exception:
    MODE_API_ACTIF = False
    print("[INFO] Mode Local active : Controle par touches multimedias (Pas d'API).")

def ecouter_micro():
    """Écoute le micro et retourne le texte compris, ou une chaîne vide."""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
            text = r.recognize_google(audio, language="fr-FR")
            print(f"Entendu : {text}")
            return text.lower()
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return ""
        except Exception as e:
            print(f"Erreur micro : {e}")
            return ""

def controler_spotify(text):
    """Analyse le texte et exécute la commande via l'API ou via simulation clavier."""
    global MODE_API_ACTIF

    if "precedente" in text or "avant" in text or "d'avant" in text:
        if MODE_API_ACTIF:
            try: sp.previous_track()
            except Exception: pass
        else:
            keyboard.send("previous track")
        print("-> Musique precedente")
            
    elif "remets-moi" in text or "remets" in text or "recommence" in text:
        if MODE_API_ACTIF:
            try: sp.seek_track(0)
            except Exception: pass
        else:
            keyboard.send("previous track")
        print("-> Musique remise a zero / precedente")
            
    elif "skip" in text or "passe" in text or "suivante" in text:
        if MODE_API_ACTIF:
            try: sp.next_track()
            except Exception: pass
        else:
            keyboard.send("next track")
        print("-> Musique suivante (Skip)")
            
    elif "pause" in text:
        if MODE_API_ACTIF:
            try: sp.pause_playback()
            except Exception: pass
        else:
            keyboard.send("play/pause media")
        print("-> Pause")
            
    elif "play" in text or "relance" in text or "mets" in text:
        if MODE_API_ACTIF:
            try: sp.start_playback()
            except Exception: pass
        else:
            keyboard.send("play/pause media")
        print("-> Lecture")

if __name__ == "__main__":
    print("Demarrage du controleur vocal Spotify...")
    
    while True:
        commande = ecouter_micro()
        
        if commande != "":
            mots_cles = ["spotify", "musique", "benger", "skip", "pause", "play"]
            if any(mot in commande for mot in mots_cles):
                controler_spotify(commande)
