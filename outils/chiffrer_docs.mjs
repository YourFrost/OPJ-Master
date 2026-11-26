// Construit l'index de recherche de la documentation en diffusion restreinte et le publie CHIFFRÉ.
//   node outils/chiffrer_docs.mjs "mot de passe"
// Sources (jamais publiées en clair) : _ancien/data/referentiel/*.json et les méthodologies PDF (pdftotext requis).
// Sortie : data/docs.chiffre.json = AES-256-GCM(gzip(JSON)), clé dérivée par PBKDF2-SHA256.
import { readFileSync, writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { gzipSync } from "node:zlib";
import { webcrypto as crypto } from "node:crypto";

const mdp = process.argv[2];
if (!mdp || mdp.length < 8) { console.error("Usage : node outils/chiffrer_docs.mjs \"mot de passe (8 caractères min.)\""); process.exit(1); }

const RACINE = new URL("..", import.meta.url).pathname.replace(/^\/([A-Z]:)/, "$1");
const REF = decodeURIComponent(RACINE) + "_ancien/data/referentiel/";
const DOCS = "C:/Users/User/Desktop/Révision OPJ/Documents/Méthologie/";
const json = (f) => JSON.parse(readFileSync(REF + f, "utf-8"));
const corpus = [];
const ajouter = (source, titre, texte) => texte?.trim() && corpus.push({ source, titre, texte: texte.trim() });

for (const g of json("gps.json")) ajouter("GPS", g.titre, `${g.modele}\n\nÀ SAVOIR\n${g.a_savoir}`);
const tacl = json("tacl.json");
for (const l of tacl.lignes) ajouter("TACL", l.libelle, l.tous ? `Tous cadres : ${l.tous}` : tacl.cadres.filter((c) => l[c.id]).map((c) => `${c.libelle} : ${l[c.id]}`).join("\n"));
const em = json("erreurs_majeures.json");
ajouter("Erreurs majeures", "Sanction des erreurs majeures", `${em.sanction}\n${em.erreurs_mineures}`);
for (const c of em.categories) ajouter("Erreurs majeures", c.libelle, c.erreurs.map((e) => "- " + e).join("\n"));
for (const f of json("gpi.json")) {
  for (const i of f.infractions) ajouter("GPI", i.libelle, `${i.qualification}\nÉlément légal : ${i.element_legal}\nÉlément matériel :\n${i.elements_materiels.map((x) => "- " + x).join("\n")}\nÉlément moral : ${i.element_moral}`);
  ajouter("GPI", `Distinctions et exemples : ${f.theme}`, ["distinctions", "precisions", "exemples"].flatMap((k) => (f[k] || []).map((x) => "- " + x)).join("\n"));
}
for (const r of json("articles_a_connaitre.json").rubriques) ajouter("Articles à connaître", r.titre, r.articles.map((a) => `${a.notion} : ${a.articles}${a.consigne ? " (" + a.consigne + ")" : ""}`).join("\n"));
for (const [nom, fichier] of [["Méthodologie PP", "Méthodologie PP - 08_2026.pdf"], ["Méthodologie CRT", "Méthodologie CRT - 2026.pdf"], ["Méthodologie DPG/DPS", "Méthodologie DPG DPS - 21_09_26.pdf"]]) {
  const texte = execFileSync("pdftotext", ["-enc", "UTF-8", "-layout", DOCS + fichier, "-"]).toString("utf-8");
  texte.split("\f").forEach((page, i) => ajouter(nom, `${nom} – page ${i + 1}`, page.replace(/[ \t]{3,}/g, "  ")));
}

const sel = crypto.getRandomValues(new Uint8Array(16)), iv = crypto.getRandomValues(new Uint8Array(12)), iterations = 250000;
const base = await crypto.subtle.importKey("raw", new TextEncoder().encode(mdp), "PBKDF2", false, ["deriveKey"]);
const cle = await crypto.subtle.deriveKey({ name: "PBKDF2", salt: sel, iterations, hash: "SHA-256" }, base, { name: "AES-GCM", length: 256 }, false, ["encrypt"]);
const chiffre = await crypto.subtle.encrypt({ name: "AES-GCM", iv }, cle, gzipSync(Buffer.from(JSON.stringify(corpus))));
const b64 = (x) => Buffer.from(x).toString("base64");
writeFileSync(decodeURIComponent(RACINE) + "data/docs.chiffre.json", JSON.stringify({ format: "aes-256-gcm+pbkdf2-sha256+gzip", iterations, sel: b64(sel), iv: b64(iv), donnees: b64(chiffre) }));
console.log(`${corpus.length} fiches chiffrées -> data/docs.chiffre.json`);
