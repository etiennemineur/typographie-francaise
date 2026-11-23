#!/usr/bin/env python3
"""Vérifie et corrige la typographie française d'un texte, d'une page HTML ou d'un Markdown.

Ne traite que le texte lisible : les balises, <script>, <style>, <code>, <pre>, les blocs
de code Markdown, les adresses, les entités HTML et les heures numériques sont laissés tels
quels. Corrige seulement les règles mécaniques et sûres ; signale le reste.

  python3 typo_fr.py verifier FICHIER...
  python3 typo_fr.py corriger FICHIER -o SORTIE
  python3 typo_fr.py corriger FICHIER --sur-place      (garde FICHIER.avant-typo)
  echo "texte" | python3 typo_fr.py corriger -

Options :
  --fine-absente        espace insécable ordinaire au lieu de l'espace fine (police sans U+202F)
  --sauf "a,b"          expressions à ne jamais toucher (ex. titres anglais : "Nightmare!")
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

NBSP, NNBSP = "\u00a0", "\u202f"
SP = "[ \u00a0\u202f]"
L = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"

# ------------------------------------------------------------------ découpage
HTML_SKIP = re.compile(r"(?is)<!--.*?-->|<(script|style|pre|code|textarea)\b.*?</\1\s*>|<[^>]*>")
MD_SKIP = re.compile(r"(?ms)^(```|~~~).*?^\1[^\n]*$|`[^`\n]*`|\]\([^)\n]*\)|<[^>\n]*>")
PROTECT_BASE = (
    r"(?:https?|ftp|mailto|file):[^\s<>\"')\]]+"     # adresses
    r"|www\.[^\s<>\"')\]]+"
    r"|[\w.+-]+@[\w-]+\.[\w.-]+"                      # e-mails
    r"|&(?:[a-zA-Z]+|#\d+|#x[0-9a-fA-F]+);"           # entités HTML
    r"|\b\d{1,2}:\d{2}(?::\d{2})?\b"                  # heures numériques 12:30
    r"|\b\d+:\d+\b"                                   # rapports 16:9
    r"|(?:\.{0,2}/)?(?:[\w.-]+/)+[\w.-]*"             # chemins
    r"|\b[\w-]+\.(?:html?|css|js|py|md|txt|png|jpe?g|gif|svg|pdf|zip|dmg|woff2?|json)\b"   # fichiers
)


def chunks(text, kind, protect):
    """Coupe le texte en morceaux (lisible ?, morceau)."""
    skip = HTML_SKIP if kind == "html" else MD_SKIP if kind == "md" else None
    parts, pos = [], 0
    if skip:
        for m in skip.finditer(text):
            if m.start() > pos:
                parts.append((True, text[pos:m.start()]))
            parts.append((False, m.group(0)))
            pos = m.end()
    parts.append((True, text[pos:]))
    out = []
    for prose, s in parts:
        if not prose:
            out.append((False, s)); continue
        p = 0
        for m in protect.finditer(s):
            if m.start() > p:
                out.append((True, s[p:m.start()]))
            out.append((False, m.group(0)))
            p = m.end()
        out.append((True, s[p:]))
    return [c for c in out if c[1]]


# ------------------------------------------------------------------ règles
ACCENTS = {"Etat": "État", "Etats": "États", "Etienne": "Étienne", "Ecole": "École", "Ecoles": "Écoles",
           "Equipe": "Équipe", "Edition": "Édition", "Editions": "Éditions", "Etude": "Étude",
           "Etudes": "Études", "Evenement": "Événement", "Elysee": "Élysée", "Eglise": "Église",
           "Electricite": "Électricité", "Economie": "Économie", "Ecran": "Écran", "Ecrans": "Écrans"}
LIGATURES = {"oeuvre": "œuvre", "oeuvres": "œuvres", "coeur": "cœur", "coeurs": "cœurs", "soeur": "sœur",
             "soeurs": "sœurs", "oeil": "œil", "voeu": "vœu", "voeux": "vœux", "manoeuvre": "manœuvre",
             "noeud": "nœud", "boeuf": "bœuf", "oeuf": "œuf", "oeufs": "œufs", "choeur": "chœur"}
UNITS = r"km|cm|mm|m|kg|mg|g|Ko|Mo|Go|To|ko|px|pt|°C|ms|min|€|\$|%|L|ml|cl"


def case_like(src, dst):
    return dst[0].upper() + dst[1:] if src[0].isupper() else dst


def rules(fine):
    T = fine
    R = []   # (nom, motif, remplacement ou None, explication)
    R.append(("apostrophe", re.compile(rf"(?<=[{L}])'(?=[{L}])"), "’", "apostrophe typographique ’"))
    R.append(("suspension", re.compile(r"(?i)\betc\.?\s*(?:\.{2,}|…)"), "etc.", "« etc. » sans points de suspension"))
    R.append(("suspension", re.compile(r"\.{3}"), "…", "points de suspension en un seul signe …"))
    R.append(("espace-avant", re.compile(rf"(?<=[^\s!?;:\u00a0\u202f(\[«]){SP}?([!?;]+)"), lambda m: T + m.group(1),
              "espace fine insécable avant ; ! ?"))
    R.append(("espace-avant", re.compile(rf"(?<=[^\s:\u00a0\u202f(\[«]){SP}?:(?=\s|$|»)"), NBSP + ":",
              "espace insécable avant :"))
    R.append(("guillemets", re.compile(rf"«{SP}*"), "«" + NBSP, "espace insécable après «"))
    R.append(("guillemets", re.compile(rf"{SP}*»"), NBSP + "»", "espace insécable avant »"))
    R.append(("ordinal", re.compile(r"\b1(?:ère|ere|iere|ière)\b"), "1re", "1re et non 1ère"))
    R.append(("ordinal", re.compile(r"\b(\d+)(?:ème|eme|ième|ieme)s?\b"), lambda m: m.group(1) + "e", "2e et non 2ème"))
    R.append(("unite", re.compile(rf"(\d)(?:[ \u202f])?({UNITS})(?![{L}\d])"), lambda m: m.group(1) + NBSP + m.group(2),
              "espace insécable entre nombre et unité"))
    R.append(("heure", re.compile(r"\b(\d{1,2}) ?[hH] ?(\d{2})\b"), lambda m: m.group(1) + NBSP + "h" + NBSP + m.group(2),
              "heure en texte : 14 h 30"))
    R.append(("heure", re.compile(rf"\b(\d{{1,2}})[hH](?![{L}\d])"), lambda m: m.group(1) + NBSP + "h", "heure en texte : 14 h"))
    R.append(("dimension", re.compile(r"\b(\d{2,}) ?[xX] ?(\d{2,})\b"), lambda m: m.group(1) + " × " + m.group(2),
              "signe × pour une dimension"))
    R.append(("ligature", re.compile(r"\b(" + "|".join(LIGATURES) + r")\b", re.I),
              lambda m: case_like(m.group(1), LIGATURES[m.group(1).lower()]), "ligature œ"))
    R.append(("accent", re.compile(r"\b(" + "|".join(ACCENTS) + r")\b"), lambda m: ACCENTS[m.group(1)],
              "majuscule accentuée"))
    R.append(("accent", re.compile(r"(?:^|(?<=[.!?…]\s)|(?<=[.!?…]\u00a0))A(?= [a-zàâçéèêëîïôûùüÿœ])"), "À",
              "« À » en début de phrase"))
    # signalements seulement (demandent un jugement)
    R.append(("guillemets-droits", re.compile(r"\"[^\"\n]{1,200}\""), None, "guillemets droits : « … » en français, “ … ” en anglais"))
    R.append(("accent?", re.compile(r"\b(?:A propos|Ca |Ile |Etre |Eviter|Ecrire|Eteindre|Echap)"), None, "majuscule à accentuer ?"))
    R.append(("milliers?", re.compile(r"(?<![\d.,/#-])\d{5,}(?![\d.,/-])"), None, "nombre long : espace fine tous les 3 chiffres (sauf numéro, code)"))
    R.append(("decimale?", re.compile(r"(?<![\d.])\d+\.\d+(?![\d.])"), None, "décimale : virgule en français (sauf version, code)"))
    R.append(("espace-avant-point", re.compile(r"(?<=\S) +[.,](?=\s|$)"), None, "pas d'espace avant . ou ,"))
    R.append(("abreviation", re.compile(r"\b(?:Mr|Mrs|Mme\.|Mlle\.|N°|No\.) ?(?=[A-Z0-9])"), None, "abréviation : M., Mme, n°"))
    R.append(("tiret?", re.compile(r"(?<=[^\s\-] )-(?= )"), None, "incise : tiret – ou —, pas un trait d'union"))
    return R


# ------------------------------------------------------------------ traitement
def kind_of(path):
    ext = Path(path).suffix.lower()
    return "html" if ext in (".html", ".htm", ".xhtml", ".svg") else "md" if ext in (".md", ".markdown") else "txt"


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def check(text, kind, R, protect, fine):
    found, offset = [], 0
    for prose, s in chunks(text, kind, protect):
        if prose:
            for name, rx, repl, why in R:
                for m in rx.finditer(s):
                    new = None if repl is None else (repl(m) if callable(repl) else repl)
                    if new is not None and new == m.group(0):
                        continue                                  # déjà juste
                    a = offset + m.start()
                    lo = max(0, m.start() - 25); hi = min(len(s), m.end() + 25)
                    found.append((line_of(text, a), name, s[lo:hi].replace("\n", " "), new, why))
        offset += len(s)
    return sorted(found, key=lambda f: f[0])


def fix(text, kind, R, protect, sans_fine):
    out, counts = [], {}
    for prose, s in chunks(text, kind, protect):
        if prose:
            for name, rx, repl, why in R:
                if repl is None:
                    continue
                new, n = rx.subn(repl, s)
                if new != s:
                    counts[why] = counts.get(why, 0) + n
                s = new
            if sans_fine:
                s = s.replace(NNBSP, NBSP)            # police sans espace fine
        out.append(s)
    return "".join(out), counts


def show(ch):
    return ch.replace(NBSP, "⍽").replace(NNBSP, "·")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["verifier", "corriger"])
    ap.add_argument("fichiers", nargs="+", help="fichiers, ou - pour lire le texte collé")
    ap.add_argument("-o", "--sortie")
    ap.add_argument("--sur-place", action="store_true")
    ap.add_argument("--fine-absente", action="store_true")
    ap.add_argument("--sauf", default="")
    ap.add_argument("--type", choices=["html", "md", "txt"])
    a = ap.parse_args()
    fine = NBSP if a.fine_absente else NNBSP
    extra = [re.escape(x.strip()) for x in a.sauf.split(",") if x.strip()]
    protect = re.compile((("|".join(extra) + "|") if extra else "") + PROTECT_BASE)
    R = rules(fine)
    total = 0
    for f in a.fichiers:
        text = sys.stdin.read() if f == "-" else Path(f).read_text(encoding="utf-8")
        kind = a.type or ("txt" if f == "-" else kind_of(f))
        if a.action == "verifier":
            found = check(text, kind, R, protect, fine)
            total += len(found)
            print(f"== {f} : {len(found)} point(s)")
            for line, name, ctx, new, why in found:
                tag = "corrigible" if new is not None else "à vérifier"
                print(f"  ligne {line:>4}  [{tag}] {why}\n             …{show(ctx)}…")
        else:
            new, counts = fix(text, kind, R, protect, a.fine_absente)
            if a.sur_place and f != "-":
                shutil.copy2(f, f + ".avant-typo")
                Path(f).write_text(new, encoding="utf-8")
                dest = f
            elif a.sortie:
                Path(a.sortie).write_text(new, encoding="utf-8"); dest = a.sortie
            else:
                sys.stdout.write(new); dest = "(sortie)"
            rest = [x for x in check(new, kind, R, protect, fine) if x[3] is None]
            msg = [f"== {f} → {dest}"] + [f"  {n} × {why}" for why, n in counts.items()]
            if rest:
                msg.append(f"  {len(rest)} point(s) à vérifier à la main :")
                msg += [f"    ligne {l} : {why} — …{show(c)}…" for l, _, c, _, why in rest]
            print("\n".join(msg), file=sys.stderr)
    if a.action == "verifier":
        print(f"\nTotal : {total} point(s). (⍽ = espace insécable, · = espace fine insécable)")


if __name__ == "__main__":
    main()
