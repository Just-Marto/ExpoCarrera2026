@echo off
echo ============================================
echo   UniDemo - Expo Ciberseguridad 2026
echo ============================================
echo.

:: Verificar que Python existe
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no encontrado. Instalar Python 3 primero.
    pause
    exit /b 1
)

:: Crear venv si no existe
if not exist "venv\" (
    echo [*] Creando entorno virtual...
    python -m venv venv
)

:: Instalar dependencias
echo [*] Verificando dependencias...
venv\Scripts\pip.exe install -q -r requirements.txt

:: Arrancar servidor
echo.
echo [OK] Servidor arrancando en http://localhost:5000
echo [OK] Abri esa URL en el navegador.
echo [OK] Para parar: Ctrl+C
echo.
venv\Scripts\python.exe run.py
