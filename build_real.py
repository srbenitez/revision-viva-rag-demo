#!/usr/bin/env python3
"""
Ingesta de los lotes REALES (Scopus + Google Academico) ejecutados el 2026-10-11.

- Normaliza ambas fuentes a un esquema comun.
- Deduplica en codigo: DOI normalizado y, sin DOI, titulo normalizado + mismo anio
  (regla de titulo parecido, umbral 0.90).
- Reconstruye coleccion.csv (registro unico, estado=pendiente) y pendientes.csv
  (hoja de cribado con sugerencia de IA; sin resumen -> evidencia insuficiente).
- Deja lotes normalizados fechados y anota el historial.

El resumen de Scopus se guarda PARAFRASEADO y corto (no el abstract del editor),
porque la vitrina es publica. El abstract completo del editor queda solo en el
export crudo (lote_scopus_2026-10-11_raw.csv).
"""
import csv, re, difflib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
UMBRAL = 0.90

def ndoi(d):
    d = (d or "").strip().lower()
    for p in ("https://doi.org/","http://dx.doi.org/","http://doi.org/","doi:"):
        if d.startswith(p): d = d[len(p):]
    return d.strip()

def ntit(t):
    t = re.sub(r"[^\w\s]", "", (t or "").lower())
    return re.sub(r"\s+", " ", t).strip()

# --- Fuente 1: Scopus (con resumen parafraseado corto + sugerencia de pertinencia) ---
# sug: incluir / excluir segun criterio (RAG sobre documentos institucionales EN
# EDUCACION SUPERIOR, 2020+). Justificacion en palabras propias.
scopus = [
 ("S01","10.1109/ICNDSA68777.2026.11652169","A Conversational AI Agent for Campus Information Using Retrieval Augmented Generation (RAG)","2026","Goyal P.; Chaudhary A.; Bijalwan V.; Bharti M.; Dwivedi A.K.","https://www.scopus.com/pages/publications/105048474552",
   "Asistente de campus (NavIQ) con RAG sobre documentos institucionales autenticados (politicas, reglas, estructura academica) mas navegacion interior.",
   "incluir","RAG sobre documentos institucionales en un campus universitario; cumple tema, poblacion (educacion superior) y anio."),
 ("S02","10.1007/978-981-95-3358-9_33","Integrating Information Retrieval and LLMs: A Document Retrieval Chatbot in Education Settings","2026","Nguyen D.D.K.; Mach V.K.; Le Dinh T.; Pham-Nguyen C.","https://www.scopus.com/pages/publications/105020802084",
   "Chatbot universitario (UniBot) que combina recuperacion de informacion y LLM (RAG) para consultar documentos internos (politicas, anuncios, horarios).",
   "incluir","RAG sobre documentos internos de una universidad; cumple los tres criterios."),
 ("S03","10.5753/jis.2026.8133","Evaluating Incremental Context Strategy in RAG-Based Chatbots for Hospital Document Retrieval: A Trade-off Between Quality and Cost","2026","Cunha M.V.D.; Silveira M.R.; Santana B.S.; Freitas L.A.; Correa U.B.","https://www.scopus.com/pages/publications/105050415270",
   "Chatbot RAG para recuperar documentos normativos de un hospital universitario; estrategia de contexto incremental para reducir tokens.",
   "excluir","El dominio es un hospital, no educacion superior; fuera de la poblacion del criterio (revisar si se amplia a 'institucional' en general)."),
 ("S04","10.3390/app16157374","A Secure Multi-Tenant Framework for Institutional Question Answering with Tool-Calling LLMs","2026","Kim S.-E.; Geem Z.W.","https://www.scopus.com/pages/publications/105047088258",
   "Marco multiinquilino seguro para QA institucional con LLM que combina recuperacion documental y consultas SQL con guardas de seguridad (Universidad Catolica de Corea).",
   "incluir","QA institucional sobre documentos de una universidad; cumple poblacion y tema."),
 ("S05","10.2478/jcbtp-2026-0014","Offline NLP Assistants for Internal Knowledge Access in a Central Bank: Proof-of-Concept Systems for Semantic Search and HR Chatbot","2026","Hajdarevic K.; Selimovic J.","https://www.scopus.com/pages/publications/105039283881",
   "Asistentes NLP offline para acceso a conocimiento interno en un banco central: busqueda semantica y chatbot de RR.HH. con RAG.",
   "excluir","El contexto es un banco central; fuera de educacion superior."),
 ("S06","10.1109/ICKECS70176.2026.11527633","Viot: A Smart Student Assistant System Using RAG and LLM-Based Query Processing","2026","Dhanush Gowda K.R.; Dhanush Kumar V.; Lakshmi B.S.; Dhanush R.; Mahadevaprasad K.; Akshatha M.","https://www.scopus.com/pages/publications/105041791571",
   "Asistente estudiantil movil (Viot) con RAG/LLM sobre documentos institucionales (horarios, silabos, anuncios) en base vectorial.",
   "incluir","Asistente universitario sobre documentos institucionales; cumple criterios."),
 ("S07","10.1109/IT67293.2026.11435604","Design and Implementation of a RAG Chatbot System for Scientific Research Institutes","2026","Radulovic I.; Mitric J.; Kovijanic K.; Ljuka M.; Merdovic N.; Hiyari M.H.; Badnjevic A.","https://www.scopus.com/pages/publications/105035988273",
   "Chatbot RAG para un instituto de investigacion cientifica: busqueda semantica sobre base vectorial mas generacion con LLM.",
   "excluir","Instituto de investigacion, no educacion superior; revisar si la poblacion del criterio se amplia."),
 ("S08","10.1080/0952813X.2026.2729304","From policy to practice: clause-grounded answers with retrieval-augmented generation","2026","Tsai W.-L.; Huang R.-Q.","https://www.scopus.com/pages/publications/105051410059",
   "Asistente de campus con RAG que ancla respuestas en regulaciones universitarias (Azure OpenAI + Cosmos DB); 51 reglamentos, 1742 preguntas.",
   "incluir","RAG anclado en regulaciones universitarias; cumple tema y poblacion."),
 ("S09","10.14569/ijacsa.2026.0170854","Effective Chunking for Retrieval-Augmented Generation over Structured Institutional Documents","2026","Khalib S.S.I.; Rahman A.H.A.; Zakaria L.Q.","https://www.scopus.com/pages/publications/105051621273",
   "Evalua estrategias de fragmentacion (chunking) para RAG sobre documentos institucionales estructurados (tablas, aranceles) de una universidad (UKM).",
   "incluir","Documentos institucionales universitarios estructurados; cumple criterios."),
 ("S10","10.1145/3828183.3828497","Design of an Intelligent Question Answering System for Universities Integrating Knowledge Graphs and Large Language Models","2026","Zhang J.; Liu Q.","https://www.scopus.com/pages/publications/105051359975",
   "Sistema de QA universitario que integra grafos de conocimiento y LLM con verificacion de respuestas; evaluado sobre consultas estudiantiles reales.",
   "incluir","QA universitario sobre informacion institucional; cumple criterios."),
]

