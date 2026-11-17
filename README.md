<div align="center">

# 📇 Agenda Algorítmica — Equipo 404

**Optimización de búsqueda, ordenamiento y control de duplicados mediante *Divide y Vencerás***

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-1F6AA5?style=for-the-badge&logo=python&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
[![Algoritmos](https://img.shields.io/badge/Paradigma-Divide_y_Vencerás-2ea44f?style=for-the-badge)](#)

*Proyecto desarrollado para la materia **Seminario de Integración de Desarrollo** — CUCEI*

</div>

---

## 🎯 Planteamiento del Problema

En negocios pequeños, consultorios, grupos escolares y aplicaciones de escritorio sencillas, los contactos (**nombre, teléfono y correo**) suelen almacenarse en listas de Python sin ningún criterio de orden. 

Cuando la agenda crece a cientos o miles de registros:
- **Consultas lentas:** Encontrar un contacto exige revisar la lista elemento por elemento; en el peor caso se recorre toda la estructura ($O(n)$).
- **Inserciones costosas y duplicados:** Para evitar registros repetidos al guardar un nuevo contacto, el sistema vuelve a recorrer toda la lista. Cuando esta validación se omite o falla, la agenda se llena de duplicados.
- **Falta de evidencia empírica:** Las aplicaciones comerciales ocultan su funcionamiento interno y los programas básicos rara vez miden cuánto mejora el rendimiento al cambiar de paradigma algorítmico.

---

## 🚀 Objetivo del Proyecto

Desarrollar una aplicación de escritorio interactiva en **Python** con interfaz gráfica moderna en **CustomTkinter** que, mediante **Merge Sort** y **Búsqueda Binaria**, mantenga los registros siempre ordenados y libres de duplicados, reduciendo drásticamente el número de revisiones y el tiempo de ejecución frente a la búsqueda secuencial, comprobándolo mediante pruebas de rendimiento con **1,000**, **10,000** y **100,000** contactos.

---

## ⚡ Comparativa Algorítmica (Base vs. Divide y Vencerás)

El sistema permite alternar en tiempo real entre dos motores de procesamiento en Python para medir su comportamiento y tiempos con los mismos lotes de datos:

```text
[ MODO BASE ]               Lista desordenada ──► Búsqueda Secuencial ──► O(n) revisiones
[ DIVIDE Y VENCERÁS ]       Merge Sort O(n log n) ──► Lista Ordenada ──► Búsqueda Binaria O(log n)
