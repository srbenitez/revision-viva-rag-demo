// Genera la presentación en español del proyecto final.
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.defineLayout({ name: "W16", width: 13.333, height: 7.5 });
p.layout = "W16";

const DARK="0B1020", GOLD="FFC629", VIOLET="5B4BDB", TEAL="0D9488",
      INK="1C1A17", MUTED="6B645C", WHITE="FFFFFF", CARD="EEEFF8", CARD2="E6F2F0";
const HEAD="Georgia", BODY="Calibri";

const N = {
 1:"Presentamos nuestro registro de revisión bibliográfica en actualización continua. Somos Marcelo Carrera, de la Universidad U T E, y Segundo Benítez, de la U T P L. Mantiene viva una revisión sin rehacerla a mano.",
 2:"Una revisión bibliográfica envejece desde el día en que se entrega. Aparecen estudios nuevos cada semana. Volver a buscar y a depurar duplicados a mano casi nunca ocurre. Falta tiempo. Veamos un caso concreto. Traemos un lote nuevo desde Scopus. Un artículo que ya teníamos vuelve a entrar. Su identificador D O I viene escrito como dirección web. Si nadie lo nota, se cuela dos veces. Así la revisión pierde confianza.",
 3:"Construimos un registro vivo basado en la guía diez del curso. Lo usa un docente o un investigador. Recibe lotes de referencias con título, año y resumen. Entrega tres cosas. Una colección sin duplicados. Una lista de pendientes con una sugerencia de pertinencia. Y una síntesis con citas comprobadas. Todo queda en archivos de texto sencillos que cualquiera puede abrir y revisar.",
 4:"El flujo tiene cuatro pasos. Primero la persona fija la pregunta y los criterios de inclusión. Segundo un programa deduplica en código. Compara el D O I normalizado y los títulos parecidos. Esta parte no la decide el modelo. Tercero la inteligencia artificial sugiere incluir o excluir cada estudio. Siempre cita el resumen y da un motivo breve. Cuarto la persona revisa y decide. La decisión queda firmada con su nombre y la fecha. El modelo propone. Nosotros decidimos y dejamos constancia.",
 5:"Hicimos una prueba real con dos fuentes. Importamos veinte referencias. El programa detectó dos duplicados entre fuentes y los señaló sin fusionarlos. Quedaron dieciocho referencias únicas. Sobre ellas decidimos. Nueve aprobadas. Cuatro rechazadas por estar fuera del tema. Cinco quedaron pendientes por falta de resumen. Además verificamos una cita contra el texto completo, con su página. Guardamos también las búsquedas originales con su fecha. Separamos lo comprobado de lo que todavía es una propuesta.",
 6:"Seamos claros con los límites. Este registro apoya el cribado. No es por sí mismo una revisión sistemática. Google Académico no entrega resúmenes. Por eso algunas referencias quedan sin evaluar. Cuidamos los datos. Solo mostramos información pública. El siguiente paso es sumar una tercera fuente y llevarlo al aula virtual.",
 7:"Veamos la herramienta en pantalla. Esta es la vista de la colección. Cada fila es una referencia con su identificador, su título y su estado. Arriba hay un buscador y un filtro por estado. Aquí la persona parte de criterios claros. El visor no modifica nada. Solo muestra lo que el registro contiene. Desde esta misma pantalla se entiende qué entró, de qué fuente y con qué fecha.",
 8:"Pasamos a la lista de pendientes. Aquí está el corazón del registro. Para cada estudio la inteligencia artificial propone incluir o excluir. Y escribe una justificación que cita el resumen. Cuando una referencia no trae resumen, el sistema lo marca como evidencia insuficiente. No inventa un veredicto. Cada sugerencia muestra también el enlace a la fuente. La columna de decisión humana queda en blanco. Está lista para que la persona resuelva.",
 9:"Finalmente la pantalla del historial. Aquí queda el registro fechado de cada cambio. Qué lote entró. Qué duplicado se descartó. Qué se aprobó o se rechazó y quién lo decidió. Nada se borra. Un rechazo se conserva con su motivo. Así no reaparece sin aviso. Con este historial cualquiera puede rehacer la colección paso a paso. La síntesis final se exporta solo con los estudios aprobados.",
 10:"Con este registro la revisión deja de envejecer sin control. El trabajo manual de depurar se reduce. Y la decisión sigue siendo humana. Pueden ver el proyecto en nuestro sitio público. Gracias por acompañarnos. Somos Marcelo Carrera y Segundo Benítez, de la U T E y la U T P L.",
};

function footer(s, n){
  s.addText("Vibe Coding CEDIA 2026 · Universidad UTE · UTPL",
    {x:0.7,y:7.08,w:9,h:0.3,fontFace:BODY,fontSize:9,color:MUTED,isTextBox:true,margin:0});
  s.addText(`${n} / 10`,
    {x:11.0,y:7.08,w:1.63,h:0.3,fontFace:BODY,fontSize:9,color:MUTED,align:"right",isTextBox:true,margin:0});
}
function title(s, t, color){
  s.addText(t,{x:0.7,y:0.5,w:11.9,h:0.9,fontFace:HEAD,fontSize:32,bold:true,color:color||INK,isTextBox:true,margin:0});
}

