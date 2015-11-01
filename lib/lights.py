#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Este archivo contiene las funciones que modifican las luces del programa

# LIGHTS
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
from constants import *


def light_color_0(initFun, lightSource):
    """Luz blanca"""
    initFun(lightSource)


def light_color_1(initFun, lightSource):
    """Luz roja"""
    initFun(lightSource, ambient=AMBIENT_COLOR_RED, diffuse=DIFFUSE_COLOR_RED, specular=SPECULAR_COLOR_RED)


def light_color_2(initFun, lightSource):
    """Luz morada"""
    initFun(lightSource, ambient=AMBIENT_COLOR_PURPLE, diffuse=DIFFUSE_COLOR_PURPLE, specular=SPECULAR_COLOR_PURPLE)


def light_color_3(initFun, lightSource):
    """Luz verde"""
    initFun(lightSource, ambient=AMBIENT_COLOR_GREEN, diffuse=DIFFUSE_COLOR_GREEN, specular=SPECULAR_COLOR_GREEN)


def light_color_4(initFun, lightSource):
    """Luz amarilla"""
    initFun(lightSource, ambient=AMBIENT_COLOR_YELLOW, diffuse=DIFFUSE_COLOR_YELLOW, specular=SPECULAR_COLOR_YELLOW)
