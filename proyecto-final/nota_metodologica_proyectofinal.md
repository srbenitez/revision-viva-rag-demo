# Nota metodológica · Proyecto final

**Herramienta:** Registro de revisión bibliográfica en actualización continua (Guía 10)
**Subgrupo G3.3:** Marcelo Carrera (Universidad UTE) · Segundo Benítez (UTPL)
**Fecha:** 2026-10-11 · **Curso:** Vibe Coding CEDIA 2026

> Esta nota, junto con la presentación, forma el entregable del módulo 5. Lo que
> todavía no existe o no se ha confirmado se marca como **pendiente**; no se inventa.

## 1 · Propósito y límite

La herramienta mantiene viva una revisión bibliográfica: importa lotes de
referencias, deduplica en código, propone pertinencia con IA y conserva la decisión
humana fechada, con historial y síntesis. **Hasta dónde llega:** apoya el cribado;
**no es por sí misma una revisión sistemática**. La sugerencia de pertinencia la
propone la IA a partir del resumen; la decisión y la verificación de citas son
humanas. Se trabaja con un caso de demostración público sobre "Uso de RAG para
consultar documentos institucionales", independiente de la investigación real del
autor.

## 2 · Recorrido revisable

- **Entrada:** un lote de referencias (CSV de Scopus) con título, año, DOI, enlace y
  resumen; más la pregunta y los criterios de inclusión fijados en `protocolo.md`.
- **Regla aplicada:** deduplicación por DOI normalizado y por título parecido (umbral
  de similitud 0,90) en código (`dedup.py`, `build_real.py`); un registro sin resumen
  se marca "evidencia insuficiente" y no se evalúa.
- **Resultado:** `coleccion.csv` (registro único con estado), `pendientes.csv`
  (sugerencia de IA + decisión humana) y `sintesis_2026-10-11.md` (solo aprobados).
- **Evidencia:** 20 referencias importadas → 2 duplicados detectados entre fuentes →
  18 únicas → 9 aprobadas, 4 rechazadas, 5 pendientes. Una cita verificada contra el
  texto completo con su ubicación (H02, §5.3). Los export crudos de las búsquedas
  quedan fechados en `lotes/`.

## 3 · Aportes de la IA y de las personas

| Intervención | Herramienta | Entrada | Producto | Revisó |
|---|---|---|---|---|
| Sugerencia de pertinencia | Claude (texto) | resúmenes + criterios | incluir/excluir con justificación | la persona (decisión) |
| Recuperación de resúmenes | Claude + web | referencias sin resumen | 3 resúmenes verificados en su fuente | la persona (pendiente de confirmar enlaces) |
| Deduplicación | Python (código) | lotes + colección | duplicados y títulos señalados | determinista, revisable |
| Guion y presentaciones | Claude | contenido de la herramienta | 10 diapositivas ES/EN + narración | la persona |
| Narración de voz | ElevenLabs (voz clonada del autor) | guion por diapositiva | 20 audios mp3 | la persona (escucha completa) |
| Producción de video | ffmpeg (código) | diapositivas + audios | 2 videos MP4 | la persona |

La decisión de inclusión/exclusión, en este ejercicio académico, **adoptó la
sugerencia** de la IA y quedó firmada con revisor y fecha.

## 4 · Versiones

- **Presentaciones:** `VC-2026-028-NNN_ProyectoFinal_ES.pptx` y `_EN.pptx`.
- **Videos:** `VC-2026-028-NNN_ProyectoFinal_ES.mp4` y `_EN.mp4` (4:33, 1920×1080).
- **Evidencia (herramienta):** `protocolo.md` v1, `reglas_dedup.md` v1,
  `coleccion.csv`, `pendientes.csv`, `historial.md`, `sintesis_2026-10-11.md`,
  lotes crudos fechados en `lotes/`.
- Repositorio: github.com/srbenitez/revision-viva-rag-demo (historial de commits).
- **Pendiente:** número de registro de Marcelo Carrera para reemplazar `NNN` en los
  nombres de archivo definitivos.

## 5 · Alcance y declaración de uso de IA

- **Qué se puede concluir:** sobre este corpus y estos criterios, la deduplicación en
  código detecta duplicados entre fuentes y los señala sin fusionarlos, y el cribado
  asistido distingue lo pertinente de lo que carece de evidencia.
- **Qué no se puede concluir:** no es una revisión sistemática; las cifras de
  desempeño de los estudios citados son observaciones del resumen, no verificadas en
  texto completo salvo la cita marcada; cinco referencias quedan sin cribar por falta
  de resumen; falta ejecutar una tercera fuente (OpenAlex).
- **Declaración de IA:** la IA propuso pertinencia, redactó código, guion y
  presentaciones, y generó la narración con la voz clonada del autor. La decisión, la
  verificación y la revisión final son humanas. La narración se declara como voz de
  IA en la portada de ambos videos.

## 6 · Plan de mantenimiento

- **Responsable:** Segundo Benítez (UTPL) mantiene el registro; Marcelo Carrera (UTE)
  revisa. *(Rol acordado por el subgrupo; confirmar.)*
- **Qué activa una revisión:** cambiar la pregunta o un criterio (nueva versión del
  protocolo y repetir lo afectado); añadir una fuente o un lote nuevo; cambiar el
  modelo o la versión del prompt.
- **Qué hacer si falla:** detener el uso del resultado afectado, conservar la
  evidencia (lotes crudos e historial), revisar la regla o el dato, y decidir de
  nuevo con la persona. El historial permite rehacer la colección paso a paso.

---
Curso Vibe Coding CEDIA 2026 · Universidad UTE y UTPL · uso educativo.
Narración generada con voz de IA (ElevenLabs) y revisada por los autores.
