---
name: typographie-francaise
description: "Règles de la typographie française (orthotypographie, Lexique des règles typographiques de l’Imprimerie nationale) pour écrire, corriger ou vérifier un texte en français. Espaces insécables et fines avant « ; : ! ? » et dans les guillemets « », apostrophe typographique ’, majuscules accentuées (État, À propos, Étienne), points de suspension …, tirets d’incise, abréviations (M., Mme, n°, 1er, 2e, XIXe siècle), nombres (1 000, 3,14), unités (12 km, 25 %, 10 €), heures, dates, sigles, ligatures (œuvre, cœur). Utilise ce skill dès qu’il faut rédiger ou relire du français destiné à être publié ou montré — page web, texte de site, fiche d’outil, interface d’application, bouton, message, mail soigné, présentation, document, légende, texte de référencement — et dès qu'on parle de « typo », d’espaces insécables, de guillemets français, de corriger ou relire un texte, même si le mot « typographie » n'est pas prononcé."
---

# Typographie française

Le but : un texte français qui suit les règles de l'Imprimerie nationale, sans rien abîmer
autour (code, adresses web, noms de fichiers, citations en langue étrangère). Ces règles
comptent parce qu'un lecteur français les remarque immédiatement quand elles manquent : un
« ? » orphelin en début de ligne, des guillemets droits ou un « Etat » sans accent font
amateur, surtout chez un designer.

Le détail de chaque règle, avec les exceptions, est dans `references/regles.md` : lis-le
dès que tu as un doute sur un cas particulier (nombres, abréviations, tirets, capitales).

## Trois usages

1. **Écrire** du français (une fiche, un bouton, un message, un mail) : applique les règles
   directement, sans les commenter.
2. **Corriger** un texte fourni : rends le texte corrigé, puis une courte liste des
   corrections par catégorie (pas une liste mot à mot si elles sont nombreuses). Ne touche
   ni au sens, ni au style, ni à l'orthographe, sauf faute évidente que tu signales.
3. **Vérifier des fichiers** (pages HTML, Markdown, textes) : utilise l'outil
   `scripts/typo_fr.py`, qui ne lit que le texte visible et laisse le code tranquille.

## L'essentiel des règles

| Règle | Juste | Faux |
|---|---|---|
| Avant `;` `!` `?` : espace fine insécable (U+202F) | `Vraiment ?` | `Vraiment?` / `Vraiment ?` avec espace normale |
| Avant `:` : espace insécable (U+00A0) | `Note : …` | `Note: …` |
| Guillemets français, espace insécable à l'intérieur | `« bonjour »` | `"bonjour"` / `«bonjour»` |
| Guillemets de second niveau | `« il dit “non” »` | `« il dit « non » »` |
| Apostrophe typographique | `l’atelier` | `l'atelier` |
| Majuscules accentuées | `État`, `À propos`, `Étienne` | `Etat`, `A propos`, `Etienne` |
| Points de suspension : un seul signe | `etc.` / `et puis…` | `...` / `etc...` |
| Ordinaux | `1er`, `1re`, `2e`, `XIXe siècle` | `1ère`, `2ème`, `2nd` (sauf « second ») |
| Abréviations | `M.`, `Mme`, `n°`, `p. 12` | `Mr`, `Mme.`, `N°12` |
| Milliers : espace fine insécable ; décimales : virgule | `12 500`, `3,14` | `12500`, `12.500`, `3.14` |
| Nombre et unité séparés par une espace insécable | `12 km`, `25 %`, `30 °C`, `10 €` | `12km`, `25%`, `€10` |
| Heures | `14 h 30` (texte) | `14h30`, `14H30` |
| Dates : jours et mois en minuscule | `mardi 17 novembre 2026` | `Mardi 17 Novembre` |
| Sigles sans points | `SNCF`, `ONU` | `S.N.C.F.` |
| Ligatures | `œuvre`, `cœur`, `Œdipe` | `oeuvre`, `coeur` |

Pas d'espace avant le point, la virgule, les points de suspension, ni à l'intérieur des
parenthèses et crochets ; une espace après.

## Ce qu'il ne faut jamais toucher

- Le **code** : balises HTML et leurs attributs techniques, JavaScript, CSS, noms de
  fichiers, variables, commandes.
- Les **adresses** (`https://…`, `mailto:`, chemins), les heures numériques `12:30`,
  les rapports `16:9`, les numéros de version, les références techniques.
- Les **textes dans une autre langue** : une citation anglaise garde la typographie
  anglaise (« I’m Too Young To Die » garde son apostrophe, pas d'espace avant le `!`).
- Les **noms propres et marques** tels qu'ils s'écrivent (`iPhone`, `MacPaint`).

En cas de doute sur un passage, signale-le plutôt que de le corriger.

## Sur le web et dans les interfaces

- Écris les caractères directement (`U+00A0` insécable, `U+202F` fine insécable,
  `’`, `«`, `»`, `…`) dans les fichiers en UTF-8 ; dans un HTML qui en a besoin,
  `&nbsp;` et `&#8239;` conviennent.
- **Vérifie que la police contient l'espace fine** (`U+202F`). Les polices bitmap
  anciennes (Chicago, Geneva de MacPain par exemple) ou certaines polices web ne l'ont
  pas : le caractère s'affiche alors en carré vide ou en espace énorme. Dans ce cas,
  utilise l'espace insécable ordinaire (`U+00A0`) partout, et dis-le.
- Dans une chaîne d'interface (bouton, menu), les règles s'appliquent aussi :
  `Enregistrer sous…`, `Niveau : facile`, `Vraiment quitter ?`.

## L'outil de vérification

`scripts/typo_fr.py` (Python 3, sans dépendance) lit des fichiers `.html`, `.htm`, `.md`,
`.txt`, ou du texte collé, et ne traite que le texte lisible (il saute balises, `<script>`,
`<style>`, `<code>`, `<pre>`, blocs de code Markdown, adresses).

```bash
python3 scripts/typo_fr.py verifier page.html          # liste les écarts, ligne par ligne
python3 scripts/typo_fr.py corriger texte.md -o sortie.md   # écrit une version corrigée
python3 scripts/typo_fr.py corriger page.html --sur-place   # corrige le fichier (copie .avant-typo gardée)
echo "Bonjour: voici l'outil..." | python3 scripts/typo_fr.py corriger -
```

Options : `--fine-absente` remplace l'espace fine par l'espace insécable ordinaire (pour
les polices qui n'ont pas l'espace fine).

L'outil ne corrige que les règles mécaniques et sûres. Il **signale sans corriger** ce qui
demande un jugement : guillemets droits ambigus, majuscules sans accent, nombres longs
(un numéro ou une année ne prend pas d'espace), tirets. Relis ces signalements toi-même et
décide au cas par cas ; ne présente jamais la sortie de l'outil comme une correction
complète.

Ne modifie un fichier du projet (site, application) que si on te l'a demandé ; sinon,
montre ce que tu changerais.
