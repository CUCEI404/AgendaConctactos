# Agenda Algorítmica — Equipo 404

**Optimización de búsqueda, ordenamiento, gestión de eventos y control de duplicados mediante estructuras de datos y Divide y Vencerás**

*Proyecto desarrollado para la asignatura **Análisis de Algoritmos** — Centro Universitario de Ciencias Exactas e Ingenierías (CUCEI).*

## Integrantes del Equipo

* **Bryhan Francisco García Espinoza**
* **Emmanuel Alejandro Ortiz Segura**
* **Roberto Hernández Zuñiga**

---

## Planteamiento del Problema

En negocios pequeños, consultorios, grupos escolares y aplicaciones administrativas sencillas, los registros de contactos (**nombre, teléfono, correo electrónico y fecha de nacimiento**) suelen almacenarse en estructuras lineales sin ningún criterio de ordenamiento ni indexación temporal.

Cuando el volumen de información crece a cientos o miles de entradas, surgen tres problemas principales:

* **Consultas lineales lentas:** Localizar un contacto o filtrar eventos por fecha requiere inspeccionar la lista elemento por elemento; en el peor caso, se recorre toda la estructura con una complejidad temporal de $O(n)$.
* **Inserciones costosas y duplicidad de datos:** Para evitar registros repetidos al dar de alta un contacto, los sistemas básicos vuelven a recorrer toda la lista. Cuando esta validación se omite o falla, la agenda acumula registros duplicados.
* **Ausencia de evidencia empírica:** Las aplicaciones comerciales ocultan su funcionamiento interno y los desarrollos académicos básicos rara vez miden cuantitativamente la mejora de rendimiento al cambiar de paradigma algorítmico.

---

## Objetivo del Proyecto

Desarrollar una aplicación web interactiva autocontenida en **HTML5, CSS3 y JavaScript (Vanilla)** que, mediante la implementación de **Merge Sort**, **Búsqueda Binaria** y **Tablas Hash (`Map` y `Set`)**, mantenga los registros ordenados, libres de duplicados y con consulta instantánea de cumpleaños y recordatorios, reduciendo significativamente el número de comparaciones y el tiempo de ejecución frente a la búsqueda secuencial.

---

## Evolución del Desarrollo por Fases

El proyecto se estructuró de manera incremental siguiendo los hitos de evaluación de la materia:

### Fase 1: Algoritmo Base y Estructura de Referencia
En esta etapa inicial se construyó el núcleo funcional sobre una estructura lineal sin ordenamiento para establecer la línea base de rendimiento:
* **Almacenamiento secuencial:** Los contactos se insertan al final de un arreglo manteniendo el orden de llegada.
* **Búsqueda Secuencial por Prefijo — $O(n)$:** Recorre linealmente toda la colección evaluando cada contacto uno por uno para hallar coincidencias, contabilizando el total exacto de revisiones y el tiempo en milisegundos mediante `performance.now()`.
* **Interfaz de captura y métricas:** Formulario de registro con validación de formato y panel de telemetría básica (total de registros, revisiones y tiempo de búsqueda).

