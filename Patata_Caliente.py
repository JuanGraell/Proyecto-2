import random
import pygame,sys
from classQueue import Queue
from button import Button
import sys
import player
import math
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


def pausar():
    pass

def continuar():
    pass

def juego(nombres_jugadores):
    num_jugadores = len(nombres_jugadores)
    pygame.init()
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

    while True:
        # Crear el título con la fuente
        text = get_font(36).render(f"Jugadores: {num_jugadores}", True, "white")
        rect = text.get_rect(center=(640, 50))
        ventana.blit(text, rect)

        MOUSE_POS = pygame.mouse.get_pos()


         # Dibujar los círculos de los jugadores
        radio = 50
        if (num_jugadores==2):
            separacion=800
        elif(num_jugadores==3):
            separacion=450
        elif(num_jugadores==4):
            separacion=300
        elif(num_jugadores==5):
            separacion=225
        elif(num_jugadores==6):
            separacion = 170
        x_ini = 200
        y = 300
        for i in range(num_jugadores):
            x = x_ini + i*separacion
            pygame.draw.circle(ventana, "white", (x, y), radio)
            font = get_font(18)  # Obtener la fuente
            nombre = nombres_jugadores[0]  # Obtener el nombre del primer jugador
            text = get_font(20).render(nombres_jugadores[i], True, "white")
            rect = text.get_rect(center=(x, y-60))  # Obtener el rectángulo de la superficie de texto
            ventana.blit(text, rect)  # Dibujar la superficie de texto sobre la ventana



        # Crear el botón de salir
        salir_button = Button(image=None, pos=(240, 600), text_input="SALIR", font=get_font(40), base_color="white", hovering_color="red")

        salir_button.changeColor(MOUSE_POS)
        salir_button.update(ventana)

        pausa_button = Button(image=None, pos=(1000, 600), text_input="PAUSAR", font=get_font(40), base_color="white", hovering_color="green")

        pausa_button.changeColor(MOUSE_POS)
        pausa_button.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if salir_button.checkForInput(MOUSE_POS):
                    #mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                if pausa_button.checkForInput(MOUSE_POS):
                    mixer.music.pause()

        pygame.display.update()

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