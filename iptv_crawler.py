#!/usr/bin/env python3
# -*- coding: utf-8 -*-

URL = "http://iptv-org.github.io/iptv/countries/fr.m3u"
OUTPUT = "./MonIPtv.m3u"

MY_CHANNELS = [
    "TF1 HD",
    "France 2 HD",
    "France 3 HD",
    "France 4 HD",
    "France 5 HD",
    "M6",
    "Arte",
    "LCP",
    "W9",
    "TMC",
    "TFX",
    "Gulli",
    "BFM TV",
    "CNews",
    "LCI",
    "France info",
    "C Star",
    "T18",
    "Novo",
    "TF1 Series Films",
    "L'Equipe",
    "6ter",
    "RMC Story",
    "RMC Decouverte",
    "Cherie 25",
    "Paris Premiere",
    "MTV",
    "Clubbing TV"
]

# Dépendances
from ipytv import playlist

def main():
    fullPlaylist = playlist.loadu(URL)
    newPlaylist = playlist.M3UPlaylist()
    print(f"Nombre de canaux téléchargés: {fullPlaylist.length()}")
    for index,channel in enumerate(MY_CHANNELS):
        for chan in fullPlaylist:
            if channel in chan.name:
                newPlaylist.append_channel(chan)
                break
    print(newPlaylist.length())
    with open(OUTPUT, 'w', encoding='utf-8') as outputFile:
        outputFile.write(newPlaylist.to_m3u_plus_playlist())


if __name__ == "__main__":
    main()