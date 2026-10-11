#!/usr/bin/env python3
# Guion ES del proyecto final. Conteo de palabras por diapositiva y tiempo (palabras/130*60).
guion = {
 1: ("Portada", 25, 35,
 "Presentamos nuestro registro de revisión bibliográfica en actualización continua. "
 "Somos Marcelo Carrera, de la Universidad U T E, y Segundo Benítez, de la U T P L. "
 "Mantiene viva una revisión sin rehacerla a mano."),
 2: ("El problema", 70, 80,
 "Una revisión bibliográfica envejece desde el día en que se entrega. "
 "Aparecen estudios nuevos cada semana. "
 "Volver a buscar y a depurar duplicados a mano casi nunca ocurre. "
 "Falta tiempo. "
 "Veamos un caso concreto. "
 "Traemos un lote nuevo desde Scopus. "
 "Un artículo que ya teníamos vuelve a entrar. "
 "Su identificador D O I viene escrito como dirección web. "
 "Si nadie lo nota, se cuela dos veces. "
 "Así la revisión pierde confianza."),
 3: ("La herramienta", 60, 70,
 "Construimos un registro vivo basado en la guía diez del curso. "
 "Lo usa un docente o un investigador. "
 "Recibe lotes de referencias con título, año y resumen. "
 "Entrega tres cosas. "
 "Una colección sin duplicados. "
 "Una lista de pendientes con una sugerencia de pertinencia. "
 "Y una síntesis con citas comprobadas. "
 "Todo queda en archivos de texto sencillos que cualquiera puede abrir y revisar."),
 4: ("Cómo funciona", 80, 90,
 "El flujo tiene cuatro pasos. "
 "Primero la persona fija la pregunta y los criterios de inclusión. "
 "Segundo un programa deduplica en código. "
 "Compara el D O I normalizado y los títulos parecidos. "
 "Esta parte no la decide el modelo. "
 "Tercero la inteligencia artificial sugiere incluir o excluir cada estudio. "
 "Siempre cita el resumen y da un motivo breve. "
 "Cuarto la persona revisa y decide. "
 "La decisión queda firmada con su nombre y la fecha. "
 "El modelo propone. Nosotros decidimos y dejamos constancia."),
 5: ("Evidencia", 70, 80,
 "Hicimos una prueba real con dos fuentes. "
 "Importamos veinte referencias. "
 "El programa detectó dos duplicados entre fuentes y los señaló sin fusionarlos. "
 "Quedaron dieciocho referencias únicas. "
 "Sobre ellas decidimos. "
 "Nueve aprobadas. "
 "Cuatro rechazadas por estar fuera del tema. "
 "Cinco quedaron pendientes por falta de resumen. "
 "Además verificamos una cita contra el texto completo, con su página. "
 "Guardamos también las búsquedas originales con su fecha. "
 "Separamos lo comprobado de lo que todavía es una propuesta."),
 6: ("Límites y uso responsable", 50, 60,
 "Seamos claros con los límites. "
 "Este registro apoya el cribado. "
 "No es por sí mismo una revisión sistemática. "
 "Google Académico no entrega resúmenes. "
 "Por eso algunas referencias quedan sin evaluar. "
 "Cuidamos los datos. "
 "Solo mostramos información pública. "
 "El siguiente paso es sumar una tercera fuente y llevarlo al aula virtual."),
 7: ("Demostración · Entrada", 60, 70,
 "Veamos la herramienta en pantalla. "
 "Esta es la vista de la colección. "
 "Cada fila es una referencia con su identificador, su título y su estado. "
 "Arriba hay un buscador y un filtro por estado. "
 "Aquí la persona parte de criterios claros. "
 "El visor no modifica nada. "
 "Solo muestra lo que el registro contiene. "
 "Desde esta misma pantalla se entiende qué entró, de qué fuente y con qué fecha."),
 8: ("Demostración · Resultado", 70, 80,
 "Pasamos a la lista de pendientes. "
 "Aquí está el corazón del registro. "
 "Para cada estudio la inteligencia artificial propone incluir o excluir. "
 "Y escribe una justificación que cita el resumen. "
 "Cuando una referencia no trae resumen, el sistema lo marca como evidencia insuficiente. "
 "No inventa un veredicto. "
 "Cada sugerencia muestra también el enlace a la fuente. "
 "La columna de decisión humana queda en blanco. "
 "Está lista para que la persona resuelva."),
 9: ("Demostración · Revisión y entrega", 60, 70,
 "Finalmente la pantalla del historial. "
 "Aquí queda el registro fechado de cada cambio. "
 "Qué lote entró. "
 "Qué duplicado se descartó. "
 "Qué se aprobó o se rechazó y quién lo decidió. "
 "Nada se borra. "
 "Un rechazo se conserva con su motivo. "
 "Así no reaparece sin aviso. "
 "Con este historial cualquiera puede rehacer la colección paso a paso. "
 "La síntesis final se exporta solo con los estudios aprobados."),
 10: ("Cierre", 50, 60,
 "Con este registro la revisión deja de envejecer sin control. "
 "El trabajo manual de depurar se reduce. "
 "Y la decisión sigue siendo humana. "
 "Pueden ver el proyecto en nuestro sitio público. "
 "Gracias por acompañarnos. "
 "Somos Marcelo Carrera y Segundo Benítez, de la U T E y la U T P L."),
}
tot_w=0; tot_s=0
print(f"{'#':>2} {'Diapositiva':34} {'Pal':>4} {'Rango':>9} {'Seg':>5} Estado")
for n,(t,lo,hi,txt) in guion.items():
    w=len(txt.split()); s=w/130*60; tot_w+=w; tot_s+=s
    est="ok" if lo<=w<=hi else ("CORTO" if w<lo else "LARGO")
    print(f"{n:>2} {t:34} {w:>4} {str(lo)+'-'+str(hi):>9} {s:>5.0f} {est}")
print(f"{'':>2} {'TOTAL':34} {tot_w:>4} {'':>9} {tot_s:>5.0f}  (meta 300 s)")
