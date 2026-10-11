// Genera la presentación en inglés + imprime conteo de palabras (palabras/150*60).
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.defineLayout({ name: "W16", width: 13.333, height: 7.5 });
p.layout = "W16";

const DARK="0B1020", GOLD="FFC629", VIOLET="5B4BDB", TEAL="0D9488",
      INK="1C1A17", MUTED="6B645C", WHITE="FFFFFF", CARD="EEEFF8", CARD2="E6F2F0";
const HEAD="Georgia", BODY="Calibri";

const N = {
 1:"We present our living bibliographic review register. We are Marcelo Carrera, from Universidad U T E, and Segundo Benítez, from U T P L. It keeps a review alive without redoing it by hand.",
 2:"A bibliographic review starts ageing the day it is delivered. New studies appear every week. Searching again and removing duplicates by hand almost never happens. There is no time. Let us look at a concrete case. We bring a new batch from Scopus. An article we already had comes back in. Its D O I identifier is written as a web address. If nobody notices, it slips in twice. This ageing is silent and easy to miss. In this way the review loses trust.",
 3:"We built a living register based on guide ten of the course. A teacher or a researcher uses it. It receives batches of references with title, year and abstract. It delivers three things. A collection without duplicates. A pending list with a relevance suggestion. And a synthesis with checked citations. Everything stays in simple text files that anyone can open and review. The reviewer stays in control at every step.",
 4:"The flow has four steps. First the person sets the question and the inclusion criteria. Second a program deduplicates in code. It compares the normalized D O I and the similar titles. This part is not decided by the model. Third the artificial intelligence suggests including or excluding each study. It always cites the abstract and gives a short reason. Fourth the person reviews and decides. The decision is signed with their name and the date. The model proposes. We decide and we keep a record. Each step leaves a trace that can be audited.",
 5:"We ran a real test with two sources. We imported twenty references. The program detected two duplicates across sources and flagged them without merging them. Eighteen unique references remained. On those we decided. Nine approved. Four rejected for being off topic. Five stayed pending for lack of an abstract. We also verified one citation against the full text, with its page. We kept the original searches with their date as well. We separate what is checked from what is still a proposal.",
 6:"Let us be clear about the limits. This register supports screening. By itself it is not a systematic review. Google Scholar does not provide abstracts. For that reason some references stay without evaluation. We protect the data. We only show public information. The next step is to add a third source and take it to the virtual classroom.",
 7:"Let us see the tool on screen. This is the collection view. The interface is in Spanish. Each row is a reference with its identifier, its title and its status. At the top there is a search box and a status filter. Here the person starts from clear criteria. The viewer changes nothing. It only shows what the register contains. From this same screen you understand what came in and from which source.",
 8:"We move to the pending list. Here is the heart of the register. For each study the artificial intelligence proposes including or excluding. And it writes a justification that cites the abstract. When a reference has no abstract, the system marks it as insufficient evidence. It does not invent a verdict. Each suggestion also shows the link to the source. The human decision column stays empty. So no hidden study is approved by mistake. It is ready for the person to resolve.",
 9:"Finally the history screen. Here stays the dated record of every change. Which batch came in. Which duplicate was discarded. What was approved or rejected and who decided it. Nothing is deleted. A rejection is kept with its reason. In this way it does not reappear without warning. With this history anyone can rebuild the collection step by step. The final synthesis is exported only with the approved studies. Everything is kept in plain, dated files.",
 10:"With this register the review stops ageing out of control. The manual work of cleaning up is reduced. And the decision stays human. You can see the project on our public site. Thank you for joining us. Our colleagues can reuse it in their own work. We are Marcelo Carrera and Segundo Benítez, from U T E and U T P L.",
};

// conteo
let tot=0,ts=0;
const rng={1:[30,40],2:[80,90],3:[70,80],4:[95,105],5:[80,90],6:[55,65],7:[70,80],8:[80,90],9:[70,80],10:[55,65]};
console.log(" # Pal Rango Seg Estado");
for(let i=1;i<=10;i++){const w=N[i].split(/\s+/).length;const s=w/150*60;tot+=w;ts+=s;
  const [lo,hi]=rng[i];const e=(w>=lo&&w<=hi)?"ok":(w<lo?"CORTO":"LARGO");
  console.log(`${String(i).padStart(2)} ${String(w).padStart(3)} ${lo}-${hi} ${s.toFixed(0).padStart(3)} ${e}`);}
console.log(`Total ${tot} palabras, ${ts.toFixed(0)} s (meta 300)`);

