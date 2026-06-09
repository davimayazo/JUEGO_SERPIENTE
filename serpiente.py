import pygame
import sys
import random

# Configuración del juego
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
TAMANO_CELDA = 20
FPS = 15

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Función para generar comida
def generar_comida(serpiente):
    while True:
        x = random.randint(0, (ANCHO_PANTALLA // TAMANO_CELDA) - 1) * TAMANO_CELDA
        y = random.randint(0, (ALTO_PANTALLA // TAMANO_CELDA) - 1) * TAMANO_CELDA
        
        if (x, y) not in serpiente:
            return (x, y)

# Función para mostrar texto (victoria o derrota)
def mostrar_texto(ventana, mensaje, color, y_offset=0):
    fuente = pygame.font.SysFont("Arial", 45)
    superficie_texto = fuente.render(mensaje, True, color)
    rect_texto = superficie_texto.get_rect(center=(ANCHO_PANTALLA // 2, (ALTO_PANTALLA // 2) + y_offset))
    ventana.blit(superficie_texto, rect_texto)

# Función principal del juego
def jugar():
    # Inicialicación de variables
    pos_x, pos_y = 400, 300
    serpiente = [(pos_x, pos_y)]
    vel_x, vel_y = 0, 0
    anterior_tecla = ""
    comida = generar_comida(serpiente)
    puntuacion = 0
    reloj = pygame.time.Clock()
    esta_vivo = True
    ganado = False


    while True:
        # Bucle para gestionar los eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            # Detectar teclas
            if evento.type == pygame.KEYDOWN:
                if esta_vivo:
                    if evento.key == pygame.K_UP and anterior_tecla != pygame.K_DOWN:
                        anterior_tecla = pygame.K_UP
                        vel_x = 0
                        vel_y = -TAMANO_CELDA  # Subir es restar en Y
                    elif evento.key == pygame.K_DOWN and anterior_tecla != pygame.K_UP:
                        anterior_tecla = pygame.K_DOWN
                        vel_x = 0
                        vel_y = TAMANO_CELDA   # Bajar es sumar en Y
                    elif evento.key == pygame.K_LEFT and anterior_tecla != pygame.K_RIGHT:
                        anterior_tecla = pygame.K_LEFT
                        vel_x = -TAMANO_CELDA  # Izquierda es restar en X
                        vel_y = 0
                    elif evento.key == pygame.K_RIGHT and anterior_tecla != pygame.K_LEFT:
                        anterior_tecla = pygame.K_RIGHT
                        vel_x = TAMANO_CELDA   # Derecha es sumar en X
                        vel_y = 0
                # Si ha perdido, presionar R para reiniciar el juego
                elif evento.key == pygame.K_r:
                    return

        if esta_vivo and (vel_x != 0 or vel_y != 0):
            pos_x += vel_x
            pos_y += vel_y

            # Comprobamos las colisiones (bordes de la pantalla y de la serpiente)
            if pos_x < 0 or pos_x >= ANCHO_PANTALLA or pos_y < 0 or pos_y >= ALTO_PANTALLA or (pos_x,pos_y) in serpiente[1:]:
                esta_vivo = False
            # Si no hay colisión, movemos la serpiente
            elif (pos_x, pos_y) != serpiente[0]:
                serpiente.insert(0,(pos_x,pos_y))
                # Si come, aumenta el tamaño la serpiente, aumenta la puntuación y genera nueva comida
                if (pos_x,pos_y) == comida:
                    puntuacion += 1
                    # Comprobamos si ha ganado (la serpiente ocupa toda la pantalla)
                    if puntuacion == ((ANCHO_PANTALLA // TAMANO_CELDA) * (ALTO_PANTALLA // TAMANO_CELDA) - 1):
                        ganado = True
                    else:
                        comida = generar_comida(serpiente)
                else:
                    serpiente.pop()

        # Actualizar pantalla
        ventana.fill(NEGRO)

        if esta_vivo and not ganado:
            # Dibujamos la serpiente
            for X, Y in serpiente:
                pygame.draw.rect(ventana, VERDE, [X, Y, TAMANO_CELDA, TAMANO_CELDA])
            # Dibujamos la comida
            pygame.draw.rect(ventana, ROJO, [comida[0], comida[1], TAMANO_CELDA, TAMANO_CELDA])
            # Mostramos el marcador de puntuación
            fuente_puntos = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente_puntos.render(f"Puntos: {puntuacion}", True, BLANCO)
            ventana.blit(texto_puntos, [10, 10]) # En la esquina superior izquierda
        elif ganado:
            # Mostramos mensaje de victoria
            mostrar_texto(ventana, "¡GANASTE!", VERDE, -30)
            mostrar_texto(ventana, "Presiona 'R' para reiniciar", BLANCO, 40)
        else:
            # Mostramos mensaje de game over
            mostrar_texto(ventana, "¡GAME OVER!", ROJO, -30)
            mostrar_texto(ventana, "Presiona 'R' para reiniciar", BLANCO, 40)

        pygame.display.flip()
        reloj.tick(FPS)

# Inicialización del juego
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption('Juego de la Serpiente')
    while True:
        jugar()