### Fase 2: Optimización con Divide y Vencerás, Indexación Hash y Calendario 
En la segunda fase se incorporaron algoritmos eficientes, estructuras de acceso constante y un módulo completo de calendario:
* **Ordenamiento con Merge Sort — $O(n \log n)$:** Algoritmo recursivo basado en *Divide y Vencerás* que ordena alfabéticamente los contactos mediante una clave normalizada (sin acentos ni distinción entre mayúsculas y minúsculas), contabilizando las comparaciones exactas realizadas.
* **Búsqueda Binaria (Cota Inferior / Lower Bound) — $O(\log n)$:** Localiza la primera aparición de un prefijo dividiendo el espacio de búsqueda a la mitad en cada iteración, recolectando posteriormente los registros contiguos que coinciden con el criterio.
* **Control de duplicados en $O(1)$ e inserción incremental:** Sustitución de la verificación lineal por una estructura `Set` indexada por número telefónico para rechazar duplicados al instante, junto con inserción ordenada mediante búsqueda binaria ($O(\log n)$) sin necesidad de reordenar todo el arreglo tras cada alta.
* **Módulo de Calendario e Indexación de Cumpleaños en $O(1)$:** Implementación de una tabla hash (`Map`) con clave `MM-DD` que agrupa las fechas de nacimiento (incluyendo soporte para años bisiestos en registros del 29 de febrero), permitiendo consultar los cumpleaños de cualquier día del mes o de los próximos 30 días en tiempo constante.
* **Gestión de Notas y Persistencia Extendida:** Soporte para crear y eliminar recordatorios por fecha, almacenándolos junto con los contactos dentro del archivo plano `contactos.txt`, y sustitución de la generación aleatoria en memoria por la carga directa de lotes externos desde archivo `.txt`.

---

## Arquitectura y Comparativa Algorítmica

El sistema permite alternar en tiempo real entre ambos motores de ejecución en memoria para contrastar su comportamiento sobre el mismo conjunto de datos:

```text
[ MODO BASE ]               Lista desordenada ──► Búsqueda Secuencial ──► O(n) comparaciones
[ DIVIDE Y VENCERÁS ]       Merge Sort O(n log n) ──► Lista Ordenada ──► Búsqueda Binaria (Lower Bound) O(log n)
[ INDEXACIÓN HASH ]         Clave MM-DD / Teléfono ──► Map / Set ──► Consulta de cumpleaños y duplicados en O(1)
```

---

## Características Técnicas

* **Trazabilidad de Búsqueda Binaria:** Visualiza cada iteración del algoritmo mostrando los límites del subarreglo activo $[lo, hi)$, el índice central (`mid`) y la dirección de descarte.
* **Calendario Interactivo y Próximos Eventos:** Vista mensual navegable con indicadores visuales para cumpleaños y notas, panel de detalle diario con cálculo automático de edad y resumen cronológico de los próximos 30 días.
* **Persistencia en Archivo Plano (`contactos.txt`):**
  * **Vinculación directa:** Integración con la *File System Access API* (disponible en navegadores basados en Chromium como Google Chrome y Microsoft Edge) para leer, anexar y sobrescribir registros directamente sobre un archivo local.
  * **Compatibilidad universal:** Funciones de importación y descarga de archivos `.txt` para cualquier navegador.
  * **Estructura de almacenamiento:** Texto plano delimitado por barras verticales (`nombre|telefono|correo|nacimiento` para contactos y `#NOTA|fecha|texto` para recordatorios).
* **Optimización del DOM:** Implementa paginación visual limitada a 100 nodos simultáneos en pantalla para mantener la fluidez de la interfaz al procesar grandes volúmenes de datos importados.

---

## Estructura del Proyecto

```text
agenda-algoritmica/
├── index.html      # Aplicación autocontenida (estructura, estilos, calendario y lógica algorítmica)
├── contactos.txt   # Archivo de datos de ejemplo en formato delimitado
└── README.md       # Documentación técnica del proyecto
```

---

## Instalación y Uso

Al tratarse de una aplicación web estática sin dependencias externas ni servicios de backend, su despliegue es inmediato:

1. Clone el repositorio o descargue los archivos del proyecto en su equipo local.
2. Abra el archivo `index.html` en un navegador web moderno (se recomienda **Google Chrome** o **Microsoft Edge** para habilitar la escritura directa en archivos locales).
3. Utilice el panel izquierdo para vincular (`Abrir contactos.txt` / `Crear contactos.txt`) o importar un archivo `.txt` con lotes de prueba.
4. Alterne entre **Modo Base O(n)** y **Divide y Vencerás** en el encabezado para comparar las revisiones y el tiempo de cada búsqueda.
5. Para correr las pruebas de casos borde de Divide y Vencerás, abra la consola del navegador (F12) y ejecute `pruebasDyV()`.