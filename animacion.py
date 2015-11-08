import pygame,sys
from pygame.locals import * 
from random import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Hola Mundo")#Titulo de la ventana

Blanco=(255,255,255)
Negro=(0,0,0)

#par1= En donde va a ir la linea (Ventana)
#par2= Color que llevara
#par3= Dupla de (x,y) indica posicion de inicio de la linea
#par4= Dupla de (x,y) indica posicion de final de la linea
#par5= Define el ancho de la linea
#pygame.draw.line(ventana,Blanco,(60,80),(160,100),4)


#par1= En donde va a ir el circulo (Ventana)
#par2= Color que llevara
#par3= Dupla de (x,y) indica posicion del centro del circulo
#par4= Radio del circulo
#pygame.draw.circle(ventana,(8,70,120),(80,90),20)


#par1= En donde va a ir el rectangulo (Ventana)
#par2= Color que llevara
#par3= Dupla de (x,y,ancho,alto) a partir de la esquina superior izq
#pygame.draw.rect(ventana,(8,70,120),(0,0,100,50))

#par1= En donde va a ir el poligono (Ventana)
#par2= Color que llevara
#par3= cantidad de pts que llevara el poligono
#pygame.draw.polygon(ventana,(8,70,120),((140,0),(291,106),(237,277),(56,277),(0,106)))

mi_imagen = pygame.image.load("imagenes/azul.png")
posX=200
posY=100

velocidad=0.1
derecha=True

while True:#ciclo infinito que muestra la ventana siempre y cuando no la quiera cerrar	
	ventana.fill(Blanco)
	ventana.blit(mi_imagen,(posX,posY))
	for event in pygame.event.get():#define eventos
		if event.type == QUIT:#evento salir!!
			pygame.quit()
			sys.exit()

	if derecha==True:
		if posX<400:
			posX+=velocidad
		else:
			derecha=False
	else:
		if posX>1:
			posX-=velocidad
		else:
			derecha=True

	pygame .display.update()