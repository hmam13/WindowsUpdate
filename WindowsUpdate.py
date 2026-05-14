#!/usr/bin/env python3

"""
Nombre del Script: LinuxUpdate
Autor: Hector Arango 
Github: https://github.com/hmam13
Descripcióon: Script para actualizar las aplicaciones de tu sistema Windows. 
Lenguaje: Python
Version: 1
"""

import subprocess
import sys

CONFIG = {
    
    "titulo": "Windows Update Manager",
    "mensaje_inicio": "Iniciando actualización de paquetes...",
    "comando": "winget upgrade --accept-source-agreements --accept-package-agreements --all --include-unknown --no-vt",
    "mensaje_fin": "Proceso finalizado correctamente.",
    "espera": 5
}

def update():
    
    comandos_cmd = (
        
        f"title {CONFIG['titulo']} && "
        f"echo. && "
        f"echo --- {CONFIG['titulo']} --- && "
        f"echo. && "
        f"echo {CONFIG['mensaje_inicio']} && "
        f"echo. && "
        f"{CONFIG['comando']} && "
        f"echo. && "
        f"echo {CONFIG['mensaje_fin']} && "
        f"timeout /t {CONFIG['espera']}"
    )

    ejecutar_update = f'Start-Process cmd -ArgumentList "/c {comandos_cmd}" -Verb RunAs'

    try:
        subprocess.Popen(['powershell', '-NoProfile', '-Command', ejecutar_update])
    except Exception as e:
        print(f"Error al intentar ejecutar el proceso: {e}")

if __name__ == "__main__":

    if sys.platform == "win32":
        update()
    else:
        print("Este script solo es compatible con Windows.")