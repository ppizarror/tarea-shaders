#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Permite manejar la libreria de pygame con pyopengl

# GL PYTHON
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
import pygame
from pygame.locals import *

# Constantes
_DEFAULT_CAPTION = "Program title"


def initPygame(w, h, caption=_DEFAULT_CAPTION, center_mouse=False, icon=None):
    """Inicia el modulo de pygame"""
    pygame.init()
    pygame.display.set_mode((w, h), OPENGLBLIT | DOUBLEBUF)
    pygame.display.set_caption(caption)
    if center_mouse:
        pygame.mouse.set_pos(w / 2, h / 2)
    if icon is not None:
        pygame.display.set_icon(icon)


def loadPythonImage(path, convert=False):
    """Carga una imagen en python"""
    try:
        image = pygame.image.load(path)
        if convert:
            image = image.convert_alpha()
        return image
    except:
        print "fail"
        return None


def setCaption(caption):
    """Cambia el titulo de la ventana"""
    pygame.display.set_caption(caption)
