#!/usr/bin/env python3
"""
Monta un video del proyecto final: une cada diapositiva (PNG) con su narración
(MP3) y produce un MP4 1920x1080, H.264 yuv420p, AAC, faststart.

Cada diapositiva dura lo que su audio más un margen (gap). Si el total queda
por debajo de 4:30, el gap se aumenta automáticamente para alcanzar el mínimo.
El CRF se ajusta hasta que el archivo pese menos de 25 MB.

Uso:
    python3 make_video.py ES   # usa video/es_slides + audio/ES_01..ES_10.mp3
    python3 make_video.py EN   # usa video/en_slides + audio/EN_01..EN_10.mp3
"""
import subprocess, sys, os, json, tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
LANG = (sys.argv[1] if len(sys.argv) > 1 else "ES").upper()
SLIDES = RAIZ / "video" / ("es_slides" if LANG == "ES" else "en_slides")
AUDIO = RAIZ / "audio"
OUTBASE = RAIZ / f"VC-2026-028-NNN_ProyectoFinal_{LANG}"
MIN_TOTAL = 273.0   # objetivo mínimo (4:33) para no rozar el límite de 4:30
MAX_MB = 24.5

def dur(path):
    out = subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","default=noprint_wrappers=1:nokey=1", str(path)])
    return float(out.strip())

def main():
    audios = [AUDIO / f"{LANG}_{i:02d}.mp3" for i in range(1, 11)]
    slides = [SLIDES / f"slide-{i:02d}.png" for i in range(1, 11)]
    for p in audios + slides:
        if not p.exists():
            sys.exit(f"Falta: {p}")
    durs = [dur(a) for a in audios]
    speech_total = sum(durs)
    base_gap = 1.0
    # si queda corto, repartir el faltante como gap extra entre las 10 diapositivas
    total_with_gap = speech_total + base_gap * len(durs)
    if total_with_gap < MIN_TOTAL:
        extra = (MIN_TOTAL - total_with_gap) / len(durs)
        gap = base_gap + extra
    else:
        gap = base_gap
    seg_durs = [d + gap for d in durs]
    total = sum(seg_durs)
    print(f"{LANG}: narración {speech_total:.1f}s, gap {gap:.2f}s/diap, total {total:.1f}s ({int(total//60)}:{int(total%60):02d})")

    tmp = Path(tempfile.mkdtemp())
    segs = []
    for i,(sl,au,sd) in enumerate(zip(slides,audios,seg_durs),1):
        seg = tmp / f"seg{i:02d}.mp4"
        # imagen fija extendida a sd; audio con pad de silencio hasta sd
        subprocess.check_call(["ffmpeg","-y","-loglevel","error",
            "-loop","1","-i",str(sl),
            "-i",str(au),
            "-filter_complex", f"[1:a]apad=whole_dur={sd}[a]",
            "-map","0:v","-map","[a]",
            "-c:v","libx264","-tune","stillimage","-pix_fmt","yuv420p","-r","30",
            "-t",f"{sd}","-c:a","aac","-b:a","128k","-shortest", str(seg)])
        segs.append(seg)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{s}'\n" for s in segs))

    for crf in (26,28,30,32):
        out = f"{OUTBASE}.mp4"
        subprocess.check_call(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0",
            "-i",str(lst),"-c:v","libx264","-crf",str(crf),"-pix_fmt","yuv420p",
            "-movflags","+faststart","-c:a","aac","-b:a","128k", out])
        mb = os.path.getsize(out)/1e6
        print(f"  CRF {crf}: {mb:.1f} MB")
        if mb <= MAX_MB:
            break
    print(f"OK -> {out} ({int(total//60)}:{int(total%60):02d}, {mb:.1f} MB)")

if __name__ == "__main__":
    main()
