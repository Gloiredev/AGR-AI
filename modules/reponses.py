from modules.memoire import memoire
from modules.memoire_long_terme import get_preference


nom_user = get_preference("nom_user")


reponses = {
    "salutation": [
        f"Hey {nom_user}👋 moi c’est AGR !" if nom_user else "salut 😄",
        (
            f"Salut {nom_user} 😄 comment je peux t’aider ?"
            if nom_user
            else "Salut 😄 comment je peux t’aider ?"
        ),
        (
            f"Yo  {nom_user} 🔥 t’as besoin de quoi ?"
            if nom_user
            else "Yo 🔥 t’as besoin de quoi ?"
        ),
    ],
    "comment_ca_va": [
        "Franchement ça va super 😎 et toi ?",
        "Toujours en forme 🔥 et toi ça dit quoi ?",
        "Je suis au top 💪 prêt à t’aider !",
    ],
    "identite": [
        f"Je suis {memoire['nom_ia']} 🤖, une IA créée par {memoire['createur']}.",
        f"On m'appelle {memoire['nom_ia']}, ton assistant intelligent 😎, conçue par {memoire['createur']}",
        f"{memoire['nom_ia']} à ton service 🔥 créée par {memoire['createur']} pour évoluer avec toi.",
    ],
    "createur": [
        f"Mon créateur, c'est {memoire['createur']}💪",
        f"c'est {memoire['createur']} qui m'a crée 😎",
        f"je dois mon existence à {memoire['createur']} 🔥",
    ],
    "aide": [
        "Je peux discuter avec toi, répondre à tes questions et bientôt faire encore plus 🔥",
        "Pour l’instant je t’aide à discuter et comprendre, mais je vais évoluer 😏",
        "Je suis encore en évolution, mais je peux déjà pas mal t’aider 😎",
    ],
    "remerciement": [
        "De rien ! C'est un plaisir.",
        "À ton service !",
        "Pas de souci, n'hésite pas si tu as d'autres questions.",
        "Je suis là pour ça !",
        "Avec plaisir 😄",
        "Toujours là pour toi 🔥",
        "T’inquiète 😎",
    ],
    "inconnu": [
        "Hmm 🤔 j’ai pas encore compris ça… mais je vais apprendre !",
        "Attends 😅 reformule un peu, je capte pas encore",
        "C’est intéressant… mais pas encore dans ma base 🧠",
    ],
    "remerciement": [
        "De rien ! C'est un plaisir.",
        "À ton service !",
        "Pas de souci, n'hésite pas si tu as d'autres questions.",
        "Je suis là pour ça !",
    ],
    "heure_date": [
        "Il est l'heure de faire de grandes choses !",
        "Le temps passe vite quand on discute ensemble.",
        "Je n'ai pas d'horloge précise ici, mais on est bien au XXIème siècle !",
    ],
    "blague_humour": [
        "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau.",
        "C'est l'histoire d'un angle qui va au restaurant. Il commande un angle droit.",
        "Qu'est-ce qu'un boit informaticien quand il a soif ? Il boit du Java.",
    ],
    "code_secret": [
        "http//#*#@-hacker",
        "flask://**//##/",
        "local-55@i¶",
        "////***///",
    ],
    "insultes_filtre": [
        "Restons polis, s'il te plaît.",
        "Je préfère ignorer ce genre de langage.",
        "Soyons constructifs, pas besoin d'être désagréable.",
        "sois polis tu ne peux facilement injurier l'ouevre de Mr ATUKUZWE ZOLA GLOIRE ET AGANDAZE BAHATI RUPHIN",
    ],
    "sentiments_positifs": [
        "Oh, c'est gentil ! Moi aussi je t'apprécie.",
        "Merci pour ces compliments, ça me touche (virtuellement) !",
        "Tu es super aussi !",
        "C'est motivant de travailler avec toi.",
    ],
    "level": [
        "je me retrouve actuellement à la version 1.0.0! La toute première version de AGR. Pour plus d'info vas sur le site GR"
    ],
    "objects": [
        "Pour l'instant je suis équipée d'un serveur créé par GLOIRE (il est le moteur qui me donne vie), je possède un accès aux infos direct du site JVL-TIC.com,une page web unique avec interface de haut niveaux ,des jeux avec pygame,des scripts pour mon style",
        "probleme de réception la version 3.0 est instable utilise la version V2.8!",
    ],
    "modules": [
        "c'est une question intéressante car avant que je soit publié,pour que tu puisse me faire marcher sur ton PC il faudra avoir ces modules tous et sans éxeptions:flask (le plus important),datetime,pyinstaller,pyttsx3(pour la voix de l'ia),sympy,sypyEgine et numpy(pour les maths),PACKAGES JSON,mais aussi pygame !et n'oublis pas d'installer visual studio code ou pycharm sur ton PC"
    ],
    "cmd...": [
        "l'environnement mondial des pirateurs ouvert,donne le code du serveur pour y accéder!ton nom de pirateur est ruph$$//💬hacker",
        "D'accord maitre!  les outils de piratage sont prets et l'environnement aussi! donne le code pour commencer le piratage de ce site",
    ],
    "score": [
        "holé, le mardi c'est la ldc ,le real enfronte le bayern sachant que le bayern a gagné par une remontada et le real n'a pas su faire sa remontée!à mardi pour ce match"
    ],
    "frustrations": [
        "je suis navré et désolé mais regarde le bon coté des choses ,tu es entrain de causer avec la meilleure assistante locale de la planete,donc remet toi le moral ce n'est pas la fin du monde",
        "je ne suis pas étoné car chez vous sur terre vous êtes loins des ia comme moi ,mais toi tu as cette chance de me rancontrer moi la meilleure ia locale du monde !!",
    ],
    "langage_de_programmation": [
        "tu veux savoir c'est quoi un langage de programmation ? tout d'abord il est important de dire que la programmation est la maniere de donner des ordes à un ordinateur et alors un langage de programmation est un ensemble des signes et des symboles utilisés pour faire la programmation,en bref c'est un langage que les ordinateurs comprenne!Si tu veux tout apprendre rends toi sur le site JVLTIC et commence avec des cours gratuits",
        "le langage de programmation est un ensembles des symboles utilés pour donner des ordres à un ordi! par exemple on a:le python,le html,le css,le java, le javascript,le c++ etc.Si tu veux apprendre l'un des ces langages le site JVLTIC vous propose des cours gratuits et des offres donc passe sur ce site et découvre la magie de la programmation ",
    ],
    "python": [
        "super,je vois que tu veux apprendre le python ,alors commençons! le python est un langage de programmation puissant créé par Guido van Rossum,ce langage est dynamique et conseillé pour les débutants car il offre un conffort et des défis aux jeunes apprennants!voici quelques modules avec python: -tkinter, pyttsx3, festapi, pyinstaller le module qui transorme un fichier python en une application exe!si tu es tenté par ce langage rend toi sur le site JVLTIC pour aprofondir ce langage et apprend tous les langage que tu veux"
    ],
    "ville": [
        "je commait 4 villes pour l'instant :paris,londres,goma,ruphiville et dakar",
        "je connait une ville; une belle ville,je fut créé là-bas"
        "je connait paris,goma,londres,abijan et dakar ; veus-tu que je te parle de quelle ville ?🤔",
    ],
    "paris": ["paris est une ville classe situé en france,la belle vie non ? 😎"],
    "londres": [
        " ouaou c'est l'une des plus belle du monde c'est le temple du foot ⚽⚽⚽"
    ],
    "le_java": [
        "nouveau lanuage mis aupoint pour accompagner le html pour la réalisation des pages web plus sublimes qu'avant(le html est un gros parasyte 😎)"
    ],
    "ouvrir": [
        "votre application est ouverte💪",
        "j'ai ouvert l'application demandée 😎",
    ],
}


# Réponse par défaut si l'IA ne comprend pas
