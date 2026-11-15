#!/usr/bin/env bash
# Arranca el motor de IA del PAQUETE (Ollama con los modelos de ./modelos-ia/ollama) y el juego en local.
cd "$(dirname "$0")" || exit 1
export OLLAMA_MODELS="$PWD/modelos-ia/ollama"      # los modelos viven dentro del proyecto
export OLLAMA_HOST="127.0.0.1:11435"               # puerto propio: no choca con un Ollama ya instalado (11434)
export OLLAMA_ORIGINS="*"                          # permite que la página local hable con el motor
if command -v ollama >/dev/null 2>&1; then
  if ! curl -s "http://$OLLAMA_HOST/api/tags" >/dev/null 2>&1; then ollama serve >/dev/null 2>&1 & sleep 2; fi
  echo "Motor del paquete en http://$OLLAMA_HOST"
else
  echo "Ollama no está instalado (https://ollama.com). El juego funcionará, pero sin el paquete de IA local."
fi
( sleep 1; (xdg-open "http://localhost:8765/01_juego/rutas-del-alma-prototipo.html" || open "http://localhost:8765/01_juego/rutas-del-alma-prototipo.html") >/dev/null 2>&1 ) &
python3 servir.py 8765
