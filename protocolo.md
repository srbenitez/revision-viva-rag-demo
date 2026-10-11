# Protocolo · Revisión viva (demo)

**Proyecto:** Registro de revisión bibliográfica en actualización continua
**Caso de demostración:** Uso de RAG para consultar documentos institucionales
**Versión del protocolo:** v1 · 2026-10-10
**Revisor:** (tú)

> Nota de alcance: este es un **caso de demostración público**, independiente de la
> revisión real del autor. Sirve para evidenciar el *procedimiento* (importación,
> deduplicación, sugerencia justificada, aprobación humana, historial y síntesis
> con citas comprobadas), no para exponer la pregunta, los criterios ni los
> resultados de la investigación real.

## Pregunta acotada

¿Cómo se usa la generación aumentada por recuperación (RAG) para consultar
documentos institucionales en educación superior, de 2020 en adelante?

## Criterios de inclusión

| Criterio | Regla |
|---|---|
| Tema | RAG aplicado a consulta/recuperación de documentos institucionales u organizacionales |
| Tipo de estudio | Artículos revisados por pares y actas de congreso |
| Años | 2020 en adelante |
| Idiomas | Inglés y español |

Un registro se marca **pendiente** cuando el resumen no permite decidir; no se
incluye ni se excluye sin evidencia.

## Fuentes de búsqueda y cadenas (con registro de ejecución)

| Fuente | Estado | Fecha | Resultado | Evidencia |
|---|---|---|---|---|
| Scopus | **ejecutada** | 2026-10-11 | 10 registros (con DOI y resumen) | `lotes/lote_scopus_2026-10-11_raw.csv` |
| Google Académico | **ejecutada** | 2026-10-11 | 10 referencias (sin DOI ni resumen exportable) | `lotes/lote_scholar_2026-10-11_raw.txt` |
| OpenAlex | **pendiente** | — | no ejecutada (el entorno bloqueó su API) | — |

**Scopus** (campo TITLE-ABS-KEY):
```
TITLE-ABS-KEY(("retrieval augmented generation" OR "RAG")
AND ("institutional documents" OR "document retrieval" OR "document question answering")
AND (university OR "higher education" OR institutional)) AND PUBYEAR > 2019
```

**Google Académico** (desde 2020): `"retrieval augmented generation" "institutional documents"`.
Nota: Google Académico no exporta en lote de forma estructurada; sus referencias
entran sin DOI ni resumen, por lo que su cribado de pertinencia queda como
**evidencia insuficiente** hasta localizar la fuente.

**OpenAlex** (pendiente de correr desde una red con acceso):
`https://api.openalex.org/works?search=retrieval augmented generation institutional documents&filter=from_publication_date:2020-01-01,type:article`

Cada ejecución se registra con su fecha en `historial.md`; cambiar una cadena o un
criterio genera una nueva versión de este protocolo.

## Exportación

CSV con: DOI, título, año, autores, enlace estable, resumen.

## Revisión y aprobación

Un revisor. Cada incorporación o rechazo queda en `coleccion.csv` con decisión,
motivo, revisor y fecha. Los rechazados se conservan; si reaparecen en un lote
posterior, el registro lo advierte.

## Forma de la síntesis

Documento vivo `sintesis_<fecha>.md`, solo con artículos aprobados; cada
afirmación vinculada a un registro `[Rxx]`. De las citas de la síntesis, al menos
una se verifica contra el **texto completo** con su ubicación (página o sección);
las demás se marcan como observación del **resumen**.

## Límite declarado

Este registro mantiene una revisión viva de cribado; **no constituye por sí mismo
una revisión sistemática**. La sugerencia de pertinencia la propone la IA a partir
del resumen; la decisión y la verificación de citas son humanas.
