"""Affiche le contenu des champs d'un ou plusieurs imprimés PDF remplis (651.4.101 / 102 / 103).

    python outils/lire_formulaire.py copie1.pdf [copie2.pdf …]

Les champs d'identification (nom, date de naissance…) sont ignorés : seule la réponse est lue.
"""
import sys

from pypdf import PdfReader

IDENTITE = {"id_coex", "ne_jour", "ne_mois", "ne_annee", "nom", "prenom", "concours", "epreuve", "session", "feuille_n", "feuille_total"}

sys.stdout.reconfigure(encoding="utf-8")
for chemin in sys.argv[1:]:
    champs = PdfReader(chemin).get_fields() or {}
    print(f"===== {chemin}")
    for nom, champ in champs.items():  # ordre du formulaire : p1R (recto), p1L, p2L, p2R
        valeur = str(champ.get("/V") or "").strip()
        if nom not in IDENTITE and valeur:
            print(f"[{nom}]\n{valeur}\n")
