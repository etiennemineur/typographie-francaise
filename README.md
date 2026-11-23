# Typographie française

Un *skill* pour Claude (Claude Code, Claude Desktop, Claude.ai) qui écrit, corrige et vérifie
les textes en français selon les règles de la typographie française, d’après le *Lexique des
règles typographiques en usage à l’Imprimerie nationale*.

Une fois installé, Claude l’utilise de lui-même dès qu’il rédige ou relit du français destiné à
être publié : page web, fiche, interface d’application, bouton, mail, présentation. On peut aussi
l’appeler directement avec `/typographie-francaise`.

Conçu par Étienne Mineur, designer, pour ses propres sites et applications.

## Ce qu’il fait

- **Espaces** : espace fine insécable avant `;` `!` `?`, espace insécable avant `:` et dans
  les guillemets `« … »`, entre un nombre et son unité (`12 km`, `25 %`, `10 €`).
- **Signes** : guillemets français, apostrophe typographique `’`, points de suspension `…`,
  tirets d’incise, signe `×` des dimensions, ligatures `œ` et `æ`.
- **Majuscules accentuées** : `État`, `À propos`, `École`.
- **Abréviations et nombres** : `M.`, `Mme`, `n°`, `1er`, `1re`, `2e`, `XIXe siècle`,
  `12 500`, `3,14`, `14 h 30`, dates en minuscules.
- **Sans rien casser** : le code, les adresses web, les noms de fichiers, les heures
  numériques (`12:30`), les formats (`16:9`) et les citations dans une autre langue restent
  intacts.
- **Polices rétro** : il rappelle de vérifier que la police contient l’espace fine (les polices
  bitmap des années 1980 ne l’ont pas) et sait la remplacer par l’espace insécable ordinaire.

## Contenu

| Fichier | Rôle |
|---|---|
| `SKILL.md` | la fiche que Claude lit : l’essentiel des règles et la façon de travailler |
| `references/regles.md` | les règles détaillées, avec les exceptions, en douze chapitres |
| `scripts/typo_fr.py` | un outil en ligne de commande qui vérifie ou corrige des fichiers |
| `exemples/` | un texte avant et après correction par l’outil, et le rapport produit |

## Installation

Copier le dossier dans les skills personnels de Claude Code :

```bash
git clone https://github.com/etiennemineur/typographie-francaise.git ~/.claude/skills/typographie-francaise
```

Pour un seul projet, le placer plutôt dans `.claude/skills/typographie-francaise/` à la racine
du projet. Sur Claude.ai, compresser le dossier en `.zip` et l’ajouter dans les réglages,
rubrique des skills.

## L’outil en ligne de commande

Python 3, sans dépendance. Il ne lit que le texte visible : balises HTML, `<script>`,
`<style>`, `<code>`, `<pre>`, blocs de code Markdown et adresses sont ignorés.

```bash
python3 scripts/typo_fr.py verifier page.html                # liste les écarts, ligne par ligne
python3 scripts/typo_fr.py corriger texte.md -o corrige.md    # écrit une version corrigée
python3 scripts/typo_fr.py corriger page.html --sur-place     # corrige le fichier (garde une copie .avant-typo)
echo "Bonjour: voici l'outil..." | python3 scripts/typo_fr.py corriger -
```

Options :

- `--fine-absente` : espace insécable ordinaire au lieu de l’espace fine, pour les polices qui
  n’ont pas ce caractère ;
- `--sauf "Nightmare!,I'm Too Young To Die"` : expressions à ne jamais toucher, par exemple des
  titres en anglais.

L’outil corrige seulement les règles mécaniques et sûres. Il signale sans les corriger les cas
qui demandent un jugement : guillemets droits, tirets, nombres longs (une année ou un numéro ne
prennent pas d’espace), décimales qui peuvent être des numéros de version.

## Limites

- Les règles automatiques ne savent pas reconnaître une phrase écrite dans une autre langue :
  utiliser `--sauf` pour la protéger, ou relire les signalements.
- Les attributs HTML lus par les personnes (`alt`, `title`) ne sont pas traités par l’outil ;
  Claude les corrige à la main quand il applique le skill.

## Licence

MIT, voir [LICENSE](LICENSE).

---

*English summary: a Claude skill that writes, fixes and checks French text according to French
typography rules (Imprimerie nationale): non-breaking and thin spaces before `; : ! ?` and inside
`« »`, typographic apostrophe, accented capitals, ellipsis, abbreviations, numbers and units. It
ships with a dependency-free Python checker that only touches visible text and leaves code,
URLs and other languages alone. MIT licence.*
