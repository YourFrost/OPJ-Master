---
name: exercice
description: Génère un exercice pour Infraction Finder (DPG/DPS ou CRT), avec son sujet et son corrigé caché. Utiliser quand l'utilisateur tape /exercice ou demande un nouvel exercice.
argument-hint: "unitaire | multiple <min>-<max> | crt [précisions libres]"
---

Arguments : `$ARGUMENTS`.
- `unitaire` : DPG/DPS, une infraction.
- `multiple 2-4` : DPG/DPS, un nombre d'infractions **tiré au hasard** dans la plage, jamais annoncé à l'utilisateur.
- `crt` : compte rendu téléphonique, **1 à 3 infractions** (nombre au hasard).

Commun :
1. Lire `CLAUDE.md` (formats), puis lister `data/sujets/` pour ne pas répéter les mêmes infractions ou scénarios.
2. **Écrire le corrigé d'abord**, puis le sujet. **Vérifier sur Légifrance** tout article ou alinéa dont tu n'es pas certain.
3. Le sujet est un récit factuel (prénoms, âges, dates, heures, lieux, paroles entre guillemets). Chaque élément du corrigé y est clairement établi, et l'infraction n'est jamais nommée. Ajouter 1 ou 2 pièges réalistes, à noter dans `pieges`.
4. Écrire `data/sujets/<id>.json` (`"epreuve": "dps"` ou `"crt"`), puis valider le JSON (`python -c "import json;json.load(open(r'…',encoding='utf-8'))"`).
5. Répondre en une ligne, **sans rien révéler du corrigé** : le titre et « Actualise la page http://127.0.0.1:8765 pour commencer ».

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
