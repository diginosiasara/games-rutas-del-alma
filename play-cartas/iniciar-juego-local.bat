@echo off
rem Arranca el motor de IA del PAQUETE (Ollama con los modelos de .\modelos-ia\ollama) y el juego en local.
cd /d "%~dp0"
set OLLAMA_MODELS=%CD%\modelos-ia\ollama
set OLLAMA_HOST=127.0.0.1:11435
set OLLAMA_ORIGINS=*
where ollama >nul 2>nul
if %errorlevel%==0 ( start "Motor IA del paquete" /min ollama serve ) else ( echo Ollama no esta instalado ^(https://ollama.com^). El juego funcionara sin IA local. )
start "" "http://localhost:8765/01_juego/rutas-del-alma-prototipo.html"
python servir.py 8765