# --- Fuente 2: Google Academico ---
# (id, titulo, anio, autores, enlace, nota, resumen_recuperado, sugerencia, justificacion)
# resumen_recuperado: SOLO si se verifico en fuente real (arXiv / editor). Parafraseado.
# Vacio = no se pudo verificar -> queda como evidencia insuficiente.
scholar = [
 ("H01","Hybrid context retrieval augmented generation pipeline: LLM-augmented knowledge graphs and vector database for accreditation reporting assistance","2024","Edwards C.","https://arxiv.org/abs/2405.15436","",
   "Pipeline RAG que ayuda a escuelas de negocios a preparar informes de acreditacion AACSB combinando base vectorial y grafo de conocimiento con datos de los estandares y documentos institucionales; evaluado con RAGAs (verificado en arXiv 2405.15436).",
   "incluir","RAG sobre documentos institucionales universitarios para acreditacion; cumple tema y poblacion (educacion superior)."),
 ("H02","A Reliability-Aware Retrieval-Augmented Generation Architecture for Open Language Models in Higher Education Decision Support","2026","Garcia-Lopez I.M.; Guillen-Yparrea N.","https://www.mdpi.com/2073-431X/15/9/564","",
   "Arquitectura RAG gobernada para modelos abiertos en apoyo a decisiones universitarias (interpretacion de politicas, asesoria, resumenes): ingesta documental, recuperacion hibrida, reranking, generacion con evidencia, rechazo por confianza y revision humana; define un indice de fiabilidad de siete dimensiones (verificado en MDPI Computers 15(9):564).",
   "incluir","RAG para soporte de decisiones en educacion superior; cumple los tres criterios."),
 ("H03","Enhancing scientific communication and institutional identity through a retrieval-augmented generation digital personal tutor","2026","Di Tore S. et al.","https://www.mdpi.com/2079-9292/15/4/847","",
   "Tutor personal digital con RAG anclado en una base curada para un museo de ciencia (Citta della Scienza, Napoles), con avatar, voz y animacion; busca comunicacion inclusiva y multilingue (verificado en MDPI Electronics 15(4):847).",
   "excluir","El entorno es un museo de ciencia, no educacion superior; fuera de la poblacion del criterio aunque lo desarrolle una universidad."),
 ("H04","Optimizing and evaluating a retrieval-augmented generation system for normative document retrieval in hospital settings","2025","da Cunha M.V. et al.","","posible relacion con S03 (mismos autores, hospital): revisar si es version previa; ademas hospital, fuera de criterio.",
   "","",""),
 ("H05","DisastRAG: A Multi-Source Disaster Information Integration and Access System Based on Retrieval-Augmented Large Language Models","2026","Li B. et al.","","identificador arXiv del export (2605.05210) no verificado; tema de desastres, probablemente fuera del criterio; localizar la fuente.",
   "","",""),
 ("H06","From policy to practice: clause-grounded answers with retrieval-augmented generation","2026","Tsai W.L.; Huang R.Q.","","",
   "","",""),
 ("H07","Effective Chunking for Retrieval-Augmented Generation over Structured Institutional Documents","2026","Khalib S.S.I. et al.","","",
   "","",""),
 ("H08","Retrieval-Augmented Generative Indonesian Question Answering for Campus Planning Documents: A Case Study at Vocational School Universitas Sebelas Maret","2026","Khadija M.A. et al.","","resumen no localizado; tema (documentos de planificacion de campus) en criterio aparente: localizar la fuente para cribar.",
   "","",""),
 ("H09","OCR-integrated retrieval-augmented generation for PDF-document question answering system in vocational higher education","2026","Khadija M.A. et al.","","resumen no localizado; tema (QA sobre PDF en educacion superior tecnica) en criterio aparente: localizar la fuente para cribar.",
   "","",""),
 ("H10","Reimagining Academic Library Services through Local RAG: Concepts and Frameworks","2025","Pal P.K.","","resumen no localizado: localizar la fuente para cribar.",
   "","",""),
]

