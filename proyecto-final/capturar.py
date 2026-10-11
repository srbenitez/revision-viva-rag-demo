#!/usr/bin/env python3
"""Captura las tres pestañas del visor (Colección, Pendientes, Historial) en 16:9."""
import time, http.server, socketserver, threading, os
from pathlib import Path
from playwright.sync_api import sync_playwright

RAIZ = Path("/home/claude/revision-viva-rag-demo")
OUT = RAIZ / "proyecto-final" / "capturas"
OUT.mkdir(parents=True, exist_ok=True)
os.chdir(RAIZ)

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("127.0.0.1", 8913), http.server.SimpleHTTPRequestHandler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
time.sleep(1)

tabs = [
    ("coleccion", "captura_entrada.png"),
    ("pendientes", "captura_resultado.png"),
    ("historial", "captura_revision.png"),
]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1366,"height":768}, device_scale_factor=2)
    pg.goto("http://127.0.0.1:8913/index.html")
    pg.wait_for_selector('nav button[data-panel="coleccion"]', timeout=15000)
    pg.wait_for_timeout(1200)
    for panel, fname in tabs:
        pg.click(f'nav button[data-panel="{panel}"]')
        pg.wait_for_timeout(700)
        pg.screenshot(path=str(OUT/fname))
        print("guardada:", fname)
    b.close()
httpd.shutdown()
print("OK ->", OUT)
