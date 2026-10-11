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

## Fuentes de búsqueda

Scopus · OpenAlex · Google Académico.

## Cadena de búsqueda

```
("retrieval augmented generation" OR "RAG")
AND ("institutional documents" OR "document retrieval" OR "document question answering")
AND (education OR university OR "higher education")
```

Fecha de ejecución del lote base: 2026-10-10. Cada ejecución posterior se registra
con su fecha en `historial.md`; cambiar la cadena o un criterio genera una nueva
versión de este protocolo.

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
