#Größen und Farben, sowie Schriftformate die in allen Dateien verwendet werden
import pygame
import os
import sys
pygame.init
pygame.font.init()

#Größe des Screens
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#Verwendete Farben
# Farben als RGB-Werte
LIGHT_RED = (255, 102, 102)  # Helles Rot  
RED = (255, 0, 0)            # Standard Rot  
GREEN = (0, 255, 0)      # Grün
BLUE = (0, 0, 255)       # Blau
YELLOW = (255, 255, 0)   # Gelb
CYAN = (0, 255, 255)     # Cyan (Türkis)
PINK = (255, 0, 255)  # Magenta (Pink)
ORANGE = (255, 165, 0)   # Orange
PURPLE = (128, 0, 128)   # Lila
BROWN = (139, 69, 19)    # Braun
WHITE = (255, 255, 255)  # Weiß
BLACK = (0, 0, 0)        # Schwarz 
GRAY = (128, 128, 128)        # Mittleres Grau  

#Schatten:
SHADOW_OFFSET = 3
SHADOW_COLOR = (0, 0, 0)

# Schriftarten

FONT_30 = pygame.font.Font(None, 30) 
FONT_40 = pygame.font.Font(None, 40) 
FONT_50 = pygame.font.Font(None, 50)
FONT_60 = pygame.font.Font(None, 50)
FONT_70 = pygame.font.Font(None, 70)
FONT_A = pygame.font.SysFont('arial', 40)