// ---------- 1 · Portada ----------
let s = p.addSlide();
s.background = { color: DARK };
s.addShape(p.ShapeType.ellipse,{x:9.8,y:4.3,w:5.2,h:5.2,fill:{color:GOLD,transparency:88},line:{type:"none"}});
s.addText("Revisión bibliográfica en actualización continua",
  {x:0.8,y:1.5,w:11.0,h:1.8,fontFace:HEAD,fontSize:40,bold:true,color:WHITE,isTextBox:true,margin:0});
s.addText("Mantiene viva una revisión sin rehacerla a mano",
  {x:0.8,y:3.3,w:10.5,h:0.6,fontFace:BODY,fontSize:20,italic:true,color:GOLD,isTextBox:true,margin:0});
s.addText([
  {text:"Marcelo Carrera  ·  Universidad UTE",options:{breakLine:true}},
  {text:"Segundo Benítez  ·  UTPL",options:{breakLine:true}},
  {text:"Guía 10 · Vibe Coding CEDIA 2026",options:{color:"AEB4C7"}},
],{x:0.8,y:4.5,w:10,h:1.4,fontFace:BODY,fontSize:18,color:WHITE,lineSpacingMultiple:1.2,isTextBox:true,margin:0});
s.addText("Narración generada con voz de IA (ElevenLabs) y revisada por los autores",
  {x:0.8,y:6.7,w:11.5,h:0.4,fontFace:BODY,fontSize:12,color:"AEB4C7",isTextBox:true,margin:0});
s.addNotes(N[1]);

// ---------- 2 · El problema ----------
s = p.addSlide(); s.background={color:WHITE}; title(s,"El problema");
s.addText("Una revisión envejece desde el día en que se entrega. Rebuscar y depurar a mano casi nunca ocurre.",
  {x:0.7,y:1.6,w:7.0,h:2.2,fontFace:BODY,fontSize:22,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.15});
s.addShape(p.ShapeType.roundRect,{x:8.1,y:1.7,w:4.5,h:3.6,rectRadius:0.12,fill:{color:CARD},line:{type:"none"}});
s.addText("2×",{x:8.1,y:2.0,w:4.5,h:1.4,fontFace:HEAD,fontSize:66,bold:true,color:VIOLET,align:"center",isTextBox:true,margin:0});
s.addText("El mismo artículo se cuela dos veces cuando el D O I viene como dirección web",
  {x:8.4,y:3.5,w:3.9,h:1.6,fontFace:BODY,fontSize:18,color:INK,align:"center",valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.1});
footer(s,2); s.addNotes(N[2]);

// ---------- 3 · La herramienta ----------
s = p.addSlide(); s.background={color:WHITE}; title(s,"La herramienta");
const cards3 = [
  ["Recibe","Lotes de referencias con título, año y resumen",VIOLET],
  ["Procesa","Deduplica en código y la IA sugiere pertinencia",TEAL],
  ["Entrega","Colección, pendientes y una síntesis comprobada",VIOLET],
];
cards3.forEach((c,i)=>{
  const x=0.7+i*4.08;
  s.addShape(p.ShapeType.roundRect,{x,y:2.1,w:3.75,h:3.4,rectRadius:0.12,fill:{color:i===1?CARD2:CARD},line:{type:"none"}});
  s.addText(c[0],{x:x+0.3,y:2.4,w:3.15,h:0.6,fontFace:HEAD,fontSize:22,bold:true,color:c[2],isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.3,y:3.15,w:3.15,h:2.1,fontFace:BODY,fontSize:18,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.15});
});
footer(s,3); s.addNotes(N[3]);

// ---------- 4 · Cómo funciona ----------
s = p.addSlide(); s.background={color:WHITE}; title(s,"Cómo funciona");
const steps=[
  ["1","Criterios","La persona fija pregunta y criterios"],
  ["2","Deduplica","Un programa compara en código, no el modelo"],
  ["3","La IA sugiere","Propone incluir o excluir y cita el resumen"],
  ["4","Decide","La persona aprueba y firma la decisión"],
];
steps.forEach((c,i)=>{
  const x=0.7+i*3.05;
  s.addShape(p.ShapeType.roundRect,{x,y:2.3,w:2.75,h:3.1,rectRadius:0.12,fill:{color:CARD},line:{type:"none"}});
  s.addShape(p.ShapeType.ellipse,{x:x+0.3,y:2.55,w:0.75,h:0.75,fill:{color:i===3?TEAL:VIOLET},line:{type:"none"}});
  s.addText(c[0],{x:x+0.3,y:2.55,w:0.75,h:0.75,fontFace:HEAD,fontSize:24,bold:true,color:WHITE,align:"center",valign:"middle",isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.28,y:3.5,w:2.2,h:0.6,fontFace:HEAD,fontSize:19,bold:true,color:INK,isTextBox:true,margin:0});
  s.addText(c[2],{x:x+0.28,y:4.1,w:2.25,h:1.2,fontFace:BODY,fontSize:16,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.1});
});
s.addText("El modelo propone. Nosotros decidimos.",
  {x:0.7,y:5.7,w:11.9,h:0.5,fontFace:BODY,fontSize:18,italic:true,color:TEAL,align:"center",isTextBox:true,margin:0});