function footer(s,n){
  s.addText("Vibe Coding CEDIA 2026 · Universidad UTE · UTPL",{x:0.7,y:7.08,w:9,h:0.3,fontFace:BODY,fontSize:9,color:MUTED,isTextBox:true,margin:0});
  s.addText(`${n} / 10`,{x:11.0,y:7.08,w:1.63,h:0.3,fontFace:BODY,fontSize:9,color:MUTED,align:"right",isTextBox:true,margin:0});
}
function title(s,t,color){s.addText(t,{x:0.7,y:0.5,w:11.9,h:0.9,fontFace:HEAD,fontSize:32,bold:true,color:color||INK,isTextBox:true,margin:0});}

// 1 Portada
let s=p.addSlide(); s.background={color:DARK};
s.addShape(p.ShapeType.ellipse,{x:9.8,y:4.3,w:5.2,h:5.2,fill:{color:GOLD,transparency:88},line:{type:"none"}});
s.addText("Continuously updated literature review",{x:0.8,y:1.6,w:11.0,h:1.6,fontFace:HEAD,fontSize:40,bold:true,color:WHITE,isTextBox:true,margin:0});
s.addText("It keeps a review alive without redoing it by hand",{x:0.8,y:3.3,w:10.5,h:0.6,fontFace:BODY,fontSize:20,italic:true,color:GOLD,isTextBox:true,margin:0});
s.addText([{text:"Marcelo Carrera  ·  Universidad UTE",options:{breakLine:true}},{text:"Segundo Benítez  ·  UTPL",options:{breakLine:true}},{text:"Guide 10 · Vibe Coding CEDIA 2026",options:{color:"AEB4C7"}}],{x:0.8,y:4.5,w:10,h:1.4,fontFace:BODY,fontSize:18,color:WHITE,lineSpacingMultiple:1.2,isTextBox:true,margin:0});
s.addText("Narration generated with A I voice (ElevenLabs) and reviewed by the authors",{x:0.8,y:6.7,w:11.5,h:0.4,fontFace:BODY,fontSize:12,color:"AEB4C7",isTextBox:true,margin:0});
s.addNotes(N[1]);

// 2 Problem
s=p.addSlide(); s.background={color:WHITE}; title(s,"The problem");
s.addText("A review starts ageing the day it is delivered. Searching and cleaning by hand rarely happens.",{x:0.7,y:1.6,w:7.0,h:2.2,fontFace:BODY,fontSize:22,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.15});
s.addShape(p.ShapeType.roundRect,{x:8.1,y:1.7,w:4.5,h:3.6,rectRadius:0.12,fill:{color:CARD},line:{type:"none"}});
s.addText("2×",{x:8.1,y:2.0,w:4.5,h:1.4,fontFace:HEAD,fontSize:66,bold:true,color:VIOLET,align:"center",isTextBox:true,margin:0});
s.addText("The same article slips in twice when the D O I comes as a web address",{x:8.4,y:3.5,w:3.9,h:1.6,fontFace:BODY,fontSize:18,color:INK,align:"center",valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.1});
footer(s,2); s.addNotes(N[2]);

// 3 The tool
s=p.addSlide(); s.background={color:WHITE}; title(s,"The tool");
[["Receive","Batches of references with title, year and abstract",VIOLET],["Process","Deduplicates in code and the AI suggests relevance",TEAL],["Deliver","Collection, pending list and a checked synthesis",VIOLET]].forEach((c,i)=>{
  const x=0.7+i*4.08;
  s.addShape(p.ShapeType.roundRect,{x,y:2.1,w:3.75,h:3.4,rectRadius:0.12,fill:{color:i===1?CARD2:CARD},line:{type:"none"}});
  s.addText(c[0],{x:x+0.3,y:2.4,w:3.15,h:0.6,fontFace:HEAD,fontSize:22,bold:true,color:c[2],isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.3,y:3.15,w:3.15,h:2.1,fontFace:BODY,fontSize:18,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.15});});
footer(s,3); s.addNotes(N[3]);

// 4 How it works
s=p.addSlide(); s.background={color:WHITE}; title(s,"How it works");
[["1","Criteria","The person sets the question and criteria"],["2","Deduplicate","A program compares in code, not the model"],["3","The AI suggests","Proposes include or exclude and cites the abstract"],["4","Decide","The person approves and signs the decision"]].forEach((c,i)=>{
  const x=0.7+i*3.05;
  s.addShape(p.ShapeType.roundRect,{x,y:2.3,w:2.75,h:3.1,rectRadius:0.12,fill:{color:CARD},line:{type:"none"}});
  s.addShape(p.ShapeType.ellipse,{x:x+0.3,y:2.55,w:0.75,h:0.75,fill:{color:i===3?TEAL:VIOLET},line:{type:"none"}});
  s.addText(c[0],{x:x+0.3,y:2.55,w:0.75,h:0.75,fontFace:HEAD,fontSize:24,bold:true,color:WHITE,align:"center",valign:"middle",isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.28,y:3.5,w:2.25,h:0.6,fontFace:HEAD,fontSize:18,bold:true,color:INK,isTextBox:true,margin:0});
  s.addText(c[2],{x:x+0.28,y:4.1,w:2.3,h:1.2,fontFace:BODY,fontSize:16,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.1});});
