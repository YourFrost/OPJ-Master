# Infraction Finder

Entraînement aux épreuves de l'examen OPJ : **DPG / DPS** (recherche d'infractions) et **CRT** (compte rendu téléphonique au parquet). Tout est en français.

- **Site statique** publié par GitHub Pages : https://yourfrost.github.io/OPJ-Master/ (dépôt public `YourFrost/OPJ-Master`, branche `main`, racine). Page unique : `index.html`. Version locale hors ligne : `Lancer Infraction Finder.bat` (`python -m http.server`).
- Aucune API d'IA : **Claude génère les exercices (`/exercice`) et les corrige (`/corriger`)**, puis fait `git add`, `git commit` et `git push` pour publier. Le site se met à jour 1 à 2 minutes après le push.
- `data/sujets/index.json` : liste des id d'exercices (le plus récent d'abord), à tenir à jour. `data/sujets/<id>.json` : écrit par Claude. Le corrigé y est lisible (dépôt public) mais la page ne l'affiche qu'une fois la correction publiée.
- La copie de l'utilisateur vit dans son navigateur (`localStorage`). « Envoyer » produit la commande `/corriger <id> <copie JSON>` ; Claude l'enregistre dans `data/copies/<id>.json`, sans la modifier.
- Statuts : nouveau → en cours → terminé (copie envoyée) → corrigé (`data/corrections/<id>.json` publié).
- **Ne jamais publier `_ancien/`** (documentation en diffusion restreinte ; exclu par `.gitignore`).
- Articles : texte **en vigueur** du Code pénal (et des autres codes) sur Légifrance. En cas de doute, vérifier ; ne jamais inventer un article ou un alinéa.

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
Copie (`data/copies/<id>.json`) : `{ reponses: [{ infraction, qualification, mis_en_cause, element_legal, elements_materiels: [{element, justification}], element_moral: {type, justification} }], rendue_le }`

## Sujet CRT
```json
{
  "id": "2026-11-02-crt-incendie", "epreuve": "crt", "titre": "…", "type": "crt", "cree_le": "2026-11-02",
  "theme": "Récit de l'enquête jusqu'au moment de l'appel, puis « Travail demandé » et « Identités »",
  "corrige": { "presentation": "…", "objet": "…", "faits": "…", "actes_realises": "…", "actes_a_realiser": "…", "qualification": "…" },
  "pieges": ["…"]
}
```
Copie (`data/copies/<id>.json`) : `{ blocs: { presentation, objet, faits, actes_realises, actes_a_realiser, qualification }, rendue_le }`

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
