# Agenda Algorítmica — Equipo 404

**Optimización de búsqueda, ordenamiento y control de duplicados mediante Divide y Vencerás**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/es/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![Paradigma](https://img.shields.io/badge/Paradigma-Divide_y_Vencerás-1e3a8a?style=flat-square)](#)

*Proyecto desarrollado para la asignatura **Seminario de Integración de Desarrollo** — Centro Universitario de Ciencias Exactas e Ingenierías (CUCEI).*

---

## Integrantes del Equipo

* **Bryhan Francisco García Espinoza**
* **Emmanuel Alejandro Ortiz Segura**
* **Roberto Hernández Zuñiga**

---

## Planteamiento del Problema

En negocios pequeños, consultorios, grupos escolares y aplicaciones administrativas sencillas, los registros de contactos (**nombre, teléfono y correo electrónico**) suelen almacenarse en estructuras lineales sin ningún criterio de ordenamiento.

Cuando el volumen de registros crece a cientos o miles de entradas, surgen tres problemas principales:

* **Consultas lineales lentas:** Localizar un contacto requiere inspeccionar la lista elemento por elemento; en el peor caso, se recorre toda la estructura con una complejidad temporal de $O(n)$.
* **Inserciones costosas y duplicidad de datos:** Para evitar registros repetidos al dar de alta un contacto, los sistemas básicos vuelven a recorrer toda la lista. Cuando esta validación se omite o falla, la agenda acumula registros duplicados.
* **Ausencia de evidencia empírica:** Las aplicaciones comerciales ocultan su funcionamiento interno y los desarrollos académicos básicos rara vez miden cuantitativamente la mejora de rendimiento al cambiar de paradigma algorítmico.

---

## Objetivo del Proyecto

Desarrollar una aplicación web interactiva autocontenida en **HTML5, CSS3 y JavaScript (Vanilla)** que, mediante la implementación de **Merge Sort** y **Búsqueda Binaria**, mantenga los registros ordenados y libres de duplicados, reduciendo significativamente el número de comparaciones y el tiempo de ejecución frente a la búsqueda secuencial, validando los resultados mediante pruebas empíricas con lotes de **1,000**, **10,000** y **100,000** contactos.

---

## Arquitectura y Comparativa Algorítmica

El sistema permite alternar en tiempo real entre dos modos de operación en memoria para medir su comportamiento, conteo exacto de operaciones y tiempos de ejecución mediante la API `performance.now()`:

```text
[ MODO BASE ]               Lista desordenada ──► Búsqueda Secuencial ──► O(n) comparaciones
[ DIVIDE Y VENCERÁS ]       Merge Sort O(n log n) ──► Lista Ordenada ──► Búsqueda Binaria (Lower Bound) O(log n)
```

### Algoritmos Implementados

1. **Búsqueda Secuencial por Prefijo — $O(n)$:**
   Recorre linealmente la colección en orden de inserción evaluando cada contacto uno por uno hasta encontrar todas las coincidencias que inicien con la cadena consultada.

2. **Merge Sort — $O(n \log n)$:**
   Algoritmo recursivo basado en el paradigma *Divide y Vencerás*. Utiliza un arreglo auxiliar para ordenar alfabéticamente los contactos mediante una clave normalizada (sin acentos ni distinción entre mayúsculas y minúsculas) y contabiliza el total exacto de comparaciones realizadas.

3. **Búsqueda Binaria (Cota Inferior / Lower Bound) — $O(\log n)$:**
   Localiza la primera aparición de un prefijo dividiendo el intervalo de búsqueda a la mitad en cada iteración, recolectando posteriormente los registros contiguos que coinciden con el criterio.

4. **Inserción Ordenada y Control de Duplicados:**
   * **Detección de duplicados en $O(1)$:** Emplea una estructura `Set` indexada por número telefónico para rechazar registros repetidos de forma inmediata.
   * **Inserción incremental:** Utiliza búsqueda binaria para determinar el índice exacto de inserción ($O(\log n)$) sin necesidad de ejecutar nuevamente *Merge Sort* tras cada alta individual.

---

## Características Técnicas

* **Carrera de Algoritmos (Benchmarking):** Ejecuta de forma comparativa la búsqueda secuencial y la búsqueda binaria sobre el mismo conjunto de datos, presentando gráficas de barras proporcionales, el costo computacional de *Merge Sort* y el **punto de equilibrio** (número mínimo de búsquedas necesarias para amortizar el costo inicial de ordenamiento).
* **Trazabilidad de Búsqueda Binaria:** Visualiza cada iteración del algoritmo mostrando los límites del subarreglo activo $[lo, hi)$, el índice central (`mid`) y la dirección de descarte.
* **Generación de Datos Sintéticos:** Permite poblar la memoria con lotes de **1,000**, **10,000** o **100,000** contactos únicos para realizar pruebas de estrés y escalabilidad.
* **Persistencia en Archivo Plano (`contactos.txt`):**
  * **Vinculación directa:** Integración con la *File System Access API* (disponible en navegadores basados en Chromium como Google Chrome y Microsoft Edge) para leer y anexar nuevos registros directamente sobre un archivo local.
  * **Compatibilidad universal:** Funciones de importación y descarga de archivos `.txt` para cualquier navegador.
  * **Estructura de almacenamiento:** Texto plano delimitado por barras verticales (`nombre|telefono|correo`).
* **Optimización del DOM:** Implementa paginación visual limitada a 100 nodos simultáneos en pantalla para mantener la fluidez de la interfaz al procesar 100,000 registros en memoria.

---

## Estructura del Proyecto

```text
agenda-algoritmica/
├── index.html      # Aplicación autocontenida (estructura, estilos y lógica algorítmica)
├── contactos.txt   # Archivo de datos de ejemplo en formato delimitado
└── README.md       # Documentación técnica del proyecto
```

---

## Instalación y Uso

Al tratarse de una aplicación web estática sin dependencias externas ni servicios de backend, su despliegue es inmediato:

1. Clone el repositorio o descargue los archivos del proyecto en su equipo local.
2. Abra el archivo `index.html` en un navegador web moderno (se recomienda **Google Chrome** o **Microsoft Edge** para habilitar la escritura directa en archivos locales).
3. Opcionalmente, vincule o importe un archivo `contactos.txt` desde el panel izquierdo.
4. Utilice los controles de carga masiva (`1,000`, `10,000`, `100,000`) y seleccione **Carrera de algoritmos** para analizar el rendimiento comparativo.