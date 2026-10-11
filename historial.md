# Historial · Revisión viva (RAG en documentos institucionales)

Registro fechado de cambios: lotes importados, duplicados detectados, títulos
señalados, inclusiones y rechazos. No se borra nada; se añade.

## 2026-10-10 · Estado inicial (conjunto de demostración, superado)
- Primera versión con una colección de referencias canónicas de RAG, ensamblada
  manualmente para probar el procedimiento. **Superada el 2026-10-11** por búsquedas
  reales en bases de datos (ver abajo). Se conserva la nota por trazabilidad.

## 2026-10-11 · Ejecución real de búsquedas e importación
- **Scopus** ejecutado el 2026-10-11 (TITLE-ABS-KEY, PUBYEAR > 2019): 10 registros
  exportados con DOI y resumen. Export crudo: `lotes/lote_scopus_2026-10-11_raw.csv`.
- **Google Académico** ejecutado el 2026-10-11 (desde 2020): 10 referencias
  recuperadas. **Sin exportación estructurada**: no trae DOI ni resumen (limitación
  real de la fuente). Export crudo: `lotes/lote_scholar_2026-10-11_raw.txt`.
- **OpenAlex**: la ejecución quedó **pendiente** — el entorno de construcción bloqueó
  el acceso a su API. Debe correrse desde una red con acceso y añadirse como un lote
  más.
- Deduplicación en código (DOI normalizado; sin DOI, título + mismo año, umbral 0.90):
  - DUPLICADO/parecido: H06 ≈ S08 (ratio 1.0) — "From policy to practice…" en ambas fuentes; no se fusiona, se conserva S08.
  - DUPLICADO/parecido: H07 ≈ S09 (ratio 1.0) — "Effective Chunking…" en ambas fuentes; se conserva S09.
  - Observación para revisión humana: H04 (hospital, 2025) puede ser versión previa de S03 (hospital, 2026); distinto año y título, no se fusionó.
- Resultado: **18 registros únicos** (10 Scopus + 8 de Académico), todos `pendiente`.
- Cribado propuesto por IA: **7 incluir, 3 excluir** (S03 hospital, S05 banco central, S07 instituto de investigación: fuera de "educación superior"), **8 evidencia insuficiente** (los de Académico, sin resumen exportado).
- Falta: decisión humana por registro y verificación de citas en la síntesis.
