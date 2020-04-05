#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Archivo principal de la tarea, crea luces, modelos y ejecuta los shaders

# CAMERA
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
from bin import materials
from bin.camera import *
from bin.figures import *
from bin.glpython import *
from bin.materials import *
from bin.opengl_lib import *
from bin.particles import *
from bin.shader import *
from bin.textures import loadTexture
from bin.utils import *
from lib.constants import *
from lib.events import *
from lib.lights import *


# Inicio de librerias
initPygame(WINDOWS_SIZE[0], WINDOWS_SIZE[1], "Shaders", loadPythonImage(PATH_IMAGES + "icon.png"))
initGl(transparency=False, materialcolor=False, normalized=True, lighting=True, numlights=NUM_LIGHTS,
       perspectivecorr=True, antialiasing=True, depth=True, smooth=True, texture=True, verbose=False)
reshape(*WINDOWS_SIZE)
initLight(GL_LIGHT0)
initLight(GL_LIGHT1)
material_functions = []
for elem in dir(materials):  # Se obtienen todas las funciones de material
    if "material" in elem: material_functions.append(elem)

# Definicion de objetos
axis = createAxes(AXES_LENGTH)  # Ejes
camera = CameraR(CAMERA_RAD, CAMERA_PHI, CAMERA_THETA)  # Camara del tipo esferica
clock = pygame.time.Clock()  # Reloj del juego
light_orbital = Particle(500, 0, 500)  # Luz orbital
light_sol = Particle(-500, 500, 500)  # Luz sol
model = Particle()  # modelo
textures = [
    loadTexture(TEXTURE_BRICK, True),
    loadTexture(TEXTURE_BRICK_NORMAL, True),
    loadTexture(TEXTURE_BRICK_BUMP, True)]
textures2 = [
    loadTexture(TEXTURE_DOTS, False),
    loadTexture(TEXTURE_DOTS_NORMAL, False),
    loadTexture(TEXTURE_DOTS_BUMP, False)]
textures3 = [
    loadTexture(TEXTURE_METAL, False),
    loadTexture(TEXTURE_METAL_NORMAL, False),
    loadTexture(TEXTURE_METAL_BUMP, False)]
textures4 = [
    loadTexture(TEXTURE_WATER, False),
    loadTexture(TEXTURE_WATER_NORMAL, False),
    loadTexture(TEXTURE_WATER_BUMP, False)]
texture_num = 3

# Se cargan los shaders
program = [0, loadShader(PATH_SHADERS, "phongShader", [NUM_LIGHTS], [texture_num, NUM_LIGHTS]),
           loadShader(PATH_SHADERS, "normalMap", [NUM_LIGHTS], [texture_num, NUM_LIGHTS]),
           loadShader(PATH_SHADERS, "parallax", [NUM_LIGHTS], [texture_num, NUM_LIGHTS])]
program[1].setName("Phong Shading")
program[2].setName("Normal Mapping")
program[3].setName("Parallax Shader")

# Configuracion de objetos
camera.setName("Camara principal")
light_orbital.setName("Luz orbital")
light_orbital.setAngVelY(LIGHT_ORBITAL_ANG_VEL, True)  # Se define la velocidad angular
light_orbital.addPropertie(PROPERTIE_COLOR, COLOR_START)  # Define el color actual
light_orbital.addPropertie(PROPERTIE_TOTAL_COLORS, COLOR_MAX)  # Define el total de colores
light_orbital.bind(light_color_0, False, [initLight, GL_LIGHT1])  # Agrega las funciones a la particula
light_orbital.bind(light_color_1, False, [initLight, GL_LIGHT1])
light_orbital.bind(light_color_2, False, [initLight, GL_LIGHT1])
light_orbital.bind(light_color_3, False, [initLight, GL_LIGHT1])
light_orbital.bind(light_color_4, False, [initLight, GL_LIGHT1])
light_sol.setName("Sol")
light_sol.addPropertie(PROPERTIE_COLOR, COLOR_START)  # Define el color actual
light_sol.addPropertie(PROPERTIE_TOTAL_COLORS, COLOR_MAX)  # Define el total de colores
light_sol.bind(light_color_0, False, [initLight, GL_LIGHT0])  # Agrega las funciones a la particula
light_sol.bind(light_color_1, False, [initLight, GL_LIGHT0])
light_sol.bind(light_color_2, False, [initLight, GL_LIGHT0])
light_sol.bind(light_color_3, False, [initLight, GL_LIGHT0])
light_sol.bind(light_color_4, False, [initLight, GL_LIGHT0])
model.setName("Modelo")
model.addPropertie(PROPERTIE_MODEL_SELECTED, MODEL_START)
model.addPropertie(PROPERTIE_MODEL_TOTALS, MODELS)
model.addPropertie(PROPERTIE_MODEL,
                   [create_sphere(100, 100), create_cube(), create_piramid_vbo(800.0), create_tetrahedron_vbo(800.0),
                    create_teapot(), loadGMSHModel(PATH_MESHES + "tuerca.msh", 20.0, 0, -3500, 0, True, True),
                    loadGMSHModel(PATH_MESHES + "carpeta.msh", 500.0, -250, -250, 0, True, False),
                    loadGMSHModel(PATH_MESHES + "esfera.msh", 800.0, 0, 0, 0, False, False),
                    loadGMSHModel(PATH_MESHES + "esfera.msh", 800.0, 0, 0, 0, True, False),
                    create_torus(0.4, 0.8, 100, 100), create_cube_textured(textures), create_cube_textured(textures3),
                    create_cube_textured(textures2), create_cube_textured(textures4), create_teapot_textured(textures),
                    create_piramid_textured(textures2)])
