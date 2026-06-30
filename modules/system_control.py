import os
import sys

APPLICATIONS = {
    "chrome": "start chrome",
    "edge": "start msedge",
    "firefox": "start firefox",
    "excel": "start excel",
    "word": "start winword",
    "powerpoint": "start powerpnt",
    "access": "start msaccess",
    "onenote": "start onenote",
    "outlook": "start outlook",
    "bloc-notes": "start notepad",
    "notepad": "start notepad",
    "calculatrice": "start calc",
    "paint": "start mspaint",
    "cmd": "start cmd",
    "powershell": "start powershell",
    "explorateur": "start explorer",
    "paramètres": "start ms-settings:",
    "gestionnaire des tâches": "start taskmgr",
    "visual studio code": "start code",
    "vscode": "start code",
    "spotify": "start spotify",
    "discord": "start discord",
    "telegram": "start telegram",
    "whatsapp": "start whatsapp",
    "steam": "start steam",
    "obs": "start obs64",
    "vlc": "start vlc",
    "photoshop": "start photoshop",
    "illustrator": "start illustrator",
    "premiere": "start premiere",
    "after effects": "start afterfx",
    "zoom": "start zoom",
    "skype": "start skype",
    "filezilla": "start filezilla"
}

def executer_commande(message):
    message = message.lower()

    if "ouvre" in message:
        for nom, commande in APPLICATIONS.items():
            if nom in message:
                try:
                    os.system(commande)
                    return f"{nom.capitalize()} est ouvert."
                except:
                    return f"Impossible d'ouvrir {nom}."

    if "ouvre le disque" in message:
        try:
            lettre = message.split("ouvre le disque")[1].strip()[0].upper()
            chemin = f"{lettre}:\\"
            if os.path.exists(chemin):
                os.startfile(chemin)
                return f"Disque {lettre} ouvert."
        except:
            return "Erreur ouverture disque."

    return None
