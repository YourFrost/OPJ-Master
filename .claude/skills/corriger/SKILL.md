---
name: corriger
description: Corrige un exercice OPJ Master terminé (DPG/DPS, CRT ou procédure pénale), écrit la correction pour la plateforme et la résume dans la discussion. Utiliser quand l'utilisateur tape /corriger ou demande la correction de sa réponse.
argument-hint: "<id de l'exercice> <copie JSON collée depuis le site>"
---

Arguments : `$ARGUMENTS` = l'id de l'exercice, suivi de la copie au format JSON (produite par le bouton « Envoyer » du site).

1. Lire `CLAUDE.md` et `data/sujets/<id>.json` (avec `corrige` et `pieges`). Valider la copie collée (`json.loads`) : si elle manque, est invalide ou n'a pas `rendue_le`, demander à l'utilisateur de cliquer sur « Envoyer » et de recoller la commande. Enregistrer la copie **telle quelle** dans `data/copies/<id>.json`, sans la modifier. Si aucun JSON n'est fourni mais que `data/copies/<id>.json` existe déjà avec `rendue_le`, utiliser ce fichier.
   **Réponse sur formulaire PDF** (`"mode": "pdf"`) : l'utilisateur joint ses imprimés remplis (101, 102, 103). Les lire avec `python outils/lire_formulaire.py <pdf…>`, puis enregistrer la copie avec le texte lu dans `"extraction"`. Ne pas reprendre l'identité (nom, date de naissance) : le script l'ignore déjà. S'il manque un PDF, le demander. Corriger ensuite comme une réponse en ligne.
2. Juger le fond, pas la formulation : une réponse exacte avec d'autres mots est juste. En cas de doute sur un article, **vérifier sur Légifrance** avant de corriger l'utilisateur.

## DPG / DPS
Associer chaque infraction du corrigé à la réponse qui la traite (d'après les faits et le mis en cause). Pour chacune, une section par point à vérifier :
- **Qualification** : crime ou délit ? Une erreur ici est grave : à l'examen, elle met l'infraction à zéro.
- **Élément légal** : articles et alinéas justes, manquants ou faux.
- **Élément matériel** : chaque élément attendu est-il présent, et chaque justification s'appuie-t-elle sur un fait réel du sujet ?
- **Élément moral** : le bon type, justifié par le sujet.

Ajouter une section pour les infractions oubliées ou relevées à tort, en expliquant le piège.

## CRT
Une section par bloc, notée sur son barème :
- **Présentation (/0,5)**.
- **Objet (/3)** : un cadre juridique faux ou absent met la rubrique à 0.
- **Faits (/4,5)** : synthèse fidèle et complète, sans recopie.
- **Actes réalisés (/4)** et **actes à réaliser (/4)** : nommés et motivés. Toute stratégie conforme au droit et au thème est acceptée, même si elle diffère du corrigé ; aucun acte inventé.
- **Qualification (/4)**, pour chaque infraction : 0 si elle est mal qualifiée (crime ou délit), relevée contre la mauvaise personne, ou si une tentative ou complicité est mal traitée ; moitié des points si une circonstance aggravante manque ou n'est pas matérialisée ; −0,5 si l'élément légal ou le libellé est incorrect ; −0,5 sur la rubrique par infraction en trop.

Note `"note": "x / 20"`. La forme (orthographe, syntaxe, clarté, termes juridiques plutôt que langage de terrain) peut retirer jusqu'à 3 points ; le signaler dans une section « Forme ».

## Procédure pénale (méthodologie PP 08/2026, lue en local : voir `/exercice`)
Note sur la somme des `points` du sujet (40 pour l'épreuve complète), ramenée sur 20 dans `"note": "x / 20"`. Une section par partie et par acte, avec `points` :
- **Q1** (par infraction) : 0 si elle est mal qualifiée (crime ou délit), relevée contre la mauvaise personne, ou si une tentative ou complicité est mal traitée ; moitié des points si une circonstance aggravante manque ou n'est pas matérialisée ; −0,5 si l'élément légal ou le libellé est incorrect ; −0,5 par infraction en trop.
- **Q2** : le cadre d'enquête, puis chaque PV, rubrique par rubrique, comparés au corrigé, au GPS et au TACL du bon cadre. Une erreur mineure retire au plus les points de la rubrique. Titre de section : « Cadre d'enquête » ou « Procès-verbal de … ».
- **Erreurs majeures** (liste de `_ancien/data/referentiel/erreurs_majeures.json`, à recouper avec la méthodologie). La première vaut 0 à l'acte et à tous les actes suivants, puis −10 sur la partie Q2, une seule fois. Une section dédiée avec « Erreur majeure » dans son titre. Un acte obligatoire omis est lui-même une erreur majeure.
- **Q3 / questions de cours** : points selon les éléments attendus. La structure « règle, puis en l'espèce » est valorisée.
- Forme : jusqu'à −3 points sur 20.

## Écrire et répondre
3. Écrire `data/corrections/<id>.json` au format de `CLAUDE.md` : `bilan`, `sections` (statut `ok` / `partiel` / `faux`, et `points` pour le CRT), 2 ou 3 `conseils` concrets. Valider le JSON.
4. Publier : `git add data/copies data/corrections && git commit -m "Correction : <titre>" && git push` (message terminé par la ligne `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`).
5. Dans la discussion, donner seulement le bilan, la note éventuelle et les deux erreurs principales, puis : « Actualise le site dans une à deux minutes pour voir la correction complète et le corrigé. »
