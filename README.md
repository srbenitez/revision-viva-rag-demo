# Revisión viva · demo RAG en documentos institucionales

Registro de **revisión bibliográfica en actualización continua** (Guía 10, curso
Vibe Coding CEDIA 2026). Importa lotes de referencias, deduplica por DOI, señala
títulos parecidos, propone pertinencia con IA y conserva la **decisión humana**
fechada, con historial y síntesis. Caso de **demostración público**, independiente
de la investigación real del autor.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `protocolo.md` | Pregunta, criterios, fuentes, cadena de búsqueda, fecha; versión |
| `reglas_dedup.md` | Normalización de DOI, umbral de título, regla sin DOI, rechazados |
| `coleccion.csv` | Registro único (18 referencias reales), estado `pendiente`; **fuente de verdad auditable** |
| `lotes/*_raw.*` | Exports crudos y fechados de Scopus (2026-10-11) y Google Académico (2026-10-11) |
| `lotes/lote_*_2026-10-11.csv` | Lotes normalizados por fuente |
| `pendientes.csv` | Hoja de cribado: sugerencia de IA y justificación; decisión humana en blanco |
| `historial.md` | Cambios fechados: duplicados, señalados, inclusiones, rechazos |
| `build_real.py` | Ingesta de los lotes reales: normaliza, deduplica en código y arma colección y pendientes |
| `dedup.py` | Deduplicación de un lote nuevo contra la colección (no la hace el modelo) |
| `index.html` | Visor web de solo lectura que presenta los CSV y el historial |

## Cómo se usa

1. **Procesar un lote nuevo** (deduplica y arma pendientes):
   ```
   python3 dedup.py lotes/lote_2026-10-10.csv
   ```
   Escribe `pendientes.csv` y añade un bloque fechado a `historial.md`.

2. **Sugerencia de pertinencia (IA):** sobre los registros nuevos de `pendientes.csv`,
   se pide a Claude —con `protocolo.md` y los resúmenes— una sugerencia *incluir/excluir*
   con justificación de dos frases. Nunca se evalúa un registro sin resumen: se marca
   "evidencia insuficiente".

3. **Decisión humana:** se completa `decision_humana`, `revisor` y `fecha` en
   `pendientes.csv`/`coleccion.csv`. La IA propone; usted decide.

4. **Ver el registro:** abrir el visor desde un servidor (no con doble clic):
   ```
   python3 -m http.server 8000
   ```
   y entrar a `http://localhost:8000/`.

## Publicar en GitHub Pages

Subir el repo a GitHub y en **Settings → Pages → Build and deployment →
Deploy from a branch → `main` / `(root)`**. La vitrina queda en
`https://<usuario>.github.io/revision-viva-rag-demo/`. Solo se publican metadatos y
resúmenes públicos; nada de PDF con licencia ni de la revisión real.

## Casos de comprobación (Guía 10), sobre datos reales

- **Duplicados entre fuentes**: H06≈S08 y H07≈S09 (mismos trabajos en Scopus y
  Académico) se señalan por similitud de título y no se fusionan.
- **Fuera de criterio**: S03 (hospital), S05 (banco central) y S07 (instituto de
  investigación) reciben sugerencia *excluir* por no ser educación superior.
- **Evidencia insuficiente**: las 8 referencias de Google Académico, sin resumen
  exportado, quedan sin cribar y marcadas como tales, sin inventar hallazgos.
- **Relación anotada**: H04 (hospital, 2025) se marca como posible versión previa de
  S03 (2026) para revisión humana; no se fusiona.

## Límite

Este registro mantiene una revisión viva de cribado; **no constituye por sí mismo
una revisión sistemática**. Si deriva en un artículo, aplica reporte tipo PRISMA y
declaración del uso de IA con verificación humana.

---
Curso Vibe Coding CEDIA 2026 · UTE y UTPL · uso educativo.
