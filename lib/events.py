#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Este archivo contiene funciones que manejan los eventos de la aplicacion

# EVENTS
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
import pygame
from pygame.locals import *

from constants import *


def handleEvents(camera, light1, light2, program, model):
    """Maneja los eventos de la aplicacion"""
    for event in pygame.event.get():
        if event.type == QUIT:  # Cierra la aplicacion
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # Cierra la aplicacion
                exit()
            elif event.key == K_F1:  # Muestra la informacion de la camara
                print camera
            elif event.key == K_m:  # Cambia el color a la luz orbital
                light2.modifyPropertie(PROPERTIE_COLOR, 1, OPERATOR_ADD)
                light2.modifyPropertie(PROPERTIE_COLOR, light2.getPropertie(PROPERTIE_TOTAL_COLORS), OPERATOR_MOD)
                light2.execFunc("light_color_{0}".format(light2.getPropertie("color")))
            elif event.key == K_p:  # Toggle del shader
                program[0] = (program[0] + 1) % (len(program) - 1)
            elif event.key == K_n:  # Cambia el color al sol
                light1.modifyPropertie(PROPERTIE_COLOR, 1, OPERATOR_ADD)
                light1.modifyPropertie(PROPERTIE_COLOR, light1.getPropertie(PROPERTIE_TOTAL_COLORS), OPERATOR_MOD)
                light1.execFunc("light_color_{0}".format(light1.getPropertie("color")))
            elif event.key == K_o:  # Activa / desactiva el shader
                if program[program[0] + 1].getStatus():
                    program[program[0] + 1].disable()
                else:
                    program[program[0] + 1].enable()
            elif event.key == K_r:  # Reestablece la camara
                camera.setPhi(CAMERA_PHI)
                camera.setTheta(CAMERA_THETA)
                camera.setRadius(CAMERA_RAD)
            elif event.key == K_t:  # Toggle del modelo
                model.modifyPropertie(PROPERTIE_MODEL_SELECTED, 1, OPERATOR_ADD)
                model.modifyPropertie(PROPERTIE_MODEL_SELECTED, MODELS, OPERATOR_MOD)
            elif event.key == K_c:  # Toggle del material del modelo
                model.modifyPropertie(PROPERTIE_MATERIAL_SELECTED, 1, OPERATOR_ADD)
                model.modifyPropertie(PROPERTIE_MATERIAL_SELECTED, model.getPropertie(PROPERTIE_MATERIAL_TOTAL),
                                      OPERATOR_MOD)
            elif event.key == K_b:  # Aumenta el paralaje
                model.modifyPropertie(PROPERTIE_MODEL_PARALLAX, 0.005, OPERATOR_ADD)
            elif event.key == K_v:  # Disminuye el paralaje
                model.modifyPropertie(PROPERTIE_MODEL_PARALLAX, 0.005, OPERATOR_DIFF)
                if model.getPropertie(PROPERTIE_MODEL_PARALLAX) < 0.01:
                    model.modifyPropertie(PROPERTIE_MODEL_PARALLAX, 0.0)

    # Comprueba las teclas presionadas
    keys = pygame.key.get_pressed()
    # Rotar la camara en el eje X
    if keys[K_w]:
        camera.rotateX(CAMERA_ROT_VEL)
    elif keys[K_s]:
        camera.rotateX(-CAMERA_ROT_VEL)
    # Rotar la camara en el eje Y
    if keys[K_a]:
        camera.rotateY(-CAMERA_ROT_VEL)
    elif keys[K_d]:
        camera.rotateY(CAMERA_ROT_VEL)
    # Rotar la camara en el eje Z
    if keys[K_q]:
        camera.rotateZ(-CAMERA_ROT_VEL)
    elif keys[K_e]:
        camera.rotateZ(CAMERA_ROT_VEL)
    # Acerca / aleja la camara
    if keys[K_n]:
        camera.close()
    elif keys[K_m]:
        camera.far()
    # Rota la luz 1 (sol)
    if keys[K_UP]:
        light1.rotateZ(LIGHT_SUN_ANG_VEL)
    elif keys[K_DOWN]:
        light1.rotateZ(-LIGHT_SUN_ANG_VEL)
    # Mueve la luz 2 (orbital)
    if keys[K_LEFT]:
        light2.moveY(-LIGHT_ORBITAL_DESPLY_DELTA)
    elif keys[K_RIGHT]:
        light2.moveY(LIGHT_ORBITAL_DESPLY_DELTA)
