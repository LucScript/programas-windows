import os
import sys

def lucscript_windowscleaner():
    print("🧹 -- LUCSCRIPT WINDOWS CLEANER -- 🧹\n\n1. Limpiar caché\n2. Optimización total\n3. Actualizar el sistema\n4. Espacio en disco\n5.Gestión de procesos en segundo plano\n6. Revisar velocidad de conexión")
    option = input("Escribe el número de la opción: ")

    if option == "1":
        print("Borrando la memoria caché del sistema...")
        os.system('powershell "[System.GC]::Collect()"')
    elif option == "2":
        print("Eliminando paquetes obsoletos y limpiando el disco...")
        os.system("cleanmgr /sagerun:1")
    elif option == "3":
        print("Actualizando el sistema...")
        os.system("winget upgrade --all --include-unknown")
    elif option == "4":
        print("Calculando el espacio libre en el disco...")
        os.system('powershell "Get-Volume | Format-Table -Property DriveLetter, FriendlyName, SizeRemaining, Size"')
    elif option == "5":
        print("Cargando programas en segundo plano...")
        os.system("taskmgr")
    elif option == "6":
        print("🌐 Iniciando test de velocidad de internet...")
        print("Conectando con el servidor más cercano (esto puede tardar unos segundos)...")
        os.system("speedtest")
    else:
        print("Opción seleccionada no válida")
lucscript_windowscleaner()