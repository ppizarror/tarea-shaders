#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Provee funciones para dibujar planos y objetos de forma sencilla mediante opengl

# UTILS GEOMETRY
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
from OpenGL.GL import *
from utils_math import *


def drawVertexList(vertexList):
    """Dibuja una lista de puntos point2/point3"""
    if len(vertexList) >= 1:
        if vertexList[0].getType() == POINT_2:
            for vertex in vertexList:
                glVertex2fv(vertex.exportToList())
        elif vertexList[0].getType() == POINT_3:
            for vertex in vertexList:
                glVertex3fv(vertex.exportToList())
    else:
        raise Exception("lista vacia")


def drawVertexListNormal(normal, vertexList):
    """Dibuja una lista de puntos point2/point3 con una normal"""
    if len(vertexList) >= 3:
        if isinstance(normal, vector3):
            glNormal3fv(normal.exportToList())
            drawVertexList(vertexList)
        else:
            raise Exception("la normal debe ser del tipo vector3")
    else:
        raise Exceptiom("vertices insucifientes")


def drawVertexListCreateNormal(vertexList):
    """Dibuja una lista de puntos point2/point3 creando una normal"""
    if len(vertexList) >= 3:
        normal = normal3points(vertexList[0], vertexList[1], vertexList[2])
        drawVertexListNormal(normal, vertexList)
    else:
        raise Exceptiom("vertices insucifientes")


def drawVertexList_textured(vertexList, tvertexList):
    """Dibuja una lista de puntos point2/point3 con una lista point2 de aristas
    para modelos texturados"""
    if len(vertexList) >= 1:
        if vertexList[0].getType() == POINT_2:
            for vertex in range(len(vertexList)):
                glTexCoord2fv(tvertexList[vertex].exportToList())
                glVertex2fv(vertexList[vertex].exportToList())
        elif vertexList[0].getType() == POINT_3:
            for vertex in range(len(vertexList)):
                glTexCoord2fv(tvertexList[vertex].exportToList())
                glVertex3fv(vertexList[vertex].exportToList())
        else:
            raise Exception("el tipo de vertexList debe ser POINT2 o POINT3")
    else:
        raise Exception("lista vacia")


def drawVertexListNormal_textured(normal, vertexList, tvertexList):
    """Dibuja una lista de puntos point2/point3 con una lista point2 de aristas
    para modelos texturados con una normal"""
    if len(vertexList) >= 1:
        if len(tvertexList) >= 3:
            if isinstance(normal, vector3):
                glNormal3fv(normal.exportToList())
                drawVertexList_textured(vertexList, tvertexList)
            else:
                raise Exception("la normal debe ser del tipo vector3")
        else:
            raise Exception("vertices insuficientes")
    else:
        raise Exception("lista vacia")


def drawVertexListCreateNormal_textured(vertexList, tvertexList):
    """Dibuja una lista de puntos point3 con una lista point2 de aristas para modelos
    texturados creando una normal"""
    if len(vertexList) >= 3:
        normal = normal3points(vertexList[0], vertexList[1], vertexList[2])
        drawVertexListNormal_textured(normal, vertexList, tvertexList)
    else:
        raise Exception("vertices insuficientes")


def drawList(lista, pos=[0.0, 0.0, 0.0], angle=0.0, rot=None, sz=None, rgb=None):
    """Dibuja una lista"""
    glPushMatrix()
    glTranslate(pos[0], pos[1], pos[2])
    if sz is not None: glScale(sz[0], sz[1], sz[2])
    if rot is not None: glRotatef(angle, rot[0], rot[1], rot[2])
    if rgb is not None: glColor4fv(rgb)
    glCallList(lista)
    glPopMatrix()
