---
name: exercice
description: Génère un exercice pour OPJ Master (DPG/DPS, CRT ou procédure pénale), avec son sujet et son corrigé caché. Utiliser quand l'utilisateur tape /exercice ou demande un nouvel exercice.
argument-hint: "unitaire | multiple <min>-<max> | crt | pp <complet|aleatoire|cours|pv: …>"
---

Arguments : `$ARGUMENTS`.
- `unitaire` : DPG/DPS, une infraction.
- `multiple 2-4` : DPG/DPS, un nombre d'infractions **tiré au hasard** dans la plage, jamais annoncé à l'utilisateur.
- `crt` : compte rendu téléphonique, **1 à 3 infractions** (nombre au hasard).
- `pp complet` : épreuve blanche de procédure pénale (Q1 + Q2 + Q3).
- `pp pv: Garde à vue (majeur), Perquisition` : sujet réduit aux éléments nécessaires pour rédiger le ou les PV choisis.
- `pp aleatoire` : un seul PV, de type tiré au hasard parmi les 25 du GPS.
- `pp cours` : 2 ou 3 questions de cours (Q3 seule).

Commun :
1. Lire `CLAUDE.md` (formats), puis lister `data/sujets/` pour ne pas répéter les mêmes infractions ou scénarios.
2. **Écrire le corrigé d'abord**, puis le sujet. **Vérifier sur Légifrance** tout article ou alinéa dont tu n'es pas certain.
3. Le sujet est un récit factuel (prénoms, âges, dates, heures, lieux, paroles entre guillemets). Chaque élément du corrigé y est clairement établi, et l'infraction n'est jamais nommée. Ajouter 1 ou 2 pièges réalistes, à noter dans `pieges`.
4. Écrire `data/sujets/<id>.json` (`"epreuve": "dps"`, `"crt"` ou `"pp"`), ajouter l'id **en tête** de `data/sujets/index.json`, puis valider les deux JSON (`python -c "import json;json.load(open(r'…',encoding='utf-8'))"`).
5. Publier : `git add data/sujets && git commit -m "Exercice : <titre>" && git push` (message terminé par la ligne `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`).
6. Répondre en une ligne, **sans rien révéler du corrigé** : le titre et « Actualise https://yourfrost.github.io/OPJ-Master/ dans une à deux minutes pour commencer ».

## DPG / DPS
Corrigé, pour chaque infraction :
- mis en cause, libellé, **qualification (crime ou délit)** ;
- élément légal : articles de définition et de répression, avec les circonstances aggravantes et la tentative ou la complicité éventuelles ;
- éléments matériels, chacun justifié par un fait du sujet ;
- élément moral (intentionnel ou non), justifié par le sujet.

En mode multiple, prévoir plusieurs auteurs ou plusieurs faits.

## CRT (méthodologie CRT 2026)
- **Sujet** : sur le modèle des sujets d'examen. L'OPJ « Mdl/Chef Alpha » exerce à la CoB de Mont, groupement et TJ de Dalis. Le récit présente la saisine (appel du CORG, plainte…), le transport et les premières constatations, quelques actes déjà faits (auditions, vidéoprotection, saisie, GAV éventuelle), et s'arrête au moment de l'appel au procureur, avec la date et l'heure. Il se termine par :
  - « Travail demandé : à ce stade de l'enquête, rédigez le compte rendu téléphonique initial adressé au procureur de la République de Dalis par le Mdl/Chef Alpha le (date) à (heure). Vous exposerez l'ensemble de vos investigations, retraçant la synthèse des actes qui ont été réalisés et de ceux qui restent à effectuer, complétée par la qualification de l'infraction ou des infractions susceptibles d'être retenues à l'encontre de la ou des personnes impliquées. »
  - une liste « Identités » : nom, date et lieu de naissance, situation, profession et adresse de chaque protagoniste.
- **Corrigé**, en 5 blocs :
  1. **Présentation (0,5 pt)** : « Bonjour Monsieur/Madame le procureur de la République, Mdl/Chef Alpha, OPJ, affecté à la CoB de Mont. »
  2. **Objet (3 pts)** : le motif de l'appel, le libellé complet des infractions et le **cadre juridique** (flagrance si les faits ont moins de 24 h, préliminaire au-delà, ou cadre particulier : découverte de cadavre, disparition inquiétante…).
  3. **Faits (4,5 pts)** : synthèse reformulée, sans recopier le sujet. Quoi, où, quand ; la victime (identité, âge, ITT, plainte) ; l'auteur (identité, interpellé ou non, GAV et heure de notification) ; comment et pourquoi ; un éventuel retentissement médiatique.
  4. **Actes d'enquête (8 pts)** : d'abord les **actes réalisés** (`actes_realises`), puis les **actes à réaliser** (`actes_a_realiser`). Chacun est nommé comme un procès-verbal (« Procès-verbal de … ») et motivé en une phrase tirée du sujet. L'OPJ doit être force de proposition (réquisitions, auditions, perquisitions, GAV, fichiers, vidéoprotection…).
  5. **Qualification (4 pts)** : une phrase par mis en cause et par infraction, avec le libellé (et les circonstances aggravantes détaillées), **délit ou crime**, « prévu et réprimé par les articles … du Code pénal », alinéas compris.
