# Python Joue à Pokémon  
[🇫🇷 Français](README.md) | [🇬🇧 English](README.en.md)  

## Aperçu  
Ce projet est un script Python qui simule une partie de Pokémon via un chat en direct sur Twitch ! Le script interagit avec un jeu Pokémon (ou tout autre jeu Gameboy) en envoyant des commandes via le chat pour contrôler le jeu, comme déplacer le personnage, combattre et naviguer dans les menus.  
L'objectif était de créer un projet amusant où je peux interagir avec différentes personnes et voir leurs choix en jeu.  
Je l'ai réalisé en 2023/2024 pendant ma dernière année de lycée.  

## Fonctionnalités  
- **Gameplay automatisé** : Le script peut simuler des pressions de touches pour contrôler le jeu.  
- **Actions personnalisables** : Les utilisateurs peuvent définir des séquences d’actions pour accomplir des tâches spécifiques dans le jeu.  
- **Intégration avec les émulateurs** : Le script est conçu pour fonctionner avec des émulateurs populaires permettant le contrôle via des entrées externes.  
- **Récupération des votes** : J’ai utilisé Pandas pour récupérer les votes dans un fichier CSV. >> Ce n'est en réalité pas nécessaire, donc tout ce qui s'y rapporte peut être supprimé. <<  

## Prérequis  
- Python 3.x  
- Une ROM Pokémon GBA  
- Un émulateur prenant en charge le contrôle via des entrées externes (J’ai utilisé Visual Boy Advance personnellement. Lien : [https://visualboyadvance.org/](https://visualboyadvance.org/))  
- Un service de streaming en direct tel qu’OBS ou Streamlabs  
- Bibliothèques Python requises : `pyautogui`, `pandas` (si vous ne supprimez pas les lignes de code correspondantes à pandas)  
  Exécutez simplement dans un terminal :  
   ```bash
   pip install pyautogui
   ```  
   ```bash
   pip install pandas
   ```  

## Installation  
1. **Cloner le dépôt** :  
   ```bash
   git clone https://github.com/ehallou/newton-plays-pokemon.git
   cd newton-plays-pokemon
   ```  
2. **Configurer l’émulateur** :  
   - Assurez-vous que votre émulateur est configuré pour accepter les entrées externes.  
   - Chargez la ROM Pokémon dans l’émulateur.  
   - Changez ou conservez les contrôles par défaut (ex. Z, Q, S, D).  

3. **Modifier la clé OAuth ainsi que USER et PASS avec vos propres identifiants** :  
   Vous pouvez obtenir votre clé OAuth ici après vous être connecté à Twitch :  
   [https://twitchtokengenerator.com/](https://twitchtokengenerator.com/)  
   Ce site devrait fonctionner. Si ce n'est pas le cas, d'autres alternatives existent.  

4. **Exécuter le script** :  
   ```bash
   python newton-plays-pokemon-FR.py
   ```  

5. **Diffusion en direct**  
   Il existe de nombreux tutoriels en ligne expliquant comment configurer un live stream :  
   [https://www.lifewire.com/twitch-streaming-with-obs-studio-4151808](https://www.lifewire.com/twitch-streaming-with-obs-studio-4151808)  

## Utilisation  
- **Exécuter le script** : Lancez le script pendant que l’émulateur est actif. Il enverra les entrées au jeu via le chat Twitch.  
  (L’émulateur doit être la fenêtre sélectionnée pour recevoir les entrées.)  

## Exemple  
Voici un exemple simple de séquence d’appuis sur les touches envoyée par le script :  
![image](https://github.com/user-attachments/assets/591f3316-ac08-4ee1-bec3-fae67e5eab3c)  

## Contributions  
Comme j’ai terminé ce projet en 2024, je n’ai pas de problème avec les contributions.  
Les contributions sont donc les bienvenues ! Forkez le dépôt et soumettez une pull request avec vos modifications.  

## Licence  
Ce projet n’est pas sous licence, vous êtes libre de l’utiliser comme bon vous semble.  

## Remerciements  
- Un grand merci à mon professeur de NSI pour l’idée de ce projet !  
- Merci aux créateurs des jeux Pokémon et aux développeurs des émulateurs.  
- Inspiré par différentes communautés d’automatisation ET par l’expérience sociale "Twitch Plays Pokémon".  
  En savoir plus ici : [https://fr.wikipedia.org/wiki/Twitch_Plays_Pok%C3%A9mon](https://fr.wikipedia.org/wiki/Twitch_Plays_Pok%C3%A9mon)  

## Avertissement  
Ce projet est uniquement destiné à des fins éducatives et de divertissement.  

