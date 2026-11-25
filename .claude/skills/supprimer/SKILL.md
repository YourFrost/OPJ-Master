---
name: supprimer
description: Supprime définitivement un exercice d'OPJ Master du site (sujet, copie, correction). Utiliser quand l'utilisateur tape /supprimer <id>.
argument-hint: "<id de l'exercice>"
---

Exercice : `$ARGUMENTS`.

1. Vérifier que `data/sujets/<id>.json` existe. Sinon, le dire et s'arrêter.
2. Retirer l'id de `data/sujets/index.json`, puis valider le JSON.
3. `git rm` les fichiers existants parmi `data/sujets/<id>.json`, `data/copies/<id>.json` et `data/corrections/<id>.json`.
4. `git add data/sujets/index.json && git commit -m "Suppression : <id>" && git push` (message terminé par la ligne `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`).
5. Répondre en une ligne : l'exercice est supprimé, et le site sera à jour d'ici une à deux minutes.
