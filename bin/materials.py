#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Provee funciones para aplicar distintos materiales

# MATERIALS
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
from OpenGL.GL import *

# Constantes
DEFAULT_EMISSION = [0.0, 0.0, 0.0, 1.0]
WHITE_EMISSION = [1.0, 1.0, 1.0, 1.0]

# def material_template(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
#    """Material de """
#    glMaterialfv(face, GL_AMBIENT, [0., 0., 0., 1.0])
#    glMaterialfv(face, GL_DIFFUSE, [0., 0., 0., 1.0])
#    glMaterialfv(face, GL_SPECULAR, [0., 0., 0., 1.0])
#    glMaterialfv(face, GL_SHININESS, 0. * 128)
#    glMaterialfv(face, GL_EMISSION, emission)


def material_obsidian(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de obsidiana"""
    glMaterialfv(face, GL_SPECULAR, [0.332741, 0.328634, 0.346435, 1.0])
    glMaterialfv(face, GL_AMBIENT, [0.05375, 0.05, 0.0625, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.18275, 0.17, 0.25525, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.3 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_silver(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plata"""
    glMaterialfv(face, GL_AMBIENT, [0.19225, 0.19225, 0.19225, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.50754, 0.50754, 0.50754, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.508273, 0.508273, 0.508273, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.4 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_copper(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de cobre"""
    glMaterialfv(face, GL_AMBIENT, [0.19125, 0.0735, 0.0225, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.7038, 0.27048, 0.0828, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.256777, 0.137622, 0.086014, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.1 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_esmerald(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de esmeralda"""
    glMaterialfv(face, GL_AMBIENT, [0.0215, 0.1745, 0.0215, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.07568, 0.61424, 0.007568, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.633, 0.727811, 0.633, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.6 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_jade(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de jade"""
    glMaterialfv(face, GL_AMBIENT, [0.135, 0.2225, 0.1575, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.54, 0.89, 0.63, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.316228, 0.316228, 0.316228, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.1 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_pearl(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de perla"""
    glMaterialfv(face, GL_AMBIENT, [0.25, 0.20725, 0.20725, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [1.0, 0.829, 0.829, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.296648, 0.296648, 0.296648, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.088 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_turquoise(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de turquesa"""
    glMaterialfv(face, GL_AMBIENT, [0.1, 0.18725, 0.1745, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.396, 0.74161, 0.69102, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.29754, 0.30829, 0.306678, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.1 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_ruby(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de rubi"""
    glMaterialfv(face, GL_AMBIENT, [0.1745, 0.01175, 0.01175, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.61424, 0.04136, 0.04136, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.727811, 0.626959, 0.626959, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.6 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_brass(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de laton"""
    glMaterialfv(face, GL_AMBIENT, [0.329, 0.223529, 0.027451, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.780392, 0.568627, 0.113725, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.992157, 0.941176, 0.807843, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.21794872 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_bronze(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de bronce"""
    glMaterialfv(face, GL_AMBIENT, [0.2125, 0.1275, 0.054, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.714, 0.4284, 0.18144, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.393548, 0.271906, 0.166721, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.2 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_chrome(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de cromo"""
    glMaterialfv(face, GL_AMBIENT, [0.25, 0.25, 0.25, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.4, 0.4, 0.4, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.774597, 0.774957, 0.774957, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.6 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_gold(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de oro"""
    glMaterialfv(face, GL_AMBIENT, [0.24725, 0.1995, 0.0745, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.75164, 0.60648, 0.22648, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.628281, 0.555802, 0.366065, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.4 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_black_plastic(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plastico negro"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.01, 0.01, 0.01, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.50, 0.50, 0.50, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.25 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_cyan_plastic(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plastico celeste"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.1, 0.06, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.0, 0.50980392, 0.50980392, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.50196078, 0.50196078, 0.50196078, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.25 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_green_plastic(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plastico verde"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.1, 0.35, 0.1, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.45, 0.55, 0.45, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.25 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_red_plastic(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plastico rojo"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.5, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.7, 0.6, 0.6, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.25 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_white_plastic(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plastico blanco"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.55, 0.55, 0.55, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.70, 0.70, 0.70, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.25 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_yellow_plastic(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de plastico amarillo"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.5, 0.5, 0.0, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.6, 0.6, 0.5, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.25 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_black_rubber(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de goma negro"""
    glMaterialfv(face, GL_AMBIENT, [0.02, 0.02, 0.02, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.01, 0.01, 0.1, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.4, 0.4, 0.4, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.078125 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_cyan_rubber(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de goma celeste"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.05, 0.05, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.4, 0.5, 0.5, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.04, 0.7, 0.7, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.078125 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_green_rubber(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de goma verde"""
    glMaterialfv(face, GL_AMBIENT, [0.0, 0.05, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.4, 0.5, 0.4, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.04, 0.7, 0.04, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.078125 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_red_rubber(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de goma rojo"""
    glMaterialfv(face, GL_AMBIENT, [0.05, 0.0, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.5, 0.4, 0.4, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.7, 0.04, 0.04, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.078125 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_white_rubber(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de goma blanco"""
    glMaterialfv(face, GL_AMBIENT, [0.05, 0.05, 0.05, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.7, 0.7, 0.7, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.078125 * 128)
    glMaterialfv(face, GL_EMISSION, emission)


def material_yellow_rubber(emission=DEFAULT_EMISSION, face=GL_FRONT_AND_BACK):
    """Material de goma amarillo"""
    glMaterialfv(face, GL_AMBIENT, [0.05, 0.05, 0.0, 1.0])
    glMaterialfv(face, GL_DIFFUSE, [0.5, 0.5, 0.4, 1.0])
    glMaterialfv(face, GL_SPECULAR, [0.7, 0.7, 0.04, 1.0])
    glMaterialfv(face, GL_SHININESS, 0.078125 * 128)
    glMaterialfv(face, GL_EMISSION, emission)
