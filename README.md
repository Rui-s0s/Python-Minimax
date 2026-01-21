# 🐱🐭 Proyecto Minimax: Gato vs Ratón

## 📌 Descripción
Este proyecto es una práctica orientada al aprendizaje de **algoritmos**, **estructuras de datos** y **recursividad**, implementando un juego por terminal donde un **gato** intenta atrapar a un **ratón** dentro de un número limitado de turnos.

El jugador controla al gato desde la terminal, mientras que el ratón utiliza una **inteligencia artificial basada en el algoritmo Minimax** para decidir sus movimientos.

---

## 🎯 Objetivos de Aprendizaje
- Comprender y aplicar el **algoritmo Minimax**
- Practicar **recursividad y casos base**
- Utilizar **listas, tuplas e inputs**
- Representar un tablero como una **matriz**
- Trabajar con **coordenadas y movimientos en el plano**
- Introducir conceptos básicos de **inteligencia artificial para juegos**

---

## 🧠 Inteligencia Artificial del Ratón
El ratón se mueve utilizando el algoritmo **Minimax**, el cual:
- Evalúa posibles movimientos futuros hasta una **profundidad limitada**
- Considera el **mejor movimiento en el peor caso posible**
- Asume que el gato siempre jugará de forma óptima
- Finaliza la recursión cuando:
  - El ratón es capturado
  - La profundidad llega a cero

El ratón puede moverse en **8 direcciones** y un número determinado de casillas por turno.

---

## 🎮 Movimiento del Gato
- El gato es controlado por el usuario desde la terminal
- Se mueve siguiendo las reglas del **caballo en ajedrez**
- Los movimientos se ingresan mediante **input por consola**

---

## 🗺️ Representación del Tablero
- El tablero se representa como una **matriz (lista de listas)**
- Cada posición se maneja mediante **coordenadas (x, y)**
- Se aplican cálculos de:
  - Distancia entre dos puntos
  - Movimientos válidos en el plano
  - Validación de límites del tablero

---

## 🔁 Recursividad
La recursividad es un concepto clave en la implementación de Minimax:
- Cada llamada recursiva representa un turno futuro
- El **caso base** ocurre cuando:
  - El ratón es capturado
  - La profundidad alcanza cero
- Los valores se propagan hacia atrás para determinar el mejor movimiento

---

## ▶️ Ejecución
Ejecuta el proyecto desde la terminal con:

```bash
git clone https://github.com/Rui-s0s/Python-Minimax.git
cd .\Python-Minimax\ 
python mimimax.py