- Durée indicative : 1 heure.

## Procédure pénale (méthodologie PP 08/2026)
**Sources, lues en local et jamais publiées** (diffusion restreinte) : `C:\Users\User\Desktop\Révision OPJ\Documents\Méthologie\Méthodologie PP - 08_2026.pdf`, `Documents\GPS+.pdf`, `Documents\TACL 09_2026.pdf`, `Documents\Liste erreurs majeures et mineures.pdf`, et leurs transcriptions dans `_ancien/data/referentiel/` (`gps.json`, `tacl.json`, `erreurs_majeures.json`, `circonscriptions.json`). Le corrigé publié ne contient que ce qu'une bonne copie écrirait (articles, mentions des PV). On ne recopie jamais les « À savoir » du GPS ni des pages de méthodologie.

**Format du sujet** (en plus des champs communs) :
```json
"type": "complet", "duree_minutes": 240, "points": { "q1": 4, "q2": 26, "q3": 10 },
"questions": {
  "q1": { "consigne": "Indiquez la qualification légale… à l'encontre de X.", "mis_en_cause": ["X"] },
  "q2": { "consigne": "Présentez de façon chronologique…", "pv_a_rediger": ["…"], "pv_a_ne_pas_rediger": ["…"] },
  "q3": [ { "n": 1, "points": 5, "enonce": "…" } ]
},
"corrige": {
  "q1": [ { "mis_en_cause": "X", "texte": "Libellé…, délit prévu et réprimé par les articles…" } ],
  "q2": [ { "type": "cadre", "points": 2, "cadre_juridique": "fd", "cadre_legal": "…", "justification": "…", "competence": "…" },
          { "type": "pv", "acte": "gav_majeur", "points": 6, "intitule": "…", "date_heure_lieu": "…", "enqueteurs": "…", "cadre_legal": "…",
            "motivation": "…", "notification_droits": "…", "deroulement": "…", "duree": "…", "elements_de_fond": "…", "nota": "…" } ],
  "q3": [ { "reponse": "Règle… En l'espèce…" } ]
}
```
- `type` : `complet`, `pv`, `aleatoire` ou `cours`. Ne mettre dans `questions` que les parties demandées.
- `cadre_juridique` : `ep`, `fd`, `cr`, `dc`, `dpgb`, `di` ou `rpf`.
- `acte` : un id du GPS (`tcmp`, `perquisition`, `saisie`, `saisie_incidente`, `bris_scelle`, `audition_victime`, `audition_representant_legal`, `audition_temoin`, `audition_anonymat`, `audition_libre`, `retenue_judiciaire`, `gav_mineur`, `gav_majeur`, `investigations`, `interpellation`, `assistance_autopsie`, `req_prestataire`, `req_personne_qualifiee`, `req_remise_informations`, `req_autorite_militaire`, `req_geolocalisation`, `req_sonorisation`, `req_interception`, `transcription`, `mandats`).
- Les rubriques d'un PV suivent la méthodologie : `motivation` ou `saisine` (TCMP, mandats) ; `notification_droits` pour les auditions de victime, de représentant légal, l'audition libre, la GAV, la retenue et les mandats ; `deroulement` pour l'audition libre, la GAV, la retenue et les mandats ; `duree` pour la GAV et la retenue.

**Selon le format** :
- `complet` : 3 à 4 pages, 1 à 2 cadres, 10 à 15 actes. Q1 sur 4 points, Q2 sur 26 répartis entre le cadre et les actes, Q3 sur 10 avec 2 questions. `duree_minutes` : 240. Ajouter une liste `pv_a_ne_pas_rediger`, comme dans les sujets 2026.
- `pv` : un récit court (saisine, cadre, faits utiles) qui permet de rédiger **le cadre d'enquête et les PV demandés, et rien d'autre**. Lister ces PV dans `pv_a_rediger` et omettre Q1 et Q3. Q2 sur 26, répartis entre le cadre et les PV. `duree_minutes` : 20 par PV, plus 10.
- `aleatoire` : comme `pv`, avec un seul PV tiré au hasard. `duree_minutes` : 30.
- `cours` : `questions.q3` seule, avec 2 ou 3 questions sur les fiches de procédure pénale du programme (CPP, CJPM, libertés publiques). Chaque réponse modèle part de la règle (articles **vérifiés sur Légifrance**), puis l'applique : « En l'espèce… ». Q3 sur 10, `duree_minutes` : 30. Le préciser à l'utilisateur : ces questions s'appuient sur le CPP et le GPS, pas sur les fiches de cours elles-mêmes.

**Rédaction du récit**, à la manière des sujets officiels :
- « Mdl/Chef Alpha, OPJ à la CoB de Mont, groupement et TJ de Dalis » et un APJ, « gendarme Lima » ;
- des horaires précis, des déclarations entre guillemets, éventuellement un acte dans un autre ressort (extension de compétence, voir `circonscriptions.json`) ;
- le sujet ne donne **pas** les réflexes procéduraux (informations et autorisations des magistrats, droits, assentiments, serments…), sauf ce que le candidat ne peut pas deviner : numéro d'ordonnance, heure de prolongation ou de fin de mesure, retenue au titre de l'art. 56, al. 11, autorisation au titre de l'art. 78.
