# Crawler IPTV

Reformate la liste IPTV avec des numéros de chaines, uniquement sur les chaines choisies dans la configuration.

## Lancement de l'application

Installer avec `pip install -r requirements.txt`

Exécuter avec `./iptv_crawler.py`

## Paramètres (variables d'environnement)

variable | objet | valeur par défaut
---|---|---
`LOG_LEVEL` | verbosité des logs (cf https://docs.python.org/3/library/logging.html#levels) | INFO
`OUT_FILE` | fichier m3u8 de sortie | `iptvList.m3u8`
`CONFIG_FILE` | fichier de configuration des chaines | `config.json`

## Structure du fichier de configuration

Le fichier est un JSON formatté ainsi:

```json
{
    "sourceUrl": "<url des chaines à crawler>",
    "channels": [
        {"id": "<identifiant de corrélation de la chaine>", "tvg-chno": "<numéro de la chaine>"},
        ...
        {"id": "<identifiant de corrélation de la chaine>", "tvg-chno": "<numéro de la chaine>"}
    ]
}
```

---
Codé avec les :foot: :foot: par moi...