#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Permite cargar las librerias de opengl y iniciar el sistema

# OPENGL
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de liberias
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from utils import *

# Definicion de constantes
_OPENGL_CONFIGS = [False]
DEFAULT_AMBIENT_COLOR = [0.2, 0.2, 0.2, 1.0]
DEFAULT_BGCOLOR = [0.0, 0.0, 0.0, 1.0]
DEFAULT_BGDEPTH = 1.0
DEFAULT_CONSTANT_ATTENUATION = 1.0
DEFAULT_DIFFUSE_COLOR = [0.8, 0.8, 0.8, 1.0]
DEFAULT_LINEAR_ATTENUATION = 0.0
DEFAULT_QUADRATIC_ATTENUATION = 0.0
DEFAULT_SPECULAR_COLOR = [1.0, 1.0, 1.0, 1.0]
DEFAULT_SPOT_CUTOFF = 180
DEFAULT_SPOT_DIRECTION = [0.0, 0.0, -1.0, 1.0]
DEFAULT_SPOT_EXPONENT = 0
SPOT_DIRECTION_ALL = [1.0, 1.0, 1.0, 1.0]


def initGl(**kwargs):
    """Inicia opengl
    Parametros validos:\n
    antialiasing=true/false (activa el antialiasing, true por defecto)\n
    bgcolor=color de fondo\n
    bgdepth=profundidad de dibujo\n
    depth=true/false (activa el depth map, true por defecto)\n
    height=alto de la ventana\n
    lighting=true/false (activa la iluminacion, false por defecto)\n
    materialcolor=true/false (activa el color natural de los materiales, true por defecto)\n
    normalized=true/false (normaliza las normales, true por defecto)\n
    numlights=1..9 (indica el numero de luces a activar, 0 por defecto)\n
    perspectivecorr=true/false (activa la correccion de perspectiva, false por defecto)\n
    polygonfillmode=true/false (indica el rellenar las superficies, true por defecto)\n
    smooth=true/false (activa el dibujado suave, true por defecto)\n
    surffil=true/false (activa el rellenado de superficies, true por defecto)\n
    textures=true/false (activa las texturas, false por defecto)\n
    transparency=true/false (activa la transparencia de los modelos, true por defecto)\n
    verbose=true/false (activa el logging, false por defecto)\n
    version=true/false (imprime la version en pantalla de OpenGL, false por defecto)\n
    width=ancho de la ventana
    """

    global verbose

    def isTrue(value):
        """Indica si el valor es true o false"""
        if kwargs.get(value) is not None:
            return kwargs.get(value)
        else:
            return False

    # Se define el verbose
    if isTrue("verbose"):
        verbose = True
    else:
        verbose = False

    def log(msg):
        """Imprime un mensaje en pantalla"""
        if verbose:
            print "[GL] {0}".format(msg)

    def logInfo(msg):
        """Imprime una informacion en pantalla"""
        print "[GL-INFO] {0}".format(msg)

    log("Iniciando OPENGL")

    # Imprime la version de opengl
    if isTrue("version"):
        logInfo("GPU {0}".format(glGetString(GL_VENDOR)))
        logInfo("Renderer {0}".format(glGetString(GL_RENDERER)))
        logInfo("OpenGL version {0}".format(glGetString(GL_VERSION)))
        logInfo("SLSL version {0}".format(glGetString(GL_SHADING_LANGUAGE_VERSION)))
        logInfo("Extensions {0}".format(glGetString(GL_EXTENSIONS)))

    # Se define el color de dibujo
    if kwargs.get("bgcolor") is not None:
        log("Se definio el color de fondo: {0}".format(kwargs.get("bgcolor")))
        glClearColor(*kwargs.get("bgcolor"))
    else:
        log("Se definio el color de fondo por defecto")
        glClearColor(*DEFAULT_BGCOLOR)

    # Se define la profundidad del color de fondo
    if kwargs.get("bgdepth") is not None:
        log("Se definio la profundidad de color en: {0}".format(kwargs.get("bgdepth")))
        glClearDepth(kwargs.get("bgdepth"))
    else:
        log("Se definio la profundidad de color por defecto")
        glClearDepth(DEFAULT_BGDEPTH)

    # Se activa la transparencia
    if isTrue("transparency"):
        log("Se activo la transparencia")
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    else:
        log("Transparencia desactivada")

    # Se activan los rellenos suaves
    if isTrue("smooth"):
        log("Se activa el modo de shading SMOOTH")
        glShadeModel(GL_SMOOTH)
    else:
        log("Se desactivan los rellenos suaves")

    # Se activa el depth test
    if isTrue("depth"):
        log("Se activa el deph test")
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
    else:
        log("Se desactiva el deph test")

    # Se activa el antialiasing
    if isTrue("antialiasing"):
        log("Se activa el antialiasing")
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    else:
        log("Se desactiva el antialiasing")

    # Se activa el normalizado de normales
    if isTrue("normalized"):
        log("Se activa el normalizado de normales")
        glEnable(GL_NORMALIZE)
    else:
        log("Se desactiva el normalizado de normales")

    # Se activa el rellenado de superficies
    if isTrue("surffill"):
        log("Se activa el relleno de superficies")
        glEnable(GL_POLYGON_OFFSET_FILL)
    else:
        log("Se desactiva el relleno de superficies")

    # Se activa la iluminacion
    if kwargs.get("lighting") is not None and kwargs.get("lighting"):
        log("Se activa la iluminacion")
        glEnable(GL_LIGHTING)

        # Se activan las luces
        if kwargs.get("numlights") is not None:
            total = int(kwargs.get("numlights"))
            for light in range(total):
                log("Luz {0} activada".format(light))
                eval("glEnable(GL_LIGHT{0})".format(light))
        _OPENGL_CONFIGS[0] = True
    else:
        log("Se desactiva la iluminacion")

    # Modo de pintado
    if isTrue("polygonfillmode"):
        log("Se activa el relleno poligonal por ambas caras")
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        log("Se activa el relleno poligonal en una sola cara")

    # Se activa el color de los materiales
    if isTrue("materialcolor"):
        log("Se activa el color de materiales")
        glEnable(GL_COLOR_MATERIAL)
    else:
        log("Se desactiva el color de materiales")

    # Se activa la correccion de la matriz de perspectiva
    if isTrue("perspectivecorr"):
        log("Se activa la correccion de perspectivas")
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    else:
        log("Se desactiva la correccion de perspectivas")

    # Se activan las texturas
    if isTrue("textures"):
        log("Se activan las texturas")
        glEnable(GL_TEXTURE_2D)
        glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    else:
        log("Se desactivan las texturas")

    log("Ha terminado la configuracion de OPENGL")


