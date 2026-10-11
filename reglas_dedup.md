# Reglas de deduplicación · v1 · 2026-10-10

Estas reglas se escriben **antes** de importar cualquier lote y se versionan junto
con el protocolo. La deduplicación se hace en código, con reglas de texto; **no se
delega al modelo**. El modelo solo sugiere pertinencia y la justifica.

## 1. Normalización de DOI (clave primaria)

El DOI es la clave para decidir identidad. Antes de comparar se normaliza:

1. Pasar a minúsculas.
2. Quitar los prefijos de URL: `https://doi.org/`, `http://dx.doi.org/`, `doi:`.
3. Quitar espacios al inicio y al final.

Ejemplo: `https://doi.org/10.1145/3539618.3591699` y `10.1145/3539618.3591699`
son el **mismo** artículo.

## 2. Duplicado exacto

Mismo DOI normalizado que un registro ya presente en la colección → el registro del
lote **se descarta** y el hecho se anota en `historial.md`. No genera un segundo
registro aprobado.

## 3. Título parecido (sospecha, no evidencia)

Para registros con el **mismo año** se compara el título normalizado (minúsculas,
sin puntuación ni espacios dobles). Si la similitud supera el umbral, se **señala
para revisión humana**; nunca se fusiona automáticamente.

- Medida: similitud por `difflib.SequenceMatcher` (ratio de 0 a 1).
- Umbral: **0.90**.
- Caso típico que debe señalarse, no fusionarse: *preprint* y versión publicada
  del mismo trabajo — comparten título pero son dos registros, con su relación
  anotada.

## 4. Referencias sin DOI

Actas, informes y muchas fuentes en español/portugués (SciELO, Redalyc) no traen
DOI. Para ellas:

- Se exige un **enlace estable**.
- La comparación de identidad se hace por **título normalizado + año**.
- Si coinciden título y año con un registro existente, se trata como duplicado
  (regla 2); si el título es parecido pero no idéntico, se señala (regla 3).

## 5. Rechazados

Un rechazado se **conserva** con su motivo, revisor y fecha en `coleccion.csv`
(estado `rechazado`). Si un lote posterior vuelve a traer ese DOI, el registro lo
**advierte** en el historial en vez de reabrir la discusión. Un rechazado con
motivo vale más que un borrado.

## 6. Evidencia insuficiente

Un registro sin resumen no puede evaluarse por pertinencia: la sugerencia de la IA
debe decir **"evidencia insuficiente"** y el registro queda `pendiente`, sin
inventar hallazgos.
