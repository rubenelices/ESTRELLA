import turtle

#Hago el input para que el programa pregunte por el número de puntas que se quieran
puntas = int(input("ingrese el número de puntas: "))

#Función con la que se dibujará la estrella 
def dibujar_estrella(puntas, longitud_puntas):
    #Velocidad del dibujo
    turtle.speed(50)     
    
    #Color del puntero (morado)    
    turtle.color("purple") 
    
    #Forma del puntero (Una tortuga)
    turtle.shape("turtle")    

    #Color del fondo (Azul clarito)   
    turtle.bgcolor("lightblue")

    for _ in range(puntas):
        turtle.forward(longitud_puntas)

        #Fórmula para las estrellas pares
        if puntas % 2 == 0:

            # Ajuste del ángulo para números pares que al dividirlos por 2 dan pares (estrella)
            if (puntas/2) % 2 == 0:
                turtle.right(180 - (360 / puntas))

            #Ajuste del ángulo para números pares que al dividirlos por 2 dan impares
            elif (puntas/2) % 2 != 0:
                turtle.right(180 - (360 / (puntas / 2)))
            
        else:

            # Ajuste del ángulo para números impares de puntas (estrella)
            turtle.right(180 - (180 / puntas))

    turtle.done()

dibujar_estrella(puntas,200)