def clearBuffer():
    """Borra el buffer"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def reshape(w, h, fov=60, nearplane=300.0, farplane=20000.0):
    """Maneja la pantalla de OPENGL"""
    h = max(h, 1)
    glLoadIdentity()

    # Se crea el viewport
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)

    # Se deja la camara en perspectiva
    gluPerspective(fov, float(w) / float(h), nearplane, farplane)

    # Se deja el modo en modelo
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def initLight(light=GL_LIGHT0, *args, **kwargs):
    """Define las propiedades de iluminacion, forma de uso
    light: luz a iniciar, del tipo GL_LIGHTn con n=0..8

    parametros validos:\n
    ambient: color ambiente rgba\n
    diffuse: color difuso rgba\n
    specular: color especular rgba\n
    spot_cutoff: angulo de enfoque\n
    spot_exponent: exponente del enfoque\n
    spot_direction: direccion de enfoque\n
    constant_att: atenuacion constante\n
    linear_att: atenuacion linear\n
    quad_att: atenuacion cuadratica\n
    """

    # Se define el color ambiente
    if kwargs.get("ambient") is not None:
        glLightfv(light, GL_AMBIENT, kwargs.get("ambient"))
    else:
        glLightfv(light, GL_AMBIENT, DEFAULT_AMBIENT_COLOR)

    # Se define el color difuso
    if kwargs.get("diffuse") is not None:
        glLightfv(light, GL_DIFFUSE, kwargs.get("diffuse"))
    else:
        glLightfv(light, GL_DIFFUSE, DEFAULT_DIFFUSE_COLOR)

    # Se define el color especular
    if kwargs.get("specular") is not None:
        glLightfv(light, GL_SPECULAR, kwargs.get("specular"))
    else:
        glLightfv(light, GL_SPECULAR, DEFAULT_SPECULAR_COLOR)

    # Se define el angulo de enfoque
    if kwargs.get("spot_cutoff") is not None:
        glLightfv(light, GL_SPOT_CUTOFF, kwargs.get("spot_cutoff"))
    else:
        glLightfv(light, GL_SPOT_CUTOFF, DEFAULT_SPOT_CUTOFF)

    # Se define el exponente
    if kwargs.get("spot_exponent") is not None:
        glLightfv(light, GL_SPOT_EXPONENT, kwargs.get("spot_exponent"))
    else:
        glLightfv(light, GL_SPOT_EXPONENT, DEFAULT_SPOT_EXPONENT)

    # Se define la direccion de enfoque
    if kwargs.get("spot_direction") is not None:
        glLightfv(light, GL_SPOT_DIRECTION, kwargs.get("spot_direction"))
    else:
        glLightfv(light, GL_SPOT_DIRECTION, DEFAULT_SPOT_DIRECTION)

    # Se define la atenuacion constante
    if kwargs.get("constant_att") is not None:
        glLightfv(light, GL_CONSTANT_ATTENUATION, kwargs.get("constant_att"))
    else:
        glLightfv(light, GL_CONSTANT_ATTENUATION, DEFAULT_CONSTANT_ATTENUATION)

    # Se define la atenuacion lineal
    if kwargs.get("linear_att") is not None:
        glLightfv(light, GL_LINEAR_ATTENUATION, kwargs.get("linear_att"))
    else:
        glLightfv(light, GL_LINEAR_ATTENUATION, DEFAULT_LINEAR_ATTENUATION)

    # Se define la atenuacion cuadratica
    if kwargs.get("quad_att") is not None:
        glLightfv(light, GL_QUADRATIC_ATTENUATION, kwargs.get("quad_att"))
    else:
        glLightfv(light, GL_QUADRATIC_ATTENUATION, DEFAULT_QUADRATIC_ATTENUATION)


def islightEnabled():
    """Retorna true/false si la luz esta activada o desactivada"""
    return _OPENGL_CONFIGS[0]
