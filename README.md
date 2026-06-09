# Juego de la Serpiente

Un clásico juego de la Serpiente (Snake) desarrollado en Python utilizando la biblioteca `pygame`.

## Características
- Movimiento clásico de la serpiente en las 4 direcciones.
- Crecimiento de la serpiente y aumento de puntuación al comer.
- Detección de colisiones contra los bordes de la pantalla y el propio cuerpo de la serpiente.
- Pantallas de "Game Over" y victoria.
- Opción para reiniciar el juego rápidamente presionando la tecla `R`.

## Requisitos
Para poder ejecutar este juego necesitas tener instalado:
- **Python 3.x**
- La biblioteca **pygame**

## Instalación
1. Clona o descarga este repositorio.
2. Instala la dependencia necesaria (pygame) ejecutando el siguiente comando en tu terminal:
   ```bash
   pip install pygame
   ```

## Cómo jugar
1. Navega hasta el directorio del proyecto en tu terminal.
2. Ejecuta el archivo principal:
   ```bash
   python serpiente.py
   ```

### Controles
- **Flecha Arriba**: Mover hacia arriba
- **Flecha Abajo**: Mover hacia abajo
- **Flecha Izquierda**: Mover hacia la izquierda
- **Flecha Derecha**: Mover hacia la derecha
- **Tecla R**: Reiniciar el juego (solo disponible en la pantalla de Game Over o Victoria)

## Reglas del Juego
- Come los bloques rojos para que la serpiente crezca y ganar puntos.
- Si chocas contra un borde de la pantalla o contra el cuerpo de la serpiente, pierdes ("Game Over").
- ¡Ganas si consigues que la serpiente ocupe toda la pantalla!
