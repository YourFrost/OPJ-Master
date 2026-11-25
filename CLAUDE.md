# Infraction Finder

Entraînement aux épreuves de l'examen OPJ : **DPG / DPS** (recherche d'infractions) et **CRT** (compte rendu téléphonique au parquet). Tout est en français.

- `python serveur.py` → http://127.0.0.1:8765 (raccourci : `Lancer Infraction Finder.bat`). Page unique : `web/index.html`.
- Aucune API d'IA : **Claude génère les exercices (`/exercice`) et les corrige (`/corriger`).** La correction est écrite dans `data/corrections/<id>.json` et s'affiche sur la plateforme.
- `data/sujets/<id>.json` : écrit par Claude. Le champ `corrige` n'est envoyé au navigateur qu'une fois la correction écrite.
- `data/copies/<id>.json` : écrit par l'application, et seulement par elle. `rendue_le` indique que l'exercice est terminé.
- Statuts : nouveau → en cours → terminé (copie envoyée) → corrigé (fichier de correction présent).
- Articles : texte **en vigueur** du Code pénal (et des autres codes) sur Légifrance. En cas de doute, vérifier ; ne jamais inventer un article ou un alinéa.
- L'ancienne version du projet est rangée dans `_ancien/` (ne pas l'utiliser).

## Sujet DPG / DPS
```json
{
  "id": "2026-11-02-u-velo", "epreuve": "dps",            // id : [a-z0-9-], préfixé de la date
  "titre": "Paul et le vélo", "type": "unitaire",          // "unitaire" | "multiple"
  "nb_min": 1, "nb_max": 1, "cree_le": "2026-11-02",
  "theme": "Texte du sujet (paragraphes séparés par des lignes vides)",
  "corrige": [{
    "mis_en_cause": "Paul", "infraction": "Tentative de vol", "qualification": "Délit",
    "element_legal": "Art. 121-4, 121-5, 311-1, 311-3 et 311-13 du Code pénal",
    "elements_materiels": [{ "element": "…", "justification": "faits du sujet" }],
    "element_moral": { "type": "Infraction intentionnelle", "justification": "…" }
  }],
  "pieges": ["Infraction voisine à ne pas retenir, et pourquoi"]
}
```
Copie : `{ reponses: [{ infraction, qualification, mis_en_cause, element_legal, elements_materiels: [{element, justification}], element_moral: {type, justification} }], rendue_le }`

## Sujet CRT
```json
{
  "id": "2026-11-02-crt-incendie", "epreuve": "crt", "titre": "…", "type": "crt", "cree_le": "2026-11-02",
  "theme": "Récit de l'enquête jusqu'au moment de l'appel, puis « Travail demandé » et « Identités »",
  "corrige": { "presentation": "…", "objet": "…", "faits": "…", "actes_realises": "…", "actes_a_realiser": "…", "qualification": "…" },
  "pieges": ["…"]
}
```
Copie : `{ blocs: { presentation, objet, faits, actes_realises, actes_a_realiser, qualification }, rendue_le }`

## Correction `data/corrections/<id>.json` (les deux épreuves)
```json
{
  "note": "14,5 / 20",                       // facultatif (CRT : barème sur 20)
  "bilan": "Une ou deux phrases.",
  "sections": [ { "titre": "Extorsion aggravée – élément légal", "statut": "ok", "points": "3 / 4", "commentaire": "…" } ],
  "conseils": ["…", "…"]
}
```
`statut` : `ok` (✅), `partiel` (⚠️) ou `faux` (❌). `points` est facultatif.
