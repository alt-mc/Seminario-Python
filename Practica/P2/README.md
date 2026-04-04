# Python 2026 - Actividad 2

Resolución de la Actividad Práctica 2 de la materia Python 2026.

## Estructura del proyecto

```
.
├── notebooks/
│   └── ejercicio10.ipynb   # Notebook con la ejecución del ejercicio 10
├── src/
│   └── ejercicio_10.py     # Función competition_simulation
└── README.md
```

## Requisitos

- Python 3.8 o superior
- Jupyter Notebook o JupyterLab

Este proyecto no tiene dependencias externas: utiliza únicamente la biblioteca estándar de Python.

## Instalación

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPO>
cd <nombre-del-repo>
```

2. (Opcional) Crear y activar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Instalar Jupyter:

```bash
pip install notebook
```

## Ejecución

Desde la raíz del proyecto, lanzar Jupyter Notebook:

```bash
jupyter notebook
```

Luego abrir el archivo `notebooks/ejercicio10.ipynb` y ejecutar las celdas en orden.

## Ejercicio 10 — Simulación de competencia de cocina

La función `competition_simulation` recibe una lista de rondas. Cada ronda contiene un tema y los puntajes otorgados por 3 jueces a cada participante.

El programa calcula por cada ronda:
- El ganador (participante con mayor puntaje en esa ronda)
- La tabla de posiciones de la ronda

Al finalizar todas las rondas, imprime la tabla de posiciones final con:
- Puntaje total acumulado
- Cantidad de rondas ganadas
- Mejor puntaje en una sola ronda
- Promedio de puntaje por ronda