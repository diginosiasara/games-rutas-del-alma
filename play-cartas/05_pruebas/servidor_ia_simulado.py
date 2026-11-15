#!/usr/bin/env python3
"""Servidor de IA SIMULADO para probar el configurador del juego sin descargar modelos.
Imita la API de Ollama (/api/tags, /api/chat en NDJSON) y la de OpenAI/LM Studio (/v1/models, /v1/chat/completions en SSE).
Uso:  python3 servidor_ia_simulado.py ollama:11435:llama3.2:3b  ollama:11434:mistral  openai:1234:mock-lm
      (tipo:puerto:modelo[,modelo2])  -> Ctrl+C para parar. NO es un modelo: solo devuelve una respuesta de prueba."""
import json,sys,threading,time
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
STYLES={'Vas al grano':'concisa','tono poético':'poetica','humor suave':'ludica','profesora de reglas':'maestra','tono de fábula':'clasica'}
LENS={'1 o 2 frases':'corta','máximo de 4 frases':'media','hasta 8 frases':'larga'}
def make(kind,models):
    class H(BaseHTTPRequestHandler):
        def log_message(self,*a):pass
        def _cors(self):
            self.send_header('Access-Control-Allow-Origin','*');self.send_header('Access-Control-Allow-Headers','*');self.send_header('Access-Control-Allow-Methods','GET,POST,OPTIONS');self.send_header('Access-Control-Allow-Private-Network','true')
        def do_OPTIONS(self):self.send_response(204);self._cors();self.end_headers()
        def do_GET(self):
            if kind=='ollama' and self.path=='/api/tags':body={'models':[{'name':m} for m in models]}
            elif kind=='openai' and self.path in('/v1/models','/models'):body={'data':[{'id':m} for m in models]}
            else:self.send_response(404);self._cors();self.end_headers();return
            b=json.dumps(body).encode();self.send_response(200);self._cors();self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
        def do_POST(self):
            n=int(self.headers.get('Content-Length') or 0);req=json.loads(self.rfile.read(n) or b'{}')
            msgs=req.get('messages',[]);sysm=next((m['content'] for m in msgs if m['role']=='system'),'');user=msgs[-1]['content'] if msgs else ''
            st=next((v for k,v in STYLES.items() if k in sysm),'?');ln=next((v for k,v in LENS.items() if k in sysm),'?')
            txt=f"[sim-{kind}:{req.get('model')}] estilo={st} longitud={ln} estado={'si' if 'Estado actual' in sysm else 'no'} historial={max(0,len(msgs)-2)} :: respuesta de prueba a «{user[-40:]}»."
            words=txt.split(' ');self.send_response(200);self._cors()
            if kind=='ollama':
                self.send_header('Content-Type','application/x-ndjson');self.end_headers()
                for w in words:self.wfile.write((json.dumps({'model':req.get('model'),'message':{'role':'assistant','content':w+' '},'done':False})+'\n').encode());self.wfile.flush();time.sleep(.005)
                self.wfile.write((json.dumps({'done':True})+'\n').encode())
            else:
                self.send_header('Content-Type','text/event-stream');self.end_headers()
                for w in words:self.wfile.write(('data: '+json.dumps({'choices':[{'delta':{'content':w+' '}}]})+'\n\n').encode());self.wfile.flush();time.sleep(.005)
                self.wfile.write(b'data: [DONE]\n\n')
    return H
def serve(spec):
    kind,port,ms=spec.split(':',2);s=ThreadingHTTPServer(('127.0.0.1',int(port)),make(kind,ms.split(',')));s.serve_forever()
if __name__=='__main__':
    for sp in sys.argv[1:]:threading.Thread(target=serve,args=(sp,),daemon=True).start();print('escuchando',sp)
    try:
        while True:time.sleep(3600)
    except KeyboardInterrupt:pass
