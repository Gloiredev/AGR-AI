import urllib.request
import json
def obtenir_meteo_leger(ville="Goma"):
    # On utilise une API gratuite sans clé complexe pour le test (ex: wttr.in)
    # wttr.in renvoie du texte pur ou du JSON sans module externe
    url = f"https://wttr.in/{ville}?format=j1"
   
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            temp = data['current_condition'][0]['temp_C']
            desc = data['current_condition'][0]['lang_fr'][0]['value']
            return f"À {ville}, il fait {temp}°C avec {desc}."
    except:
        return "le serveur méteo déconnecté,vérifie ta connection "