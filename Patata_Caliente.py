import random
import pygame,sys
from classQueue import Queue
from button import Button
import sys
import math
#from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.font import Font
from pygame import mixer

pygame.init()

height=1280
widht=720

ventana = pygame.display.set_mode((height,widht))

# Fondo y Caption
BG = pygame.image.load("assets/Background.png")
pygame.display.set_caption("Papa Caliente")

class Jugador:
    def __init__(self,nombre,estado,bola,posx,posy):
        self.nombre=nombre
        self.estado=estado
        self.bola=bola
        self.posx=posx
        self.posy=posy
        #self.imagen=imagen

    def setBola(self,bola):
        self.bola=bola
    def getBola(self):
        return self.bola
    def getNombre(self):
        return self.nombre

    def crearJugador(self):

        radio = 50
        if (self.bola):
            pygame.draw.circle(ventana, "green", (self.posx, self.posy), radio)
            text = get_font(20).render(self.nombre, True, "green")
            rect = text.get_rect(center=(self.posx, self.posy-60))
            ventana.blit(text, rect)
        else:
            pygame.draw.circle(ventana, "white", (self.posx, self.posy), radio)
            text = get_font(20).render(self.nombre, True, "white")
            rect = text.get_rect(center=(self.posx, self.posy-60))
            ventana.blit(text, rect)
        #font = get_font(18)  # Obtener la fuente
        #nomb = nombre[0]  # Obtener el nombre del primer jugador
        
    
    

# Devuelve la fuente del tamaño que se desee
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def jugar():

    num_jugadores = 2 # número inicial de jugadores
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        ventana.fill("black")

        # Mostrar el número actual de jugadores en la pantalla
        text = get_font(36).render(f"Jugadores: {num_jugadores}", True, "white")
        rect = text.get_rect(center=(640, 50))
        ventana.blit(text, rect)

        # Crear el botón de aumentar jugadores
        aumentar_jugadores_button = Button(image=None, pos=(640, 300), text_input="+", font=get_font(64), base_color="white", hovering_color="green")
        
        # Crear el botón de disminuir jugadores
        disminuir_jugadores_button = Button(image=None, pos=(640, 400), text_input="-", font=get_font(64), base_color="white", hovering_color="red")

        # Crear el botón de salir
        salir_button = Button(image=None, pos=(240, 600), text_input="SALIR", font=get_font(40), base_color="white", hovering_color="red")

         # Crear el botón de continuar
        continuar_button = Button(image=None, pos=(1000, 600), text_input="CONTINUAR", font=get_font(40), base_color="white", hovering_color="green")


        # Actualizar y mostrar los botones
        aumentar_jugadores_button.changeColor(MOUSE_POS)
        aumentar_jugadores_button.update(ventana)

        disminuir_jugadores_button.changeColor(MOUSE_POS)
        disminuir_jugadores_button.update(ventana)

        salir_button.changeColor(MOUSE_POS)
        salir_button.update(ventana)

        continuar_button.changeColor(MOUSE_POS)
        continuar_button.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if aumentar_jugadores_button.checkForInput(MOUSE_POS) and num_jugadores < 6:
                    num_jugadores += 1
                if disminuir_jugadores_button.checkForInput(MOUSE_POS) and num_jugadores > 2:
                    num_jugadores -= 1
                if salir_button.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if continuar_button.checkForInput(MOUSE_POS):
                    nombres(num_jugadores)

        pygame.display.update()

    radio = 50
    if (num==2):
        separacion=800
    elif(num==3):
        separacion=450
    elif(num==4):
        separacion=300
    elif(num==5):
        separacion=225
    elif(num==6):
        separacion = 170
    x_ini = 200
    y = 300
    for i in range(num):
        x = x_ini + i*separacion
        pygame.draw.circle(ventana, "white", (x, y), radio)
        font = get_font(18)  # Obtener la fuente
        nomb = nombre[0]  # Obtener el nombre del primer jugador
        text = get_font(20).render(nombre[i], True, "white")
        rect = text.get_rect(center=(x, y-60))  # Obtener el rectángulo de la superficie de texto
        ventana.blit(text, rect)  # Dibujar la superficie de texto sobre la ventana


