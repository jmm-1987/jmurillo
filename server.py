#!/usr/bin/env python3
"""
Servidor web local simple para servir el portfolio sin errores de CORS
Uso: python server.py
Luego abre: http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Puerto del servidor
PORT = 8000

# Directorio actual
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Agregar headers para evitar problemas de CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def start_server():
    """Inicia el servidor web local"""
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"🚀 Servidor iniciado en http://localhost:{PORT}")
            print(f"📁 Sirviendo archivos desde: {DIRECTORY}")
            print("💡 Presiona Ctrl+C para detener el servidor")
            print("🌐 Abriendo navegador...")
            
            # Abrir automáticamente el navegador
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Iniciar el servidor
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido")
    except OSError as e:
        if e.errno == 98:  # Puerto ya en uso
            print(f"❌ Error: El puerto {PORT} ya está en uso")
            print("💡 Intenta con un puerto diferente o cierra otras aplicaciones que usen ese puerto")
        else:
            print(f"❌ Error al iniciar el servidor: {e}")

if __name__ == "__main__":
    start_server()
