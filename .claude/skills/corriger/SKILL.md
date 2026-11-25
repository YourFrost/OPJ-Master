---
name: corriger
description: Corrige un exercice Infraction Finder terminé (DPG/DPS ou CRT), écrit la correction pour la plateforme et la résume dans la discussion. Utiliser quand l'utilisateur tape /corriger ou demande la correction de sa réponse.
argument-hint: "[id de l'exercice]"
---

Exercice : `$ARGUMENTS`. Si rien n'est indiqué, prendre la dernière copie de `data/copies/` qui a `rendue_le` et pas encore de fichier dans `data/corrections/`.

1. Lire `CLAUDE.md`, `data/sujets/<id>.json` (avec `corrige` et `pieges`) et `data/copies/<id>.json`. Si `rendue_le` est absent, demander à l'utilisateur d'envoyer d'abord sa réponse. **Ne jamais modifier le sujet ni la copie.**
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

## Écrire et répondre
3. Écrire `data/corrections/<id>.json` au format de `CLAUDE.md` : `bilan`, `sections` (statut `ok` / `partiel` / `faux`, et `points` pour le CRT), 2 ou 3 `conseils` concrets. Valider le JSON.
4. Dans la discussion, donner seulement le bilan, la note éventuelle et les deux erreurs principales, puis : « Actualise la page pour voir la correction complète et le corrigé. »
