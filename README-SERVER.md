# Servidor Local para Portfolio

## Problema de CORS
Cuando abres el archivo `index.html` directamente desde el explorador de archivos (protocolo `file://`), el navegador bloquea el acceso al `manifest.json` por políticas de seguridad CORS.

## Solución 1: Usar el servidor local incluido

### Opción A: Usar el archivo batch (Windows)
1. Haz doble clic en `start-server.bat`
2. El servidor se iniciará automáticamente en `http://localhost:8000`
3. El navegador se abrirá automáticamente

### Opción B: Usar Python directamente
1. Abre una terminal/cmd en la carpeta del proyecto
2. Ejecuta: `python server.py`
3. Abre tu navegador en `http://localhost:8000`

## Solución 2: Otros servidores locales

### Con Node.js (si tienes npm instalado)
```bash
npx serve .
```

### Con PHP
```bash
php -S localhost:8000
```

### Con Live Server (VS Code)
Si usas Visual Studio Code, instala la extensión "Live Server" y haz clic derecho en `index.html` > "Open with Live Server"

## Ventajas del servidor local
- ✅ Sin errores de CORS
- ✅ El manifest.json funciona correctamente
- ✅ Mejor experiencia de desarrollo
- ✅ Comportamiento idéntico al de producción
- ✅ PWA (Progressive Web App) funciona correctamente

## Detener el servidor
Presiona `Ctrl+C` en la terminal donde está corriendo el servidor.
