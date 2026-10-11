#!/usr/bin/env python3
"""
Importador de un export crudo de Scopus al esquema del registro.

Lee un CSV tal como lo exporta Scopus (columnas: Authors, Title, Year, DOI,
Link, Abstract, ...), lo mapea al esquema del registro y asigna identificadores
nuevos que no chocan con los existentes en coleccion.csv. Deja un lote
normalizado listo para dedup.py. NO deduplica ni decide: eso es dedup.py y la
persona.

Uso:
    python importar_scopus.py lotes/lote_scopus_2026-11-15_raw.csv
    python importar_scopus.py lotes/lote_scopus_2026-11-15_raw.csv --prefijo S --salida lotes/lote_scopus_2026-11-15.csv
"""
import csv, re, sys, argparse
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
COLECCION = RAIZ / "coleccion.csv"
ESQUEMA = ["id_ref","doi","titulo","anio","autores","enlace","resumen"]

# mapeo tolerante: nombre destino -> posibles nombres en el crudo de Scopus
MAPA = {
    "doi":     ["DOI", "doi"],
    "titulo":  ["Title", "title", "Document Title"],
    "anio":    ["Year", "year", "Publication Year"],
    "autores": ["Authors", "Author full names", "authors"],
    "enlace":  ["Link", "link", "URL"],
    "resumen": ["Abstract", "abstract"],
}

def primera(fila, nombres):
    for n in nombres:
        if n in fila and (fila[n] or "").strip():
            return fila[n].strip()
    return ""

def ids_existentes(prefijo):
    maxn = 0
    if COLECCION.exists():
        for r in csv.DictReader(COLECCION.open(encoding="utf-8-sig")):
            m = re.fullmatch(rf"{re.escape(prefijo)}(\d+)", (r.get("id_ref") or "").strip())
            if m:
                maxn = max(maxn, int(m.group(1)))
    return maxn

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("crudo")
    ap.add_argument("--prefijo", default="S", help="prefijo de id_ref (por defecto S de Scopus)")
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()

    crudo = Path(a.crudo)
    if not crudo.exists():
        sys.exit(f"No existe: {crudo}")
    salida = Path(a.salida) if a.salida else crudo.with_name(crudo.name.replace("_raw", ""))

    filas = list(csv.DictReader(crudo.open(encoding="utf-8-sig")))
    if not filas:
        sys.exit("El CSV crudo está vacío o no tiene encabezados reconocibles.")

    n = ids_existentes(a.prefijo)
    salida_filas, sin_doi, sin_titulo = [], 0, 0
    for fila in filas:
        titulo = primera(fila, MAPA["titulo"])
        if not titulo:
            sin_titulo += 1
            continue
        n += 1
        doi = primera(fila, MAPA["doi"])
        if not doi:
            sin_doi += 1
        salida_filas.append({
            "id_ref": f"{a.prefijo}{n:02d}",
            "doi": doi,
            "titulo": titulo,
            "anio": primera(fila, MAPA["anio"]),
            "autores": primera(fila, MAPA["autores"]),
            "enlace": primera(fila, MAPA["enlace"]),
            "resumen": primera(fila, MAPA["resumen"]),
        })

    with salida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ESQUEMA)
        w.writeheader(); w.writerows(salida_filas)

    print(f"Crudo: {crudo.name} ({len(filas)} filas)")
    print(f"Normalizado: {salida.name} ({len(salida_filas)} referencias, ids {a.prefijo}{n-len(salida_filas)+1:02d}..{a.prefijo}{n:02d})")
    if sin_doi:    print(f"  Aviso: {sin_doi} sin DOI (dedup usará título + año).")
    if sin_titulo: print(f"  Aviso: {sin_titulo} fila(s) sin título, omitidas.")
    print(f"Siguiente: python dedup.py {salida.as_posix()}")

if __name__ == "__main__":
    main()