s.addText("The model proposes. We decide.",{x:0.7,y:5.7,w:11.9,h:0.5,fontFace:BODY,fontSize:18,italic:true,color:TEAL,align:"center",isTextBox:true,margin:0});
footer(s,4); s.addNotes(N[4]);

// 5 Evidence
s=p.addSlide(); s.background={color:WHITE}; title(s,"Evidence");
[["20 → 18","References imported and unique after deduplicating",VIOLET],["9 / 4 / 5","Approved, rejected and pending",TEAL],["1","Citation verified against the full text, with page",VIOLET]].forEach((c,i)=>{
  const x=0.7+i*4.08;
  s.addShape(p.ShapeType.roundRect,{x,y:2.1,w:3.75,h:3.3,rectRadius:0.12,fill:{color:i===1?CARD2:CARD},line:{type:"none"}});
  s.addText(c[0],{x:x+0.2,y:2.5,w:3.35,h:1.2,fontFace:HEAD,fontSize:46,bold:true,color:c[2],align:"center",isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.3,y:3.9,w:3.15,h:1.3,fontFace:BODY,fontSize:17,color:INK,align:"center",valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.1});});
s.addText("We separate what is checked from what is still a proposal.",{x:0.7,y:5.7,w:11.9,h:0.5,fontFace:BODY,fontSize:17,italic:true,color:MUTED,align:"center",isTextBox:true,margin:0});
footer(s,5); s.addNotes(N[5]);

// 6 Limits
s=p.addSlide(); s.background={color:WHITE}; title(s,"Limits and responsible use");
[["Not a substitute","By itself it is not a systematic review",VIOLET],["Public data","We only show public information",TEAL],["Next step","Add a third source and take it to the virtual classroom",VIOLET]].forEach((c,i)=>{
  const x=0.7+i*4.08;
  s.addShape(p.ShapeType.roundRect,{x,y:2.1,w:3.75,h:3.4,rectRadius:0.12,fill:{color:i===1?CARD2:CARD},line:{type:"none"}});
  s.addText(c[0],{x:x+0.3,y:2.4,w:3.15,h:0.6,fontFace:HEAD,fontSize:21,bold:true,color:c[2],isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.3,y:3.15,w:3.15,h:2.1,fontFace:BODY,fontSize:18,color:INK,valign:"top",isTextBox:true,margin:0,lineSpacingMultiple:1.15});});
footer(s,6); s.addNotes(N[6]);

// 7-9 Demo
[[7,"Demo: the collection","proyecto-final/capturas/captura_entrada.png","Each reference with its status and the recorded decision",N[7]],
 [8,"Demo: pending list","proyecto-final/capturas/captura_resultado.png","The A I suggests and justifies; the human decision stays with the person",N[8]],
 [9,"Demo: the history","proyecto-final/capturas/captura_revision.png","A dated record of every change; nothing is deleted",N[9]]].forEach(([n,t,img,rot,notes])=>{
  s=p.addSlide(); s.background={color:WHITE}; title(s,t);
  s.addImage({path:img,x:1.85,y:1.5,w:9.63,h:5.0,sizing:{type:"contain",w:9.63,h:5.0}});
  s.addText(rot,{x:0.7,y:6.55,w:11.9,h:0.45,fontFace:BODY,fontSize:16,italic:true,color:MUTED,align:"center",isTextBox:true,margin:0});
  footer(s,n); s.addNotes(notes);});

// 10 Close
s=p.addSlide(); s.background={color:DARK};
s.addShape(p.ShapeType.ellipse,{x:-1.5,y:-1.5,w:5,h:5,fill:{color:VIOLET,transparency:80},line:{type:"none"}});
s.addText("The decision stays human",{x:0.8,y:2.2,w:11.5,h:1.2,fontFace:HEAD,fontSize:38,bold:true,color:WHITE,isTextBox:true,margin:0});
s.addText("The review stops ageing out of control and the manual work is reduced",{x:0.8,y:3.5,w:11.0,h:0.8,fontFace:BODY,fontSize:20,italic:true,color:GOLD,isTextBox:true,margin:0,lineSpacingMultiple:1.1});
s.addText([{text:"github.com/srbenitez/revision-viva-rag-demo",options:{breakLine:true,color:"CADCFC"}},{text:"Marcelo Carrera · UTE    ·    Segundo Benítez · UTPL",options:{color:WHITE}}],{x:0.8,y:4.8,w:11.5,h:1.2,fontFace:BODY,fontSize:18,lineSpacingMultiple:1.3,isTextBox:true,margin:0});
s.addNotes(N[10]);

p.writeFile({fileName:"proyecto-final/VC-2026-028-NNN_ProyectoFinal_EN.pptx"}).then(f=>console.log("OK:",f));
