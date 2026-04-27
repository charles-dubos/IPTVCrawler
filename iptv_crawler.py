#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dépendances
from ipytv import playlist
import json,logging, os

def main():
    
    # Chargement des variables d'environnement
    logLevel = os.getenv('LOG_LEVEL', 'INFO')
    logging.basicConfig(level=getattr(logging, logLevel))
    logging.debug(f"Logging activé en mode {logLevel}")
    logging.getLogger("ipytv").setLevel(logging.WARNING)


    logging.info("Début du traitement...")
    outputFile = os.getenv('OUT_FILE',
        os.path.dirname(os.path.abspath(__file__)) + "/iptvList.m3u8")
    configFile = os.getenv('CONFIG_FILE',
        os.path.dirname(os.path.abspath(__file__)) + "/config.json"
    )
    
    # Parsing du fichier json de confs
    logging.debug(f"Chargement du fichier {configFile}")
    with open(configFile, "r") as r_file:
        logging.debug("Chargement du fichier JSON en dictionnaire Python")
        configJson = json.load(r_file)
    # Si pas de conf, generer une erreur
    if not configJson:
        raise FileNotFoundError
    logging.debug("Chargement du fichier de configuration terminé")

    # Recuperation de la playlist complete a l'URL donnée
    logging.debug(f"Connection à l'URL {configJson['sourceUrl']}")
    fullPlaylist = playlist.loadu(configJson["sourceUrl"])
    logging.debug(f"Nombre de canaux téléchargés: {fullPlaylist.length()}")

    # Generation de la nouvelle playlist et import des chaines voulues
    newPlaylist = playlist.M3UPlaylist()
    for channel in configJson["channels"]:
        logging.debug(f"Recherche de {channel['id']}...")
        for chan in fullPlaylist:
            if channel['id'] in chan.name:
                logging.debug(f"{channel['id']} trouvé dans {chan.name}")
                chan.attributes["tvg-chno"] = channel['tvg-chno']
                logging.debug(f"Enregistrement du numero de chaine à {channel['tvg-chno']}")
                newPlaylist.append_channel(chan)
                logging.info(f"{channel['id']} chargé.")
                break
    logging.debug(f"{newPlaylist.length()} chaines chargées.")
    
    # Enregistrement de la sortie dans le fichier de sortie
    with open(outputFile, 'w', encoding='utf-8') as w_file:
        w_file.write(newPlaylist.to_m3u_plus_playlist())
        logging.info(f"Playlist {outputFile} enregistrée.")


if __name__ == "__main__":
    main()
