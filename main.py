import os
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


load_dotenv()


r = sr.Recognizer()
r.pause_threshold = 2

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
    """Analyse le texte et exécute la commande Spotify correspondante."""
    scope = "user-modify-playback-state"
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    except Exception as e:
        print(f"Erreur d'authentification Spotify : {e}")
        return

    if "précédente" in text or "avant" in text or "d'avant" in text:
        try:
            sp.previous_track()
            print("⏮️ Musique précédente")
        except Exception:
            pass
            
    elif "remets-moi" in text or "remets" in text or "recommence" in text:
        try:
            sp.seek_track(0)
            print("🔄 Musique remise à zéro")
        except Exception:
            pass
            
    elif "skip" in text or "passe" in text or "suivante" in text:
        try:
            sp.next_track()
            print("⏭️ Musique suivante")
        except Exception:
            pass
            
    elif "pause" in text:
        try:
            sp.pause_playback()
            print("⏸️ Pause")
        except Exception:
            pass
            
    elif "play" in text or "relance" in text or "mets" in text:
        try:
            sp.start_playback()
            print("▶️ Lecture")
        except Exception:
            pass

if __name__ == "__main__":
    print("Démarrage du contrôleur vocal Spotify...")
    
    while True:
        commande = ecouter_micro()
        
        if commande != "":
            mots_cles = ["spotify", "musique", "benger", "skip", "pause", "play"]
            if any(mot in commande for mot in mots_cles):
                controler_spotify(commande)
