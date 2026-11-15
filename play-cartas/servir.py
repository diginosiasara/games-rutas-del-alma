#!/usr/bin/env python3
"""Servidor estático local para el juego (necesario para que la página lea modelos-ia/manifest.json).
Uso: python3 servir.py [puerto]   ->  http://localhost:8765/01_juego/rutas-del-alma-prototipo.html"""
import sys,os
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
class H(SimpleHTTPRequestHandler):
    def end_headers(self):self.send_header('Cache-Control','no-store');super().end_headers()
    def log_message(self,*a):pass
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p=int(sys.argv[1]) if len(sys.argv)>1 else 8765
print(f'Juego en http://localhost:{p}/01_juego/rutas-del-alma-prototipo.html  (Ctrl+C para parar)')
ThreadingHTTPServer(('127.0.0.1',p),H).serve_forever()