def juego(nombres_jugadores):
    jugadores_eliminados=[]
    num_jugadores = len(nombres_jugadores)

    if (num_jugadores==2):
        jugador1=Jugador(nombres_jugadores[0],True,True,200,300)#+800
        jugador2=Jugador(nombres_jugadores[1],True,False,1000,300)

        jugadores=[jugador1,jugador2]
        for i in range(len(jugadores)):
            jugadores[i].crearJugador()

    if(num_jugadores==3):
        jugador1=Jugador(nombres_jugadores[0],True,True,200,300)#+450
        jugador2=Jugador(nombres_jugadores[1],True,False,650,300)
        jugador3=Jugador(nombres_jugadores[2],True,False,1100,300)

        jugadores=[jugador1,jugador2,jugador3]
        for i in range(len(jugadores)):
            jugadores[i].crearJugador()
        

    elif(num_jugadores==4):
        jugador1=Jugador(nombres_jugadores[0],True,True,200,300)#+300
        jugador2=Jugador(nombres_jugadores[1],True,False,500,300)
        jugador3=Jugador(nombres_jugadores[2],True,False,800,300)
        jugador4=Jugador(nombres_jugadores[3],True,False,1100,300)

        jugadores=[jugador1,jugador2,jugador3,jugador4]
        for i in range(len(jugadores)):
            jugadores[i].crearJugador()

    elif(num_jugadores==5):
        jugador1=Jugador(nombres_jugadores[0],True,True,200,300)#+225
        jugador2=Jugador(nombres_jugadores[1],True,False,425,300)
        jugador3=Jugador(nombres_jugadores[2],True,False,650,300)
        jugador4=Jugador(nombres_jugadores[3],True,False,875,300)
        jugador5=Jugador(nombres_jugadores[4],True,False,1100,300)

        jugadores=[jugador1,jugador2,jugador3,jugador4,jugador5]
        for i in range(len(jugadores)):
            jugadores[i].crearJugador()


    elif(num_jugadores==6):
        jugador1=Jugador(nombres_jugadores[0],True,True,200,300)#+170
        jugador2=Jugador(nombres_jugadores[1],True,False,370,300)
        jugador3=Jugador(nombres_jugadores[2],True,False,540,300)
        jugador4=Jugador(nombres_jugadores[3],True,False,710,300)
        jugador5=Jugador(nombres_jugadores[4],True,False,880,300)
        jugador6=Jugador(nombres_jugadores[5],True,False,1100,300)#1050

        jugadores=[jugador1,jugador2,jugador3,jugador4,jugador5,jugador6]
        

    estado=True
    pygame.init()
    print
    ventana = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Juego")

    # Starting the mixer
    mixer.init()
    
    # Loading the song
    mixer.music.load("Sounds/cancion.mp3")
    
    # Setting the volume
    mixer.music.set_volume(0.2)
    
    # Start playing the song
    mixer.music.play()

    pausa_button = Button(image=None, pos=(1000, 600), text_input="PAUSAR", font=get_font(40), base_color="white", hovering_color="green")
    
    pausa_button.update(ventana)
    
    past=pygame.time.get_ticks()
    accumulated=0
    jug=0
    reloj=pygame.time.Clock()
    while True:
        present=pygame.time.get_ticks()
        delta=present-past
        past=present
        accumulated+=delta
        if(accumulated>=1500 and estado):
            accumulated=0
            if(jug>=num_jugadores):
                jug=0
            jugadores[jug-1].setBola(False)
            jugadores[jug].setBola(True)
            jug+=1
        


        # Crear el título con la fuente
        text = get_font(36).render(f"Jugadores: {num_jugadores}", True, "white")
        rect = text.get_rect(center=(640, 50))
        ventana.fill((0,0,0))
        ventana.blit(text, rect)

        MOUSE_POS = pygame.mouse.get_pos()

        for i in range(len(jugadores)):
            jugadores[i].crearJugador()


        # Crear el botón de salir
        salir_button = Button(image=None, pos=(240, 600), text_input="SALIR", font=get_font(40), base_color="white", hovering_color="red")

        salir_button.changeColor(MOUSE_POS)
        salir_button.update(ventana)
        pausa_button.changeColor(MOUSE_POS)
        pausa_button.update(ventana)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if salir_button.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                if pausa_button.checkForInput(MOUSE_POS):
                    if (estado):
                        past=0
                        present=0
                        delta=0
                        accumulated=0
                        mixer.music.stop()
                        estado=False
                        pausa_button = Button(image=None, pos=(1000, 600), text_input="REANUDAR", font=get_font(40), base_color="white", hovering_color="green")
                        ventana.fill((0,0,0))
                        j=0
                        for i in jugadores:
                            if (i.getBola()):
                                mixer.music.load("Sounds/Gun_sound.mpeg")
                                #pygame.time.wait(1000)
                                
                                mixer.music.set_volume(0.2)
                                mixer.music.play()
                                jugador_eliminado=i.getNombre()
                                jugadores_eliminados.append(jugador_eliminado)
                                nombres_jugadores.pop(j)
                                jugadores.pop(j)
                                num_jugadores-=1
                                #Tk().wm_withdraw() #to hide the main window
                                messagebox.showinfo('Jugador Eliminado','El jugador '+jugador_eliminado+' ha sido ejecutado')
                            j+=1
                        #juego(nombres_jugadores) #para volver a crear a los jugadores

                    else:
                        past=0
                        present=0
                        delta=0
                        accumulated=0
                        estado=True
                        pausa_button = Button(image=None, pos=(1000, 600), text_input="PAUSAR", font=get_font(40), base_color="white", hovering_color="green")
                        ventana.fill((0,0,0))
                        mixer.music.load("Sounds/cancion.mp3")
                        mixer.music.set_volume(0.2)
                        mixer.music.play()
                    
                    
                    
        
        pygame.display.update()
        reloj.tick(60)

