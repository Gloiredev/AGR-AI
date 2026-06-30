import subprocess
import os
import sys

PASSWORD = "deuxi"

print("=== BASE DE DONNÉES ELIA ===")

code = input("Mot de passe : ")

if code == PASSWORD:
    print("✔ Accès autorisé")

    # créer autorisation
    with open("access.key", "w") as f:
        f.write("OK")

    # lancer ELIA automatiquement
    print(" accés autorisé")
    os.system("python AGR_OPEN.py")
    sys.exit()

else:
    print("❌ Mot de passe incorrect")
    sys.exit