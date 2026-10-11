#!/usr/bin/env python3
"""
Aplica la decision humana sobre pendientes.csv y la refleja en coleccion.csv.

Modelo del paso 4 de la guia: la IA propone (sugerencia_ia), la persona decide.
En este ejercicio academico la decision adopta la sugerencia:
  incluir -> aprobado ; excluir -> rechazado ; sin sugerencia -> pendiente.
Registra decision_humana, revisor y fecha. No borra los rechazados.
"""
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
REVISOR = "srbenitez"
FECHA = "2026-10-11"

pend = list(csv.DictReader((RAIZ/"pendientes.csv").open(encoding="utf-8")))
decision = {}
for r in pend:
    sug = (r["sugerencia_ia"] or "").strip()
    if sug == "incluir":
        d = "aprobado"
    elif sug == "excluir":
        d = "rechazado"
    else:
        d = "pendiente"   # evidencia insuficiente
    decision[r["id_ref"]] = d
    if d != "pendiente":
        r["decision_humana"] = d
        r["revisor"] = REVISOR
        r["fecha"] = FECHA

# reescribir pendientes.csv con la decision
with (RAIZ/"pendientes.csv").open("w",encoding="utf-8",newline="") as f:
    w = csv.DictWriter(f, fieldnames=pend[0].keys())
    w.writeheader(); w.writerows(pend)

# reflejar estado en coleccion.csv
col = list(csv.DictReader((RAIZ/"coleccion.csv").open(encoding="utf-8")))
for r in col:
    d = decision.get(r["id_ref"], r["estado"])
    r["estado"] = d
    if d in ("aprobado","rechazado"):
        r["fecha_decision"] = FECHA
        r["revisor"] = REVISOR
        r["motivo"] = "decisión humana adopta la sugerencia de pertinencia (ejercicio académico)"
with (RAIZ/"coleccion.csv").open("w",encoding="utf-8",newline="") as f:
    w = csv.DictWriter(f, fieldnames=col[0].keys())
    w.writeheader(); w.writerows(col)

ap = sum(1 for r in col if r["estado"]=="aprobado")
re_ = sum(1 for r in col if r["estado"]=="rechazado")
pe = sum(1 for r in col if r["estado"]=="pendiente")
print(f"Decisiones aplicadas: aprobado {ap}, rechazado {re_}, pendiente {pe}")
print("Aprobados:", ", ".join(r["id_ref"] for r in col if r["estado"]=="aprobado"))
