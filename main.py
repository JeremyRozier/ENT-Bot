import asyncio
from getpass import getpass
import check_module
from ametice_bot import AmeticeBot

print(
    """\nCe programme permet de télécharger toutes les
ressources disponibles sur ton compte Ametice. Tous les fichiers seront stockés dans le chemin : 
'Fichiers_Ametice/annee_debut:annee_fin/UE/chapitre/fichier'.\n
Tous les dossiers seront automatiquement créés par le programme.\n"""
)

username = input("Nom d'utilisateur : ")
password = getpass(prompt="Mot de passe : ")

ametice_bot = AmeticeBot(username, password)
asyncio.run(ametice_bot.download_all_documents())