def nombres(num_jugadores):
    # Crear una ventana
    ventana = tk.Tk()

    # Establecer el tamaño de la ventana como el tamaño de la pantalla
    ventana.geometry("{0}x{1}+0+0".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))

    # Configurar la fuente y los colores
    fuente = Font(family='Helvetica', size=16, weight='bold')
    color_fondo = '#000000' # negro
    color_letra = '#FFFFFF' # blanco
    color_boton = '#4169E1'

    # Configurar el color de fondo y letra de la ventana
    ventana.configure(bg=color_fondo)
    ventana.option_add('*Font', fuente)
    ventana.option_add('*foreground', color_letra)

    # Añadir campos de texto para los nombres de los jugadores
    tk.Label(ventana, text='Introduzca los nombres de los jugadores', font=fuente, bg=color_fondo, fg='white').pack(pady=20)

    nombres = []
    for i in range(num_jugadores):
        frame = tk.Frame(ventana, bg=color_fondo)
        frame.pack(pady=10)
        etiqueta = tk.Label(frame, text=f"Jugador {i+1}:", font=fuente, bg=color_fondo)
        etiqueta.pack(side=tk.LEFT, padx=20)
        entrada = tk.Entry(frame, font=fuente, bg=color_fondo, fg=color_letra) # fondo negro, letra blanca
        entrada.pack(side=tk.LEFT, padx=10)
        nombres.append(entrada)

    def guardar_nombres():
        for i, nombre in enumerate(nombres):
            if nombre.get().strip()=="":
                messagebox.showerror("Error", f"El campo de nombre del jugador {i+1} está vacío.")
                return
        nombres_jugadores = [nombre.get() for nombre in nombres]
        ventana.destroy()
        juego(nombres_jugadores)


        # Añadir un botón para guardar los nombres de los jugadores
    boton = tk.Button(ventana, text="Guardar", font=fuente, bg=color_boton, fg=color_letra, command=guardar_nombres)
    boton.pack(pady=20)

    # Mostrar la ventana
    ventana.mainloop()
    
def instrucciones():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        ventana.fill("white")

        TEXT= get_font(45).render("Ventana de instrucciones", True, "Black")
        RECT = TEXT.get_rect(center=(640, 260))
        ventana.blit(TEXT, RECT)

        ATRAS = Button(image=None, pos=(640, 460), text_input="ATRAS", font=get_font(75), base_color="Black", hovering_color="Green")

        ATRAS.changeColor(MOUSE_POS)
        ATRAS.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ATRAS.checkForInput(MOUSE_POS):
                    menu_principal()

        pygame.display.update()

def menu_principal():
    while True:
        ventana.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        TEXT = get_font(80).render("MENU PRINCIPAL", True, "#b68f40")
        RECT = TEXT.get_rect(center=(640, 100))

        JUGAR_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="JUGAR", font=get_font(64), base_color="#d7fcd4", hovering_color="White")
        INSTRUCCIONES_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), text_input="INSTRUCCIONES", font=get_font(41), base_color="#d7fcd4", hovering_color="White")
        SALIR_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="SALIR", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        ventana.blit(TEXT, RECT)

        for button in [JUGAR_BUTTON, INSTRUCCIONES_BUTTON, SALIR_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(ventana)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JUGAR_BUTTON.checkForInput(MOUSE_POS):
                    jugar()
                if INSTRUCCIONES_BUTTON.checkForInput(MOUSE_POS):
                    instrucciones()
                if SALIR_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principal()


'''
jugadores = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(patataCaliente(jugadores), "ganó")
'''