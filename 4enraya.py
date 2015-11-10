import pygame,sys
import numpy as np
from pygame.locals import * 
from StringIO import StringIO 

matriz_A = [False,False,False,False,False,False,False,False]
matriz_B = [False,False,False,False,False,False,False,False]
matriz_C = [False,False,False,False,False,False,False,False]
matriz_D = [False,False,False,False,False,False,False,False]
matriz_E = [False,False,False,False,False,False,False,False]
matriz_F = [False,False,False,False,False,False,False,False]
matriz_G = [False,False,False,False,False,False,False,False]
matriz_H = [False,False,False,False,False,False,False,False]

AM = [(8,456),(8,392),(8,328),(8,264),(8,200),(8,136),(8,72),(8,8)]
BM = [(72,456),(72,392),(72,328),(72,264),(72,200),(72,136),(72,72),(72,8)]
CM = [(136,456),(136,392),(136,328),(136,264),(136,200),(136,136),(136,72),(136,8)]
DM = [(200,456),(200,392),(200,328),(200,264),(200,200),(200,136),(200,72),(200,8)]
EM = [(264,456),(264,392),(264,328),(264,264),(264,200),(264,136),(264,72),(264,8)]
FM = [(328,456),(328,392),(328,328),(328,264),(328,200),(328,136),(328,72),(328,8)]
GM = [(392,456),(392,392),(392,328),(392,264),(392,200),(392,136),(392,72),(392,8)]
HM = [(456,456),(456,392),(456,328),(456,264),(456,200),(456,136),(456,72),(456,8)]


Y = [456,392,328,264,200,136,72,8]

xv = [8,72,136,200,264,328,392,456]

pygame.init()
ventana = pygame.display.set_mode((512,512))
pygame.display.set_caption("4 en Raya")

Blanco=(255,255,255)
Negro=(0,0,0)

azul = pygame.image.load("imagenes/azul.png")
rojo = pygame.image.load("imagenes/rojo.png")
fondo = pygame.image.load("imagenes/normal.png")
posX,posY=200,100;

una_vez=True
turno=True
ocupado=1

def turnochange( loque ):
	if (loque==True):
		turnolocal=False
	else:
		turnolocal=True
	return turnolocal


def colorprint( loque ):
	if (loque==True):
		#azul
		turnolocal= azul
	else:
		#rojo
		turnolocal= rojo
	return turnolocal

def posiciones( matriz ):
	global turno
	total = len( matriz ) - 1
	print total
	if ( matriz[total] == False): 
		for i in range(0,len(matriz)):
			if matriz[i] == False:
				matriz[i] = colorprint(turno)
				turno = turnochange(turno)
				return matriz
				break
			else:
				print "-"
	else:
		return matriz			


while True:	
	ventana.blit(fondo,(0,0))
	for i in range(0,len(matriz_A)):	
		if matriz_A[i]!=False:
			ventana.blit(matriz_A[i],(AM[i]))
	for i in range(0,len(matriz_B)):
		if matriz_B[i]!=False:
			ventana.blit(matriz_B[i],(BM[i]))
	for i in range(0,len(matriz_C)):
		if matriz_C[i]!=False:
			ventana.blit(matriz_C[i],(CM[i]))
	for i in range(0,len(matriz_D)):
		if matriz_D[i]!=False:
			ventana.blit(matriz_D[i],(DM[i]))
	for i in range(0,len(matriz_E)):
		if matriz_E[i]!=False:
			ventana.blit(matriz_E[i],(EM[i]))
	for i in range(0,len(matriz_F)):
		if matriz_F[i]!=False:
			ventana.blit(matriz_F[i],(FM[i]))
	for i in range(0,len(matriz_G)):
		if matriz_G[i]!=False:
			ventana.blit(matriz_G[i],(GM[i]))
	for i in range(0,len(matriz_H)):
		if matriz_H[i]!=False:
			ventana.blit(matriz_H[i],(HM[i]))

	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

	click = evento.type	
	if click == pygame.MOUSEBUTTONDOWN:
		pygame.time.delay(100)
		pos_mouse=pygame.mouse.get_pos()		

		if (pos_mouse[0] <64):				
				matriz_A = posiciones( matriz_A )
		elif (pos_mouse[0] >= 64) & (pos_mouse[0] < 128):
				matriz_B = posiciones( matriz_B )
		elif (pos_mouse[0] >= 128) & (pos_mouse[0] < 192):
				matriz_C = posiciones( matriz_C )
		elif (pos_mouse[0] >= 192) & (pos_mouse[0] < 254):	
				matriz_D = posiciones( matriz_D )
		elif (pos_mouse[0] >= 254) & (pos_mouse[0] < 320):			
				matriz_E = posiciones( matriz_E )
		elif (pos_mouse[0] >= 320) & (pos_mouse[0] < 384):
				matriz_F = posiciones( matriz_F)
		elif (pos_mouse[0] >= 384) & (pos_mouse[0] < 448):
				matriz_G = posiciones( matriz_G )
		elif (pos_mouse[0] >= 448) & (pos_mouse[0] < 512):
				matriz_H = posiciones( matriz_H )

	pygame .display.update()