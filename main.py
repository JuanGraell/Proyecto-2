from Patata_Caliente import *

pygame.init()

#"""Las medidas de la ventana del juego."""
height=1280
widht=720

#"""Crea la ventana del juego con las medidas."""
ventana = pygame.display.set_mode((height,widht))

#""" Fondo y Caption"""
BG = pygame.image.load("assets/Background.png")
pygame.display.set_caption("Papa Caliente")

menu_principal(ventana,BG)