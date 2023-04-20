import random
import pygame,sys
from classQueue import Queue
from button import Button

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
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        ventana.fill("black")

        TEXT = get_font(45).render("Ventana Juego.", True, "White")
        RECT = TEXT.get_rect(center=(640, 260))
        ventana.blit(TEXT, RECT)

        ATRAS = Button(image=None, pos=(640, 460), text_input="ATRAS", font=get_font(75), base_color="White", hovering_color="Green")

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