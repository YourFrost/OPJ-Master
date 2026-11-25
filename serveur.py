"""Serveur local d'Infraction Finder : python serveur.py  ->  http://127.0.0.1:8765"""
import json
import re
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

RACINE = Path(__file__).resolve().parent
DATA = RACINE / "data"
SUJETS, COPIES, CORRECTIONS = DATA / "sujets", DATA / "copies", DATA / "corrections"
ID = re.compile(r"^[a-z0-9-]{1,80}$")


def lire(f):
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None


def public(sujet):
    """Le sujet avec son statut ; le corrigé n'est joint qu'une fois la correction écrite."""
    copie = lire(COPIES / f"{sujet['id']}.json") or {}
    corrige = (CORRECTIONS / f"{sujet['id']}.json").exists()
    s = {k: v for k, v in sujet.items() if corrige or k != "corrige"}
    s["statut"] = "corrige" if corrige else "rendu" if copie.get("rendue_le") else "en_cours" if copie else "nouveau"
    return s


class Gestionnaire(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(RACINE / "web"), **k)

    def repondre(self, code, donnees):
        corps = json.dumps(donnees, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def do_GET(self):
        parts = self.path.split("?")[0].strip("/").split("/")
        if parts[0] != "api":
            return super().do_GET()
        if parts[1:] == ["sujets"]:
            sujets = [public(lire(f)) for f in sorted(SUJETS.glob("*.json"), reverse=True)]
            return self.repondre(200, sujets)
        if len(parts) == 3 and ID.match(parts[2]):
            dossier = {"sujets": SUJETS, "copies": COPIES, "corrections": CORRECTIONS}.get(parts[1])
            donnees = lire(dossier / f"{parts[2]}.json") if dossier else None
            if donnees is not None:
                return self.repondre(200, public(donnees) if parts[1] == "sujets" else donnees)
            if parts[1] in ("copies", "corrections"):
                return self.repondre(200, {})
        self.repondre(404, {"erreur": "introuvable"})

    def do_PUT(self):
        parts = self.path.strip("/").split("/")
        if len(parts) != 3 or parts[:2] != ["api", "copies"] or not ID.match(parts[2]) \
                or not (SUJETS / f"{parts[2]}.json").exists():
            return self.repondre(404, {"erreur": "introuvable"})
        fichier = COPIES / f"{parts[2]}.json"
        if (lire(fichier) or {}).get("rendue_le") or (CORRECTIONS / f"{parts[2]}.json").exists():
            return self.repondre(409, {"erreur": "copie déjà rendue"})
        copie = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
        if copie.pop("rendre", False):
            copie["rendue_le"] = datetime.now().isoformat(timespec="seconds")
        fichier.write_text(json.dumps(copie, ensure_ascii=False, indent=1), encoding="utf-8")
        self.repondre(200, {"ok": True})


if __name__ == "__main__":
    for d in (SUJETS, COPIES, CORRECTIONS):
        d.mkdir(parents=True, exist_ok=True)
    print("Infraction Finder : http://127.0.0.1:8765")
    ThreadingHTTPServer(("127.0.0.1", 8765), Gestionnaire).serve_forever()
