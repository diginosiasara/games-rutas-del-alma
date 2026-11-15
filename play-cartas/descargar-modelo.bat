@echo off
rem Descarga un modelo DENTRO del paquete:  descargar-modelo.bat llama3.2:3b
cd /d "%~dp0"
if "%1"=="" ( echo Uso: descargar-modelo.bat ^<modelo^>  p. ej. llama3.2:3b & exit /b 1 )
set OLLAMA_MODELS=%CD%\modelos-ia\ollama
set OLLAMA_HOST=127.0.0.1:11435
set OLLAMA_ORIGINS=*
start "Motor IA del paquete" /min ollama serve
timeout /t 3 >nul
ollama pull %1
