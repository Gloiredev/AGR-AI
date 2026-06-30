
from modules.generation_image import generer_image
from modules.generation_code import generer_code
from modules.analyse_donnees import analyser_donnees
from modules.conversation import discuter
from modules.memoire import memoire

def main():
    print("=== AGR est en ligne  ===")
   
    while True:
        user = input("gloire: ")
       
        if user.lower() in ["quit", "exit"]:
            print("AGR : À bientôt 👋")
            break
       
        reponse = discuter(user)
        print("AGR :", reponse)


if __name__ == "__main__":
    main()
