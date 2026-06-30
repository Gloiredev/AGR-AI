# ===============================
# 1️⃣ IMPORTER LA LIBRAIRIE
# ===============================

# On importe CustomTkinter et on lui donne
# un surnom "ctk" pour écrire moins
import customtkinter as ctk
from modules.conversation import discuter

# ===============================
# 2️⃣ CONFIGURATION VISUELLE
# ===============================

# Définit le mode d'apparence
# "dark" = mode sombre
# "light" = mode clair
# "system" = suit Windows
ctk.set_appearance_mode("dark")
let= discuter
# Définit la couleur principale des boutons
ctk.set_default_color_theme("blue")


# ===============================
# 3️⃣ CRÉER LA FENÊTRE PRINCIPALE
# ===============================

# CTk() crée la fenêtre de l'application
app = ctk.CTk()

# Titre affiché en haut de la fenêtre
app.title("Mon Assistant IA de gloire")

# Taille de la fenêtre
# largeur x hauteur
app.geometry("450x600")

# Empêche l'utilisateur de redimensionner
# False = bloqué horizontalement
# False = bloqué verticalement
app.resizable(False, False)

# Garde la fenêtre toujours au-dessus
# des autres programmes
app.attributes("-topmost", True)


# ===============================
# 4️⃣ CRÉER UNE ZONE (FRAME)
# ===============================

# Un Frame = un conteneur
# comme une boîte pour organiser les éléments
frame = ctk.CTkFrame(app, fg_color="violet")

# pack() place le frame dans la fenêtre
# fill="both" → prend toute la place
# expand=True → s'adapte à la taille
# padx/pady → marges extérieures
frame.pack(fill="both", expand=True, padx=10, pady=10)


# ===============================
# 5️⃣ ZONE DE DISCUSSION (CHAT)
# ===============================

# CTkTextbox = zone où on peut afficher du texte
chat_box = ctk.CTkTextbox(frame,
                          width=400,
                          height=450)

# On place la zone dans le frame
chat_box.pack(pady=10)

# insert() permet d'écrire du texte dedans
# "end" signifie écrire à la fin
chat_box.insert("end", "Assistant prêt...\n")


# ===============================
# 6️⃣ CHAMP POUR ÉCRIRE
# ===============================

# Entry = champ où l'utilisateur écrit
entry = ctk.CTkEntry(frame,
                     placeholder_text="Pose ta question...",
                     width=400)

entry.pack(pady=5)


# ===============================
# 7️⃣ CRÉER UNE FONCTION
# ===============================

# Une fonction est un bloc de code
# qui s'exécute quand on clique sur un bouton
def envoyer():

    # récupère le texte écrit par l'utilisateur
    question = entry.get()

    # affiche le message utilisateur
    chat_box.insert("end", f"\nToi : {question}\n")

    # réponse simple simulée
    chat_box.insert("end",f"ELIA; {let}")

    # efface le champ d'écriture
    entry.delete(0, "end")


# ===============================
# 8️⃣ BOUTON ENVOYER
# ===============================

# Création du bouton
btn = ctk.CTkButton(frame,
                    text=" 💬",
                    fg_color="#6C5CE7",
                    hover_color="#4834d4",
                    command=envoyer)
# command = fonction appelée quand on clique

btn.pack(pady=10)


# ===============================
# 9️⃣ LANCER L'APPLICATION
# ===============================

# mainloop() démarre la fenêtre
# Sans ça → rien ne s'affiche
app.mainloop()

