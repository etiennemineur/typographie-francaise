# Règles détaillées

D'après le *Lexique des règles typographiques en usage à l'Imprimerie nationale*, avec les
usages courants de l'édition française. Quand deux usages coexistent, le premier cité est
celui à appliquer par défaut.

## Sommaire

1. Espaces et ponctuation
2. Guillemets
3. Apostrophe
4. Points de suspension
5. Tirets et traits d'union
6. Majuscules et accents
7. Abréviations
8. Nombres, unités, heures, dates
9. Sigles et acronymes
10. Italique
11. Ligatures et caractères spéciaux
12. Cas particuliers du web et des interfaces

## 1. Espaces et ponctuation

| Signe | Avant | Après |
|---|---|---|
| `.` `,` `…` | rien | espace |
| `;` `!` `?` | espace fine insécable (U+202F) | espace |
| `:` | espace insécable (U+00A0) | espace |
| `«` | espace | espace insécable |
| `»` | espace insécable | espace (ou ponctuation) |
| `(` `[` | espace | rien |
| `)` `]` | rien | espace (ou ponctuation) |
| `—` `–` d'incise | espace insécable avant le tiret d'ouverture, espace après ; l'inverse à la fermeture | |

- `?!` ou `!?` : une seule espace fine avant le groupe, aucune entre les signes.
- Pas d'espace avant `:` dans une heure (`12:30`), un rapport (`16:9`), une adresse
  (`https://`), un horodatage, un raccourci (`Cmd:K`) ni dans du code.
- Espace fine insécable aussi avant `%` dans certains usages ; l'Imprimerie nationale
  demande l'espace insécable ordinaire : `25 %`.
- Pas de double espace.

## 2. Guillemets

- Premier niveau : `« … »` avec espaces insécables intérieures.
- Second niveau (citation dans la citation) : `“ … ”` sans espace, ou à défaut à nouveau
  `« … »`.
- Ponctuation finale : à l'intérieur si elle appartient à la citation complète, à
  l'extérieur sinon. `Il a dit : « Je viens. »` mais `Il parle d'un « petit » projet.`
- Une citation en langue étrangère insérée dans un texte français prend les guillemets
  français ; son contenu garde sa propre typographie.

## 3. Apostrophe

- `’` (U+2019) dans tout le texte courant, y compris les mots étrangers (`I’m`).
- `'` droite seulement dans le code, les noms de fichiers et les adresses.
- Élision devant une majuscule : `l’État`, `d’Étienne`.

## 4. Points de suspension

- Un seul caractère `…` (U+2026), jamais trois points.
- Collés au mot qui précède, espace après.
- Jamais après `etc.` (`etc.` suffit).
- Coupure dans une citation : `[…]`.
- Dans une interface, une commande qui ouvre une fenêtre de dialogue se termine par `…` :
  `Enregistrer sous…`, `Imprimer…`.

## 5. Tirets et traits d'union

- Trait d'union `-` : mots composés (`peut-être`, `Saint-Denis`), coupures, intervalles
  simples de dates (`1914-1918`).
- Tiret demi-cadratin `–` (U+2013) : incises (`le projet – enfin terminé – part demain`),
  énumérations, intervalles dans les tableaux.
- Tiret cadratin `—` (U+2014) : dialogues, et incises dans une composition soignée
  (choix de maison : rester cohérent dans tout le texte).
- Le signe moins des nombres est `−` (U+2212) dans un texte soigné.

## 6. Majuscules et accents

- Les capitales prennent leurs accents, cédilles et trémas : `État`, `À`, `Ça`, `Œ`,
  `ÉCOLE`, `Île-de-France`, `Étienne`. C'est la règle de l'Académie française et de
  l'Imprimerie nationale ; l'absence d'accent est une faute, pas une simplification.
- Minuscule : jours, mois, langues, adjectifs de nationalité (`le français`, `un
  artiste français`), points cardinaux employés comme direction.
- Majuscule : peuples (`les Français`), institutions uniques (`l’État`, `l’Assemblée
  nationale`), premier mot d'un titre d'œuvre (`À la recherche du temps perdu`).
- Titres et boutons d'interface : majuscule au premier mot seulement
  (`Ouvrir l’outil`, pas `Ouvrir L’Outil`).

## 7. Abréviations

