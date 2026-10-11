#!/usr/bin/env python3
"""
Deduplicacion e importacion de lotes para la revision viva.

Reglas: ver reglas_dedup.md (v1). La deduplicacion se hace aqui, en codigo;
el modelo NO deduplica. El modelo solo sugiere pertinencia (paso posterior).

Uso:
    python3 dedup.py lotes/lote_2026-10-10.csv

Produce / actualiza:
    pendientes.csv   registros nuevos que esperan sugerencia de IA y decision humana
    historial.md     bloque fechado con lo importado, duplicados y senalados
"""

import csv
import re
import sys
import difflib
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
COLECCION = RAIZ / "coleccion.csv"
PENDIENTES = RAIZ / "pendientes.csv"
HISTORIAL = RAIZ / "historial.md"
UMBRAL_TITULO = 0.90

PREFIJOS_DOI = ("https://doi.org/", "http://dx.doi.org/", "http://doi.org/", "doi:")


def normalizar_doi(doi: str) -> str:
    """Regla 1: minusculas, sin prefijo de URL, sin espacios."""
    d = (doi or "").strip().lower()
    for p in PREFIJOS_DOI:
        if d.startswith(p):
            d = d[len(p):]
    return d.strip()


def normalizar_titulo(t: str) -> str:
    t = (t or "").lower()
    t = re.sub(r"[^\w\s]", "", t)        # sin puntuacion
    t = re.sub(r"\s+", " ", t).strip()    # sin espacios dobles
    return t


def leer_csv(ruta: Path):
    with ruta.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 dedup.py <ruta_al_lote.csv>")
    ruta_lote = Path(sys.argv[1])
    if not ruta_lote.exists():
        sys.exit(f"No existe el lote: {ruta_lote}")

    coleccion = leer_csv(COLECCION)
    lote = leer_csv(ruta_lote)

    # indices de la coleccion existente
    dois_existentes = {normalizar_doi(r["doi"]): r for r in coleccion if normalizar_doi(r["doi"])}
    por_anio = {}
    for r in coleccion:
        por_anio.setdefault(r["anio"], []).append(r)

    duplicados, senalados, nuevos = [], [], []

    for r in lote:
        doi_n = normalizar_doi(r.get("doi", ""))
        # Regla 2: duplicado exacto por DOI normalizado
        if doi_n and doi_n in dois_existentes:
            duplicados.append((r, dois_existentes[doi_n]))
            continue
        # Regla 3: titulo parecido en el mismo anio
        titulo_n = normalizar_titulo(r.get("titulo", ""))
        marca_similar = None
        for existente in por_anio.get(r.get("anio", ""), []):
            ratio = difflib.SequenceMatcher(None, titulo_n, normalizar_titulo(existente["titulo"])).ratio()
            if ratio >= UMBRAL_TITULO:
                marca_similar = (existente, round(ratio, 2))
                break
        if marca_similar:
            senalados.append((r, marca_similar[0], marca_similar[1]))
            continue
        nuevos.append(r)

    # pendientes.csv: nuevos que esperan sugerencia de IA + decision humana
    campos = ["id_ref", "doi", "titulo", "anio", "autores", "enlace", "resumen",
              "sugerencia_ia", "justificacion", "decision_humana", "revisor", "fecha", "nota"]
    with PENDIENTES.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in nuevos:
            nota = ""
            if not (r.get("resumen") or "").strip():
                nota = "evidencia insuficiente: sin resumen; no evaluar pertinencia ni inventar hallazgos"
            w.writerow({
                "id_ref": r["id_ref"], "doi": r.get("doi", ""), "titulo": r["titulo"],
                "anio": r["anio"], "autores": r.get("autores", ""), "enlace": r.get("enlace", ""),
                "resumen": r.get("resumen", ""), "sugerencia_ia": "", "justificacion": "",
                "decision_humana": "", "revisor": "", "fecha": "", "nota": nota,
            })

    # historial.md: bloque fechado
    hoy = date.today().isoformat()
    lineas = [f"\n## {hoy} · Importacion de {ruta_lote.name}\n"]
    lineas.append(f"- Registros en el lote: {len(lote)}\n")
    for r, ex in duplicados:
        lineas.append(f"- DUPLICADO descartado: {r['id_ref']} (DOI ya presente como {ex['id_ref']}); no genera registro nuevo\n")
    for r, ex, ratio in senalados:
        lineas.append(f"- TITULO PARECIDO ({ratio}): {r['id_ref']} se parece a {ex['id_ref']}; senalado para revision, no fusionado\n")
    for r in nuevos:
        if not (r.get("resumen") or "").strip():
            lineas.append(f"- NUEVO con evidencia insuficiente: {r['id_ref']} (sin resumen) -> pendiente\n")
        else:
            lineas.append(f"- NUEVO a cribado: {r['id_ref']} -> pendiente de sugerencia y aprobacion\n")
    with HISTORIAL.open("a", encoding="utf-8") as f:
        f.writelines(lineas)

    print(f"Lote: {ruta_lote.name}")
    print(f"  Duplicados descartados: {len(duplicados)}")
    print(f"  Titulos senalados:      {len(senalados)}")
    print(f"  Nuevos a pendientes:    {len(nuevos)}")
    print(f"Escrito: {PENDIENTES.name}, {HISTORIAL.name}")


if __name__ == "__main__":
    main()