model.addPropertie(PROPERTIE_MODEL_TYPES,
                   [FIGURE_LIST, FIGURE_LIST, FIGURE_VBO, FIGURE_VBO, FIGURE_LIST, FIGURE_VBO, FIGURE_VBO, FIGURE_VBO, \
                    FIGURE_VBO, FIGURE_LIST, FIGURE_LIST, FIGURE_LIST, FIGURE_LIST, FIGURE_LIST, FIGURE_LIST,
                    FIGURE_LIST])
for function in material_functions: model.bind(eval(function), False)
model.addPropertie(PROPERTIE_MATERIAL_SELECTED, material_functions.index(MATERIAL_START))
model.addPropertie(PROPERTIE_MATERIAL_NAMES, material_functions)
model.addPropertie(PROPERTIE_MODEL_LIGHT, create_sphere(100, 100))
model.addPropertie(PROPERTIE_MATERIAL_TOTAL, len(material_functions))
model.addPropertie(PROPERTIE_MODEL_NAMES,
                   ["Esfera glut", "Cubo glut", "Piramide vbo", "Tetraedro vbo", "Teapot glut", "Tuerca gmsh",
                    "Carpeta gmsh", "Esfera gmsh, normales sin promediar", "Esfera gmsh, normales promediadas",
                    "Torus glut", "Cubo texturado ladrilllo", "Cubo texturado metalico", "Cubo texturado puntos",
                    "Cubo texturado agua", "Teapot texturado", "Piramide texturada"])
model.addPropertie(PROPERTIE_MODEL_TEXTURES, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
model.addPropertie(PROPERTIE_MODEL_PARALLAX, PARALLAX)

# Bucle principal
while True:
    clock.tick(FPS)
    clearBuffer()
    camera.place()
    handleEvents(camera, light_sol, light_orbital, program, model)
    if SHOW_AXIS:
        if islightEnabled():
            glDisable(GL_LIGHTING)
            glCallList(axis)
            glEnable(GL_LIGHTING)
        else:
            glCallList(axis)
    time = clock.get_time() / 1000.0

    # Actualiza las particulas
    light_sol.update()
    light_orbital.update()
    model.update()

    # Posiciona las luces
    material_silver()
    glLightfv(GL_LIGHT0, GL_POSITION, light_sol.getList())
    drawList(model.getPropertie(PROPERTIE_MODEL_LIGHT), light_sol.getList(), 0, None, LIGHT_SUN_SIZE, None)
    glLightfv(GL_LIGHT1, GL_POSITION, light_orbital.getList())
    drawList(model.getPropertie(PROPERTIE_MODEL_LIGHT), light_orbital.getList(), 0, None, LIGHT_SUN_SIZE, None)

    # Inicia el shader
    program[program[0] + 1].start()

    # Carga el modelo
    textured = model.getPropertieList(PROPERTIE_MODEL_TEXTURES, model.getPropertie(PROPERTIE_MODEL_SELECTED))
    program[program[0] + 1].uniformi('toggletexture', textured)
    program[program[0] + 1].uniformi('togglebump', textured)
    program[program[0] + 1].uniformi('toggleparallax', textured)
    program[program[0] + 1].uniformf('parallaxheight', model.getPropertie(PROPERTIE_MODEL_PARALLAX))
    if not textured:
        if program[program[0] + 1].getStatus():
            glDisable(GL_TEXTURE_2D)
    else:
        for i in range(texture_num):
            program[program[0] + 1].uniformi('texture[{0}]'.format(i), i)
    material = model.getPropertieList(PROPERTIE_MATERIAL_NAMES, model.getPropertie(PROPERTIE_MATERIAL_SELECTED))
    model.execFunc(material)  # Carga el material
    objList = model.getPropertieList(PROPERTIE_MODEL,
                                     model.getPropertie(PROPERTIE_MODEL_SELECTED))  # Obtiene el objeto
    objName = model.getPropertieList(PROPERTIE_MODEL_NAMES, model.getPropertie(PROPERTIE_MODEL_SELECTED))  # Nombre
    materialTitle = str(material).replace("material_", "").title().replace("_", " ")
    shaderName = program[program[0] + 1].getName()
    if shaderName == "Parallax Shader":
        shaderName += " - height: {0}".format(model.getPropertie(PROPERTIE_MODEL_PARALLAX))
    setCaption("Modelo: {0}, Material : {1}, Shader: {2}".format(objName, materialTitle, shaderName))

    # Dibuja el modelo
    if model.getPropertieList(PROPERTIE_MODEL_TYPES, model.getPropertie(PROPERTIE_MODEL_SELECTED)) == FIGURE_LIST:
        drawList(objList, MODEL_POSITION, 0, None, [400, 400, 400], None)
    else:
        objList.draw(MODEL_POSITION, getRGBNormalized(255, 255, 255))

    # Detiene el shader
    program[program[0] + 1].stop()

    pygame.display.flip()