footer(s,4); s.addNotes(N[4]);

// ---------- 5 · Evidencia ----------
s = p.addSlide(); s.background={color:WHITE}; title(s,"Evidencia");
const stats=[
  ["20 → 18","Referencias importadas y únicas tras deduplicar",VIOLET],
  ["9 / 4 / 5","Aprobadas, rechazadas y pendientes",TEAL],
  ["1","Cita verificada contra el texto completo, con página",VIOLET],
];
stats.forEach((c,i)=>{
  const x=0.7+i*4.08;
  s.addShape(p.ShapeType.roundRect,{x,y:2.1,w:3.75,h:3.3,rectRadius:0.12,fill:{color:i===1?CARD2:CARD},line:{type:"none"}});
  s.addText(c[0],{x:x+0.2,y:2.5,w:3.35,h:1.2,fontFace:HEAD,fontSize:46,bold:true,color:c[2],align:"center",isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.3,y:3.9,w:3.15,h:1.3,fontFace:BODY,fontSize:17,color:INK,align:"center",valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.1});
});
s.addText("Separamos lo comprobado de lo que todavía es una propuesta.",
  {x:0.7,y:5.7,w:11.9,h:0.5,fontFace:BODY,fontSize:17,italic:true,color:MUTED,align:"center",isTextBox:true,margin:0});
footer(s,5); s.addNotes(N[5]);

// ---------- 6 · Límites y uso responsable ----------
s = p.addSlide(); s.background={color:WHITE}; title(s,"Límites y uso responsable");
const lim=[
  ["No sustituye","No es por sí mismo una revisión sistemática",VIOLET],
  ["Datos públicos","Solo mostramos información pública",TEAL],
  ["Siguiente paso","Sumar una tercera fuente y llevarlo al aula virtual",VIOLET],
];
lim.forEach((c,i)=>{
  const x=0.7+i*4.08;
  s.addShape(p.ShapeType.roundRect,{x,y:2.1,w:3.75,h:3.4,rectRadius:0.12,fill:{color:i===1?CARD2:CARD},line:{type:"none"}});
  s.addText(c[0],{x:x+0.3,y:2.4,w:3.15,h:0.6,fontFace:HEAD,fontSize:21,bold:true,color:c[2],isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.3,y:3.15,w:3.15,h:2.1,fontFace:BODY,fontSize:18,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.15});
});
footer(s,6); s.addNotes(N[6]);

// ---------- 7-9 · Demostración ----------
const demos=[
  [7,"Demostración: la colección","proyecto-final/capturas/captura_entrada.png","Cada referencia con su identificador, su estado y la decisión registrada",N[7]],
  [8,"Demostración: pendientes","proyecto-final/capturas/captura_resultado.png","La IA sugiere y justifica; la decisión humana queda a la persona",N[8]],
  [9,"Demostración: el historial","proyecto-final/capturas/captura_revision.png","Registro fechado de cada cambio; nada se borra",N[9]],
];
demos.forEach(([n,t,img,rot,notes])=>{
  s=p.addSlide(); s.background={color:WHITE}; title(s,t);
  s.addImage({path:img,x:1.85,y:1.5,w:9.63,h:5.0,sizing:{type:"contain",w:9.63,h:5.0}});
  s.addText(rot,{x:0.7,y:6.55,w:11.9,h:0.45,fontFace:BODY,fontSize:16,italic:true,color:MUTED,align:"center",isTextBox:true,margin:0});
  footer(s,n); s.addNotes(notes);
});

// ---------- 10 · Cierre ----------
s = p.addSlide(); s.background={color:DARK};
s.addShape(p.ShapeType.ellipse,{x:-1.5,y:-1.5,w:5,h:5,fill:{color:VIOLET,transparency:80},line:{type:"none"}});
s.addText("La decisión sigue siendo humana",
  {x:0.8,y:2.2,w:11.5,h:1.2,fontFace:HEAD,fontSize:38,bold:true,color:WHITE,isTextBox:true,margin:0});
s.addText("La revisión deja de envejecer sin control y el trabajo manual se reduce",
  {x:0.8,y:3.5,w:11.0,h:0.8,fontFace:BODY,fontSize:20,italic:true,color:GOLD,isTextBox:true,margin:0,lineSpacingMultiple:1.1});
s.addText([
  {text:"github.com/srbenitez/revision-viva-rag-demo",options:{breakLine:true,color:"CADCFC"}},
  {text:"Marcelo Carrera · UTE    ·    Segundo Benítez · UTPL",options:{color:WHITE}},
],{x:0.8,y:4.8,w:11.5,h:1.2,fontFace:BODY,fontSize:18,lineSpacingMultiple:1.3,isTextBox:true,margin:0});
s.addNotes(N[10]);

p.writeFile({ fileName: "proyecto-final/VC-2026-028-NNN_ProyectoFinal_ES.pptx" })
 .then(f=>console.log("OK:",f));
