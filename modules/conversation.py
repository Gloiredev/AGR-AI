# modules/conversation.py
from modules.memoire_long_terme import (
                                        ajouter_discussion, 
                                        ajouter_préference
                                        )
from modules.intentions import intentions
from modules.reponses import reponses
import random
from modules.system_control import executer_commande
from modules.meteo import obtenir_meteo_leger

import sys
from datetime import datetime

#PEUT DETECTER ET COMPRENDRE UNE ERREUR DANS LA QUESTION
 

def score_phrase(message, mots_cles):
    score = 0
    message = message.lower().split()
   
    for mot in message:
        for mot_cle in mots_cles:
            if mot in mot_cle or mot_cle in mot:
                score += 1
    return score
   
    

def detecter_intention(message):
    
    meilleur_score = 0
    meilleure_intention = "inconnu"
   
    for intention, mots in intentions.items():
        score = score_phrase(message, mots)
       
        if score > meilleur_score:
            meilleur_score = score
            meilleure_intention = intention
    if intention=="date":
        date=datetime.now()
        return f"nous somme le{date.strftime('%d/%m/%Y')}" 
    
    return meilleure_intention
    intention = detecter_intention(message)
    if intention=="calcul":
        return math
    #-------------pour les calculs-------------
   
   
        #-------------l'heure et les dates-------------    
    if intention=="heure":
        maintenant=datetime.now()
        return f"il est actuellement{maintenant.strftime('%H:%M:%S secondes')}."
    
    if intentions=="ouvrir":
        return executer_commande(message)       
    reponse = reponses.get(intention, reponses["inconnu"])
    if  intention=="meteo":
        return obtenir_meteo_leger(message)
    
    if  intention == ouvrir :
        return executer_commande   
    
   
    # Si plusieurs réponses → choix au hasart
    if isinstance(reponse, list):
        import random
        reponse = random.choice(reponse)
    #sauvegarder les messages 
    ajouter_discussion(message, reponse) 
    analyser_prefernces(message) 


def discuter(message):
    intention = detecter_intention(message)
   
    reponse = reponses.get(intention, reponses["inconnu"])
   
    # Si plusieurs réponses → choix aléatoire
    if isinstance(reponse, list):
        
        reponse = random.choice(reponse)
    #sauvegarder les messages 
    ajouter_discussion(message, reponse) 
    analyser_preferences(message)  
    return reponse
    
    if intention=="date":
        date=datetime.now()
        return f"nous somme le{date.strftime('%d/%m/%Y')}"

def analyser_preferences(message):
    message = message.lower()
    resultat_systeme = executer_commande(message)

    if "je m'appelle" in message:
        nom = message.split("je m'appelle")[-1].strip()
        ajouter_préference("nom_user", nom)

    if "j'aime" in message:
        nom = message.split("j'aime")[-1].strip()
        ajouter_préference("aime", nom)

    
   

    

   
    