# --- Deduplicacion en codigo ---
uniq = []          # registros unicos (dicts)
dups = []          # (scholar_id, scopus_id_match, ratio)
# base: Scopus ya es unico entre si
for s in scopus:
    uniq.append({"id_ref":s[0],"doi":s[1],"titulo":s[2],"anio":s[3],"autores":s[4],
                 "enlace":s[5],"resumen":s[6],"sugerencia":s[7],"justificacion":s[8],
                 "fuente":"scopus","nota":""})
# scholar contra lo ya unico
for h in scholar:
    hid,tit,anio,aut,enl,nota,res,sug,just = h
    match = None
    for u in uniq:
        if u["anio"]==anio:
            r = difflib.SequenceMatcher(None, ntit(tit), ntit(u["titulo"])).ratio()
            if r >= UMBRAL:
                match = (u["id_ref"], round(r,2)); break
    if match:
        dups.append((hid, match[0], match[1]))
        continue
    uniq.append({"id_ref":hid,"doi":"","titulo":tit,"anio":anio,"autores":aut,
                 "enlace":enl,"resumen":res,"sugerencia":sug,"justificacion":just,
                 "fuente":"scholar","nota":nota})

# --- coleccion.csv (registro unico, estado pendiente) ---
with (RAIZ/"coleccion.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.writer(f)
    w.writerow(["id_ref","doi","titulo","anio","autores","enlace","resumen","estado","fecha_decision","revisor","motivo","fuente"])
    for u in uniq:
        w.writerow([u["id_ref"],u["doi"],u["titulo"],u["anio"],u["autores"],u["enlace"],u["resumen"],"pendiente","","","",u["fuente"]])

# --- pendientes.csv (hoja de cribado) ---
with (RAIZ/"pendientes.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.writer(f)
    w.writerow(["id_ref","doi","titulo","anio","autores","enlace","resumen","sugerencia_ia","justificacion","decision_humana","revisor","fecha","nota"])
    for u in uniq:
        if u["resumen"]:
            w.writerow([u["id_ref"],u["doi"],u["titulo"],u["anio"],u["autores"],u["enlace"],u["resumen"],u["sugerencia"],u["justificacion"],"","","",u["nota"]])
        else:
            nota = "evidencia insuficiente: sin resumen exportado (Google Academico); no evaluar pertinencia ni inventar hallazgos"
            if not u["enlace"]: nota += "; sin DOI ni enlace estable: localizar la fuente"
            if u["nota"]: nota += "; "+u["nota"]
            w.writerow([u["id_ref"],u["doi"],u["titulo"],u["anio"],u["autores"],u["enlace"],"","","","","","",nota])

# --- lotes normalizados fechados ---
with (RAIZ/"lotes"/"lote_scopus_2026-10-11.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["id_ref","doi","titulo","anio","autores","enlace","resumen"])
    for s in scopus: w.writerow([s[0],s[1],s[2],s[3],s[4],s[5],s[6]])
with (RAIZ/"lotes"/"lote_scholar_2026-10-11.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["id_ref","doi","titulo","anio","autores","enlace","resumen"])
    for h in scholar: w.writerow([h[0],"",h[1],h[2],h[3],h[4],""])

# --- resumen por consola ---
inc = sum(1 for u in uniq if u["sugerencia"]=="incluir")
exc = sum(1 for u in uniq if u["sugerencia"]=="excluir")
ins = sum(1 for u in uniq if not u["resumen"])
print(f"Scopus: {len(scopus)} | Google Academico: {len(scholar)}")
print(f"Duplicados/parecidos detectados (Scholar vs Scopus): {len(dups)} -> {dups}")
print(f"Registros unicos: {len(uniq)} (scopus {sum(1 for u in uniq if u['fuente']=='scopus')}, scholar {sum(1 for u in uniq if u['fuente']=='scholar')})")
print(f"Cribado: incluir {inc}, excluir {exc}, evidencia insuficiente {ins}")
