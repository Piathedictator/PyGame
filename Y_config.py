#Größen und Farben, sowie Schriftformate die in allen Dateien verwendet werden
import pygame

width, height = 600, 600
screen = pygame.display.set_mode((width, height))

WHITE, BLUE, GRAY, PINK, YELLOW, BLACK = ((255, 255, 255), (173, 216, 230), (180, 180, 180),(255, 0, 255), (255, 255, 102), (0, 0, 0))
font = pygame.font.Font(None, 50)
font_titel = pygame.font.Font(None, 70)
font_instruction = pygame.font.Font(None, 30)