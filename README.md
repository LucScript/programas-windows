# programas-windows
# 🪟 Colección de Programas para Windows

Colección oficial de mis scripts en Python para la optimización avanzada, limpieza de recursos y automatización de tareas en Windows.

---

## 📁 Sección: Optimización del Sistema

* **`mantenimiento_windows.py`**: Panel de control con 6 utilidades principales:
  * **Opción 1:** Limpieza de caché y liberación de RAM mediante PowerShell.
  * **Opción 2:** Optimización general y borrado de temporales del sistema.
  * **Opción 3:** Actualización masiva de aplicaciones mediante `winget`.
  * **Opción 4:** Visualización del espacio en disco (libre y total).
  * **Opción 5:** Acceso rápido al Administrador de Tareas.
  * **Opción 6:** Test de velocidad de conexión a internet.

### 🛠️ Requisitos

* **General:** Tener **Python** instalado.
* **Exclusivo para la Opción 6:** Instalar el cliente CLI de Ookla desde la terminal:
  ```cmd
  winget install -e --id Ookla.Speedtest.CLI
  ```

### 🚀 Ejecución
Abre la terminal como **Administrador** en la carpeta del script y ejecuta:
```cmd
python mantenimiento_windows.py
```

---
*Desarrollado por **LucScript** 🪟🔥*