| Mot | Abréviation |
|---|---|
| Monsieur, Messieurs | `M.`, `MM.` |
| Madame, Mesdames | `Mme`, `Mmes` |
| Mademoiselle | `Mlle` |
| Docteur, Professeur, Maître | `Dr`, `Pr`, `Me` |
| numéro(s) | `n°`, `nos` |
| premier, première | `1er`, `1re` |
| deuxième, troisième… | `2e`, `3e` (lettres en exposant si possible) |
| second(e) | `2d`, `2de` |
| siècle | `XIXe siècle` (chiffres romains en petites capitales si possible) |
| page, pages | `p.` |
| et cetera | `etc.` |
| confer | `cf.` |
| environ | `env.` |

- On abrège `Monsieur` seulement devant un nom (`M. Dupont`), jamais seul.
- L'abréviation qui se termine par la dernière lettre du mot ne prend pas de point
  (`Mme`, `Dr`, `Me`).
- Sur le web, les exposants : `1<sup>er</sup>`, `XIX<sup>e</sup>` quand c'est possible ;
  sinon `1er`, `XIXe` sur la ligne.

## 8. Nombres, unités, heures, dates

- Milliers : espace fine insécable à partir de 5 chiffres (`12 500`, `1 000 000`) ;
  à 4 chiffres, facultative (`1 000` ou `1000`, rester cohérent).
- Jamais d'espace dans : années (`2026`), numéros de page, codes postaux, numéros de
  téléphone (qui ont leur propre groupement : `01 23 45 67 89`), références, numéros de
  version.
- Décimales : virgule (`3,14`, `0,5 %`).
- Nombre + unité : espace insécable (`12 km`, `3 Mo`, `25 %`, `30 °C`, `90°` pour un
  angle sans espace, `10 €`, `1 200 px` en typographie soignée).
- Monnaie après le nombre : `10 €`, `25,50 €`, `100 $`.
- Heures dans un texte : `14 h`, `14 h 30`, `14 h 30 min 12 s` ; `14:30` seulement dans
  un contexte numérique (affichage, horaires techniques).
- Dates : `mardi 17 novembre 2026`, `le 1er décembre`, `du 3 au 5 mai`,
  `en 2026-2027`.
- En toutes lettres : nombres en début de phrase, petits nombres dans un texte
  littéraire (`trois outils`), âges et durées dans un récit.

## 9. Sigles et acronymes

- Sans points ni espaces : `SNCF`, `ONU`, `UNESCO` ou `Unesco` (acronyme lexicalisé qu'on
  prononce comme un mot : majuscule initiale seule).
- Pas de `s` au pluriel : `des PME`.
- La première occurrence peut être développée : `Imprimerie nationale (IN)`.

## 10. Italique

- Titres d'œuvres, de journaux, de logiciels quand on les cite comme œuvres
  (*MacPaint*) — sur le web, `<em>` ou `<i>`.
- Mots étrangers non intégrés (*design thinking* en contexte français), locutions
  latines non francisées (*sic*).
- La ponctuation qui suit un mot en italique reste en romain.

## 11. Ligatures et caractères spéciaux

- `œ`, `Œ` : `œuvre`, `cœur`, `sœur`, `œil`, `Œdipe`, `manœuvre`.
- `æ`, `Æ` : `curriculum vitæ`, `ex æquo`.
- Pas de ligature dans `moelle`, `coefficient`, `coexister` (les lettres se prononcent
  séparément).
- `×` pour une multiplication ou une dimension (`1024 × 768`), pas la lettre `x`.
- `°` pour les degrés, `№` déconseillé (préférer `n°`).

## 12. Cas particuliers du web et des interfaces

- Caractères à utiliser : espace insécable `U+00A0` (`&nbsp;`), espace fine insécable
  `U+202F` (`&#8239;`), apostrophe `U+2019`, guillemets `U+00AB` `U+00BB`, points de
  suspension `U+2026`, tirets `U+2013` `U+2014`.
- L'espace fine insécable `U+202F` n'existe pas dans toutes les polices (polices bitmap
  rétro, certaines polices web anciennes). Vérifier le rendu ; à défaut, utiliser
  `U+00A0` partout.
- Ne jamais mettre d'espace insécable dans un attribut technique (`href`, `src`, `id`,
  `class`, `data-*`). Les attributs lus par les personnes (`alt`, `title`, `aria-label`,
  `content` des balises `meta` de description) suivent les règles.
- Textes de référencement (`<title>`, `meta description`, Open Graph) : mêmes règles ;
  les moteurs de recherche gèrent bien les espaces insécables et les guillemets français.
- Libellés d'interface : majuscule au premier mot seulement, `…` pour une commande qui
  ouvre une fenêtre, pas de point final sur un bouton.
