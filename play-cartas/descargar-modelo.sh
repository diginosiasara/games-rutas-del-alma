#!/usr/bin/env bash
# Descarga un modelo DENTRO del paquete:  ./descargar-modelo.sh llama3.2:3b
cd "$(dirname "$0")" || exit 1
[ -z "$1" ] && { echo "Uso: $0 <modelo>   p. ej. llama3.2:3b (ver modelos-ia/manifest.json)"; exit 1; }
command -v ollama >/dev/null 2>&1 || { echo "Instala Ollama primero: https://ollama.com"; exit 1; }
export OLLAMA_MODELS="$PWD/modelos-ia/ollama" OLLAMA_HOST="127.0.0.1:11435" OLLAMA_ORIGINS="*"
if ! curl -s "http://$OLLAMA_HOST/api/tags" >/dev/null 2>&1; then ollama serve >/dev/null 2>&1 & sleep 2; fi
ollama pull "$1" && echo "Listo: $1 queda guardado en modelos-ia/ollama"
