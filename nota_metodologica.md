# Nota metodológica y declaración de uso de IA

**Proyecto:** Registro de revisión bibliográfica en actualización continua (Guía 10)
**Caso de demostración:** Uso de RAG para consultar documentos institucionales
**Fecha:** 2026-10-11 · **Protocolo:** v1 · **Revisor:** srbenitez

## Propósito y alcance

Mantener una revisión viva: importar lotes de referencias, deduplicar, proponer
pertinencia con IA y conservar la decisión humana fechada, con historial y síntesis.
Es un **caso de demostración público**, independiente de la investigación real del
autor. No es, por sí mismo, una revisión sistemática.

## Datos y procedencia

- **Scopus**, ejecutado el 2026-10-11 (TITLE-ABS-KEY, PUBYEAR > 2019): 10 registros
  con DOI y resumen. Export crudo: `lotes/lote_scopus_2026-10-11_raw.csv`.
- **Google Académico**, 2026-10-11: 10 referencias sin DOI ni resumen exportable.
  Export crudo: `lotes/lote_scholar_2026-10-11_raw.txt`.
- **OpenAlex**: pendiente (el entorno de construcción bloqueó su API).
- Las cadenas de búsqueda por fuente están en `protocolo.md`.

## Reglas de tratamiento

- Deduplicación **en código** (`build_real.py`, `dedup.py`): DOI normalizado como
  clave; sin DOI, título normalizado + mismo año con umbral de similitud 0.90.
  La deduplicación no se delega al modelo. Reglas en `reglas_dedup.md`.
- Un registro sin resumen se marca **evidencia insuficiente**; no se cribar ni se
  inventan hallazgos.

## Intervención de IA y humana (declaración proporcional)

- **La IA (Claude) hizo:** proponer la sugerencia de pertinencia (incluir/excluir)
  con una justificación que cita el resumen; parafrasear resúmenes; recuperar y
  parafrasear resúmenes de tres referencias desde su fuente real (H01 arXiv, H02 y
  H03 MDPI); escribir el código de deduplicación y el visor.
- **La persona hizo / debe hacer:** fijar pregunta y criterios; decidir la
  inclusión o exclusión de cada registro (en este ejercicio académico la decisión
  adoptó la sugerencia, registrada con revisor y fecha); y **verificar los enlaces
  y las citas**. La decisión y la verificación son humanas.
- **Qué NO se declara como verificado:** las cifras de desempeño de los estudios
  (observadas en resúmenes), y el cribado de las 5 referencias sin resumen.

## Comprobaciones ejecutadas

- Deduplicación detectó 2 coincidencias entre fuentes (H06≈S08, H07≈S09), señaladas
  y no fusionadas.
- CSV validados (columnas consistentes); visor servido localmente sin errores.
- Síntesis con 3 citas comprobadas, una de ellas contra **texto completo** con
  ubicación (H02, §5.3).

## Resultados

- 20 registros importados → 2 duplicados entre fuentes → **18 únicos**.
- Decisión: **9 aprobados, 4 rechazados** (hospital, banco central, instituto de
  investigación, museo de ciencia: fuera de educación superior), **5 pendientes**
  por evidencia insuficiente.

## Limitaciones y pendientes

- El registro **no constituye una revisión sistemática**; es cribado vivo que
  alimenta una revisión. Si deriva en artículo, aplicar reporte tipo PRISMA y
  declarar el cribado asistido por IA con verificación humana.
- Falta la tercera fuente (OpenAlex) y recuperar el texto de 5 referencias.
- La sugerencia de la IA puede variar entre ejecuciones; el registro válido es la
  decisión humana fechada, con la versión del protocolo.
- Google Académico no permite exportación estructurada reproducible: es una
  limitación de la fuente, anotada en el protocolo.
