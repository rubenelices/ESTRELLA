import turtle
import turtle

def dibujar_estrella(puntas, longitud_puntas):
    turtle.speed(12)  # Velocidad del dibujo

    for _ in range(puntas):
        turtle.forward(longitud_puntas)

        # Ángulo para estrella
        angulo_estrella = 180 - 180 / puntas

        # Ajuste adicional para números pares y múltiplos de 6
        if puntas % 2 == 0 or puntas % 6 == 0:
            angulo_estrella += 60

        turtle.right(angulo_estrella)

    turtle.done()

# Ejemplo: Dibujar una estrella de 15 puntas con longitud de puntas 150
dibujar_estrella(8, 150)

