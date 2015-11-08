import pygame,sys
from pygame.locals import * 
from random import randint

pygame.init()
ventana = pygame.display.set_mode((512,512))
pygame.display.set_caption("4 en Raya")

Blanco=(255,255,255)
Negro=(0,0,0)

a8=(8,8)
a7=(8,72)
a6=(8,136)
a5=(8,200)
a4=(8,264)
a3=(8,328)
a2=(8,392)
a1=(8,456)

b1=(72,456)
c1=(136,456)
d1=(200,456)
e1=(264,456)
f1=(328,456)
g1=(392,456)
h1=(456,456)

b8=(72,8)
c8=(136,8)
d8=(200,8)
e8=(264,8)
f8=(328,8)
g8=(392,8)
h8=(456,8)

b7=(72,72)

A1="none"
B1="none"
C1="none"
D1="none"
E1="none"
F1="none"
G1="none"
H1="none"

azul = pygame.image.load("imagenes/azul.png")
rojo = pygame.image.load("imagenes/rojo.png")
fondo = pygame.image.load("imagenes/normal.png")
posX,posY=200,100;

ventana.blit(azul,(b1))
ventana.blit(azul,(c1))
ventana.blit(azul,(d1))
ventana.blit(azul,(e1))
ventana.blit(azul,(f1))
ventana.blit(azul,(g1))
ventana.blit(azul,(h1))

ventana.blit(azul,(posX,posY))
una_vez=True
turno=True
ocupado=1
permanente_A1=False
while True:	
	ventana.blit(fondo,(0,0))
	if A1=="azul":
		ventana.blit(azul,(a1))		
	elif A1=="rojo":
		ventana.blit(rojo,(a1))
	if B1=="azul":
		ventana.blit(azul,(b1))
	elif B1=="rojo":
		ventana.blit(rojo,(b1))
	if C1=="azul":
		ventana.blit(azul,(c1))
	elif C1=="rojo":
		ventana.blit(rojo,(c1))
	if D1=="azul":
		ventana.blit(azul,(d1))
	elif D1=="rojo":
		ventana.blit(rojo,(d1))
	if E1=="azul":
		ventana.blit(azul,(e1))
	elif E1=="rojo":
		ventana.blit(rojo,(e1))
	if F1=="azul":
		ventana.blit(azul,(f1))
	elif F1=="rojo":
		ventana.blit(rojo,(f1))
	if G1=="azul":
		ventana.blit(azul,(g1))
	elif G1=="rojo":
		ventana.blit(rojo,(g1))
	if H1=="azul":
		ventana.blit(azul,(h1))
	elif H1=="rojo":
		ventana.blit(rojo,(h1))

	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()		

	click = evento.type	

	if click==6:
		pos_mouse=pygame.mouse.get_pos()
		if (pos_mouse[0] <64):
			if (turno==True) & (permanente_A1==False):
				A1="azul"
				permanente_A1=True
			elif (turno==False) & (permanente_A1==False):
				A1="rojo"
				permanente_A1=True
		elif (pos_mouse[0] >= 64) & (pos_mouse[0] < 128):
			if turno==True:
				B1="azul"
			else:
				B1="rojo"
		elif (pos_mouse[0] >= 128) & (pos_mouse[0] < 192):
			if turno==True:
				C1="azul"
			else:
				C1="rojo"
		elif (pos_mouse[0] >= 192) & (pos_mouse[0] < 254):
			if turno==True:
				D1="azul"
			else:
				D1="rojo"
		elif (pos_mouse[0] >= 254) & (pos_mouse[0] < 320):
			if turno==True:
				E1="azul"
			else:
				E1="rojo"
		elif (pos_mouse[0] >= 320) & (pos_mouse[0] < 384):
			if turno==True:
				F1="azul"
			else:	
				F1="rojo"
		elif (pos_mouse[0] >= 384) & (pos_mouse[0] < 448):
			if turno==True:
				G1="azul"
			else:	
				G1="rojo"
		elif (pos_mouse[0] >= 448) & (pos_mouse[0] < 512):
			if turno==True:
				H1="azul"
			else:	
				H1="rojo"

	pygame .display.update()