import socket
import pyautogui 
import threading
import time
import pandas as pd

# Détails du serveur IRC de Twitch
SERVEUR = "irc.twitch.tv"
PORT = 6667
MDP = "" #Mettez votre clé OAuth ici
BOT = "TwitchBot"
CHAÎNE = "" #mettez votre pseudonyme/nom d'utilisateur ici
PROPRIÉTAIRE = "" #mettez votre pseudonyme/nom d'utilisateur ici
message = ""

# Connexion au chat Twitch
irc = socket.socket()
irc.connect((SERVEUR, PORT))
irc.send(("PASS " + MDP + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHAÎNE + "\n").encode()) 

# Configuration de base pour la collecte des votes
max_votes = 1  # Modifier cette variable pour changer le nombre de votes par cycle
intervalle = 2  # Modifier cette variable pour changer la durée du vote
dernière_action = time.time()
liste_messages = []
liste_utilisateurs = []
total_votes = []
touches = ['z', 's', 'q', 'd', 'a', 'b', 'enter']
compteur_touches = [0] * len(touches)
bool_exec = True

# Charger les votes précédents depuis un fichier CSV
#Ces deux lignes peuvent être effacée avec le reste des lignes lié à pandas (ligne 121)
df_vote = pd.read_csv("votes.csv", sep=";")
liste_votes = list(df_vote["Vote"])

def sectionTwitch():
    # Gère la connexion au chat Twitch et la récupération des messages
    global dernière_action
    def rejoindreChat():
        # Rejoint le chat Twitch
        Chargement = True
        while Chargement:
            tampon_lecture = irc.recv(1024).decode()
            for ligne in tampon_lecture.split("\n")[0:-1]:
                print(ligne)
                Chargement = chargementTerminé(ligne)
    
    def chargementTerminé(ligne):
        # Confirme la connexion réussie au chat
        if("End of /NAMES list" in ligne):
            print("Le bot a rejoint la chaîne de " + CHAÎNE + " !")
            envoyerMessage(irc, "Le chat a été rejoint")
            return False
        else:
            return True
    
    def envoyerMessage(irc, message):
        # Envoie un message dans le chat Twitch
        tempMessage = "PRIVMSG #" + CHAÎNE + " :" + message
        irc.send((tempMessage + "\n").encode())
    
    def obtenirUtilisateur(ligne):
        # Extrait le nom d'utilisateur du message
        separate = ligne.split(":", 2)
        utilisateur = separate[1].split("!", 1)[0]
        return utilisateur
    
    def obtenirMessage(ligne):
        # Extrait le contenu du message
        global message
        try:
            message = (ligne.split(":", 2))[2]
        except:
            message = ""
        return message
    
    def estConsole(ligne):
        # Vérifie si la ligne est un message de console ou un message de chat
        return "PRIVMSG" not in ligne
    
    rejoindreChat()

    while True:
        try:
            tampon_lecture = irc.recv(1024).decode()
        except: 
            tampon_lecture = ""
        for ligne in tampon_lecture.split("\r\n"):
            if ligne == "":
                continue
            if "PING" in ligne and estConsole(ligne):
                # Répond aux messages PING de Twitch pour maintenir la connexion
                message_ping = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(message_ping)
                print(message_ping)
                continue
            else:
                # Traite les messages entrants
                utilisateur = obtenirUtilisateur(ligne)
                message = obtenirMessage(ligne)
                print(utilisateur + " : " + message)
                liste_messages.append(message.lower())  # Stocker le message reçu
                liste_utilisateurs.append(utilisateur)
                temps_actuel = time.time()
                if temps_actuel - dernière_action >= intervalle:
                    gagnant = compterVotes()
                    total_votes.append(gagnant)
                    envoyerMessage(irc, "Touche exécutée : " + str(gagnant) + ".")
                    envoyerMessage(irc, " -> par : " + liste_utilisateurs[0])
                if len(liste_messages) >= max_votes:
                    liste_messages.clear()
                    liste_utilisateurs.clear()
                    dernière_action = temps_actuel
            
            # Stocker les résultats des votes dans le fichier CSV
            #Ces trois lignes peuvent être effacée avec le reste des lignes lié à pandas (ligne 37)
            liste_votes.append(gagnant)
            df_vote = pd.DataFrame({"Vote": liste_votes})
            df_vote.to_csv("votes.csv", index=False, sep=";")

def compterVotes():
    # Compte les votes et exécute la touche la plus votée
    global compteur_touches, bool_exec
    for message in liste_messages:
        for i, touche in enumerate(touches):
            if touche in message:
                compteur_touches[i] += 1
    
    # Trouver la touche la plus votée
    index_max = compteur_touches.index(max(compteur_touches))
    if compteur_touches[index_max] > 0:
        pyautogui.keyDown(touches[index_max])
        pyautogui.keyUp(touches[index_max])
        print(f"Exécution de l'action : {touches[index_max]}")
        bool_exec = False
    compteur_touches = [0] * len(touches)

    return touches[index_max]

print(f"La touche la plus votée de cette session est : {max(liste_votes, key=liste_votes.count)}")

# Utilisation du threading pour exécuter plusieurs boucles simultanément
if __name__ == '__main__':
    t1 = threading.Thread(target=sectionTwitch)
    t1.start()
