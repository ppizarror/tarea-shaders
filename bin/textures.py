#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Provee funciones utilitarias para el manejo de texturas

# TEXTURES
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
from OpenGL.GL import *
import numpy

try:
    from PIL import Image
except ImportError:
    print "[ERR] Error al importar la libreria, probando Image"
    try:
        import Image
    except:
        print "[ERR] Error al importar Image, esta aplicacion requiere de PIL"
        exit()


def loadTexture(imageFile, repeat=False):
    """Carga una textura desde un archivo t"""
    img = Image.open(imageFile)
    data = numpy.array(list(img.getdata()), numpy.int8)

    tex = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBindTexture(GL_TEXTURE_2D, tex)

    if repeat:
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    else:
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, data)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    return tex
