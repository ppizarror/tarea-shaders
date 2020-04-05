#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Provee herramientas matematicas para la creacion y manipulacion de figuras geometricas

# UTILS MATH
# Autor: PABLO PIZARRO @ ppizarro ~
# Fecha: JUNIO 2015

# Importacion de librerias
import math
import types


# Constantes
POINT_2 = "util-point-2"
POINT_3 = "util-point-3"

# Punto de 3 componentes
class point3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Funcion constructora"""
        self._point = vector3(x, y, z)
        self._type = POINT_3

    def getType(self):
        """Retorna el tipo de punto"""
        return self._type

    def getX(self):
        """Retorna el primer elemento del punto"""
        return self._point.getX()

    def getY(self):
        """Retorna el segundo elemento del punto"""
        return self._point.getY()

    def getZ(self):
        """Retorna el tercer elemento del punto"""
        return self._point.getZ()

    def setX(self, value):
        """Define el primer elemento del punto"""
        self._point.setX(value)

    def setY(self, value):
        """Define el segundo elemento del punto"""
        self._point.setY(value)

    def setZ(self, value):
        """Define el tercer elemento del punto"""
        self._point.setZ(value)

    def exportToList(self):
        """Exportar el punto a una lista"""
        return [self._point.getX(), self._point.getY(), self._point.getZ()]

    def exportToTuple(self):
        """Exportar el punto a una tupla"""
        return self._point.getX(), self._point.getY(), self._point.getZ()

    def normalize(self):
        """Normaliza el punto"""
        self._point.normalize()

    # override
    def echo(self, mantise=1):
        """Imprime el punto"""
        self._point.echo(mantise, point3=True)

    def __add__(self, other):
        """Sumar el punto con otro"""
        return self._vectoPoint(self._point.__add__(self._pointToVec(other)))

    def __sub__(self, other):
        """Restar el punto con otro"""
        return self._vectoPoint(self._point.__sub__(self._pointToVec(other)))

    def __mul__(self, other):
        """Multiplicar el punto por otro"""
        return self._vectoPoint(self._point.__mul__(self._pointToVec(other)))

    def __str__(self, mantise=1, **kwargs):
        """Retornar el string del punto"""
        return self._point.__str__(mantise, point3=True)

    def __div__(self, other):
        """Dividir el punto por otro"""
        return self._vectoPoint(self._point.__div__(self._pointToVec(other)))

    def __abs__(self):
        """Retornar el valor absoluto del punto"""
        return self._vectoPoint(self._point.__abs__())

    def __iadd__(self, other):
        """Suma el mismo punto con other"""
        self = self._vectoPoint(self._point.__iadd__(other))
        return self

    def __isub__(self, other):
        """Resta el mismo punto con other"""
        self = self._vectoPoint(self._point.__isub__(other))
        return self

    def __imul__(self, other):
        """Multiplica el mismo punto con other"""
        self = self._vectoPoint(self._point.__imul__(other))
        return self

    def __idiv__(self, other):
        """Divide el mismo punto con other"""
        self = self._vectoPoint(self._point.__iadd__(other))
        return self

    # noinspection PyMethodMayBeStatic,PyShadowingNames
    def _pointToVec(self, point):
        """Convierte un punto a un vector"""
        if isinstance(point, point3):
            return vector3(point.getX(), point.getY(), point.getZ())
        else:
            return point

    # noinspection PyMethodMayBeStatic
    def _vectoPoint(self, vec):
        """Convierte un vector a un punto"""
        if isinstance(vec, vector3):
            return point3(vec.getX(), vec.getY(), vec.getZ())
        else:
            return vec


# Punto de 2 componentes
class point2(point3):
    def __init__(self, x=0.0, y=0.0):
        self._point = vector3(x, y, 0.0)
        self._type = POINT_2

    # noinspection PyMethodMayBeStatic,PyShadowingNames
    def _pointToVec(self, point):
        """Convierte un punto a un vector"""
        if isinstance(point, point2):
            return vector3(point.getX(), point.getY(), 0.0)
        else:
            return point

    # noinspection PyMethodMayBeStatic
    def _vectoPoint(self, vec):
        """Convierte un vector a un punto"""
        if isinstance(vec, vector3):
            return point2(vec.getX(), vec.getY(), 0.0)
        else:
            return vec

    def __str__(self, mantise=1, **kwargs):
        """Retornar el string del punto"""
        return self._point.__str__(mantise, point2=True)

    # override
    def echo(self, mantise=1):
        """Imprime el punto"""
        self._point.echo(mantise, point2=True)

    def exportToList(self):
        """Exportar el punto a una lista"""
        return [self._point.getX(), self._point.getY()]

    def exportToTuple(self):
        """Exportar el punto a una tupla"""
        return self._point.getX(), self._point.getY()


# Vector de 3 componentes, provee funciones matematicas basicas
class vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Funcion constructora"""
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def getModule(self):
        """Retorna el modulo del vector"""
        return self.distancewith(vector3(0, 0, 0))

    def setX(self, x):
        """Define la coordenada x"""
        self.x = x

    def setY(self, y):
        """Define la coordenada y"""
        self.y = y

    def setZ(self, z):
        """Define la coordenada z"""
        self.z = z

    def getX(self):
        """Retorna la coordenada x"""
        return self.x

    def getY(self):
        """Retorna la coordenada y"""
        return self.y

    def getZ(self):
        """Retorna la coordenada z"""
        return self.z

    def ponderate(self, a=1):
        """Pondera el vector por un numero"""
        if isinstance(a, types.FloatType) or isinstance(a, types.IntType):
            self.x *= a
            self.y *= a
            self.z *= a
        else:
            self.throwError(2, "ponderate")
            return self

    def __add__(self, other):
        """Suma el vector con otro"""
        if isinstance(other, vector3):
            return vector3(self.x + other.getX(), self.y + other.getY(), self.z + other.getZ())
        elif isinstance(other, types.TupleType) or isinstance(other, types.ListType):
            if len(other) == 3:
                return vector3(self.x + other[0], self.y + other[1], self.z + other[2])
        else:
            self.throwError(2, "__add__")
            return self

    def __sub__(self, other):
        """Resta el vector con otro"""
        if isinstance(other, vector3):
            return vector3(self.x - other.getX(), self.y - other.getY(), self.z - other.getZ())
        elif isinstance(other, types.TupleType) or isinstance(other, types.ListType):
            if len(other) == 3:
                return vector3(self.x - other[0], self.y - other[1], self.z - other[2])
        else:
            self.throwError(2, "__sub__")
            return self

    def __mod__(self, other):
        """Calcula el modulo con otro"""
        return vector3(self.x % other.getX(), self.y % other.getY(), self.z % other.getZ())

    def __mul__(self, other):
        """Producto punto o producto por valor"""
        if isinstance(other, vector3):
            return vector3(self.x * other.getX(), self.y * other.getY(), self.z * other.getZ())
        else:
            if isinstance(other, types.ListType) or isinstance(other, types.TupleType):
                return vector3(self.x * other[0], self.y * other[1], self.z * other[2])
            elif isinstance(other, types.IntType) or isinstance(other, types.FloatType):
                return vector3(self.x * other, self.y * other, self.z * other)
            else:
                self.throwError(2, "__mul__")
                return self

    def __abs__(self):
        """Valor absoluto"""
        return vector3(abs(self.x), abs(self.y), abs(self.z))

    def __div__(self, other):
        """Dividir por un ector o por un valor"""
        if isinstance(other, vector3):
            return vector3(self.x / other.getX(), self.y / other.getY(), self.z / other.getZ())
        else:
            if isinstance(other, types.IntType) or isinstance(other, types.FloatType):
                return vector3(self.x / other, self.y / other, self.z / other)
            else:
                self.throwError(2, "__div__")
                return self

    def __invert__(self, other):
        """Invertir signo del vector en forma ~"""
        return vector3(-self.x, -self.y, -self.z)

    def __neg__(self):
        """Invertir signo del vector en forma -"""
        return vector3(-self.x, -self.y, -self.z)

    def __pos__(self):
        """Aplicar signo positivo"""
        return vector3(self.x, self.y, self.z)

    def __and__(self, other):
        """Calcula el operador logico and"""
        if isinstance(other, vector3):
            if self.x > 0 and other.getX() > 0:
                x = 1
            else:
                x = 0
            if self.y > 0 and other.getY() > 0:
                y = 1
            else:
                y = 0
            if self.z > 0 and other.getZ() > 0:
                z = 1
            else:
                z = 0
            return vector3(x, y, z)
        else:
            self.throwError(2, "__and__")
            return vector3()

    def __or__(self, other):
        """Calcula el operador logico and"""
        if isinstance(other, vector3):
            if self.x > 0 or other.getX() > 0:
                x = 1
            else:
                x = 0
            if self.y > 0 or other.getY() > 0:
                y = 1
            else:
                y = 0
            if self.z > 0 or other.getZ() > 0:
                z = 1
            else:
                z = 0
            return vector3(x, y, z)
        else:
            self.throwError(2, "__or__")
            return vector3()

    def __int__(self):
        """Convierte el vector a enteros"""
        return vector3(int(self.x), int(self.y), int(self.z))

    def __float__(self):
        """Convierte el vector a flotante"""
        return vector3(float(self.x), float(self.y), float(self.z))

    def normalize(self):
        """Normalizar el vector"""
        modl = self.getModule()
        self.x /= modl
        self.y /= modl
        self.z /= modl

    def getNormalized(self):
        """Retorna el vector normalizado"""
        modl = self.getModule()
        return vector3(self.x / modl, self.y / modl, self.z / modl)

    def clone(self):
        """Clonar el vector"""
        return vector3(self.x, self.y, self.z)

    def __complex__(self):
        """Genera un vector complejo"""
        return vector3(complex(self.x), complex(self.y), complex(self.z))

    def __long__(self):
        """Genera un vector long"""
        return vector3(long(self.x), long(self.y), long(self.z))

    def __hex__(self):
        """Genera un vector hex"""
        return vector3(hex(self.x), hex(self.y), hex(self.z))

    def __oct__(self):
        """Genera un vector oct"""
        return vector3(oct(self.x), oct(self.y), oct(self.z))

    def __iadd__(self, other):
        """Suma un vector con otro"""
        if isinstance(other, vector3):
            self.x += other.getX()
            self.y += other.getY()
            self.z += other.getZ()
            return self
        elif isinstance(other, types.TupleType) or isinstance(other, types.ListType):
            if len(other) == 3:
                self.x += other[0]
                self.y += other[1]
                self.z += other[2]
                return self
        else:
            self.throwError(2, "__iadd__")
            return self

    def __isub__(self, other):
        """Resta un vector con otro"""
        if isinstance(other, vector3):
            self.x -= other.getX()
            self.y -= other.getY()
            self.z -= other.getZ()
            return self
        elif isinstance(other, types.TupleType) or isinstance(other, types.ListType):
            if len(other) == 3:
                self.x -= other[0]
                self.y -= other[1]
                self.z -= other[2]
                return self
        else:
            self.throwError(2, "__isub__")
            return self

    def __imul__(self, other):
        """Producto punto con otro"""
        if isinstance(other, vector3):
            self.x *= other.getX()
            self.y *= other.getY()
            self.z *= other.getZ()
            return self
        else:
            if isinstance(other, types.ListType) or isinstance(other, types.TupleType):
                self.x *= other[0]
                self.y *= other[1]
                self.z *= other[2]
                return self
            elif isinstance(other, types.IntType) or isinstance(other, types.FloatType):
                self.x *= other
                self.y *= other
                self.z *= other
                return self
            else:
                self.throwError(2, "__imul__")
                return self

    def __idiv__(self, other):
        """Division con otro vector por valor"""
        if isinstance(other, vector3):
            self.x /= other.getX()
            self.y /= other.getY()
            self.z /= other.getZ()
            return self
        else:
            if isinstance(other, types.ListType) or isinstance(other, types.TupleType):
                self.x /= other[0]
                self.y /= other[1]
                self.z /= other[2]
                return self
            elif isinstance(other, types.IntType) or isinstance(other, types.FloatType):
                self.x /= other
                self.y /= other
                self.z /= other
                return self
            else:
                self.throwError(2, "__idiv__")
                return self

    @staticmethod
    def throwError(errNum, errFunc):
        """Imprime un error en pantalla"""

        def _printError(error):
            print "Error :: {0} ~ {1}".format(error, errFunc)

        if errNum == 1:
            _printError("La mantisa es menor a 1")
        elif errNum == 2:
            _printError("Tipo invalido")

    # override
    def echo(self, mantise=1, **kwargs):
        """Imprime el vector en pantalla"""
        print self.__str__(mantise, **kwargs)

    def dot(self, other):
        """Producto punto"""
        return self.__mul__(other)

    def dotwith(self, other):
        """Producto punto con otro"""
        dot = self.dot(other)
        self.x = dot.getX()
        self.y = dot.getY()
        self.z = dot.getZ()

    def cross(self, other):
        """Retorna el producto cruz"""
        if isinstance(other, vector3):
            i = self.y * other.getZ() - self.z * other.getY()
            j = self.z * other.getX() - self.x * other.getZ()
            k = self.x * other.getY() - self.y * other.getX()
            return vector3(i, j, k)
        elif isinstance(other, types.TupleType) or isinstance(other, types.ListType):
            return self.cross(vector3(*other))
        else:
            self.throwError(2, "cross")
            return self

    def crosswith(self, other):
        """Aplica el producto cruz con el otro vector"""
        cross = self.cross(other)
        self.x = cross.getX()
        self.y = cross.getY()
        self.z = cross.getZ()

    def distancewith(self, other):
        """Retorna la distancia a otro vector"""
        if isinstance(other, vector3):
            return math.sqrt((self.x - other.getX()) ** 2 + (self.y - other.getY()) ** 2 + (self.z - other.getY()) ** 2)
        elif isinstance(other, types.ListType) or isinstance(other, types.TupleType):
            return self.distancewith(vector3(*other))
        else:
            self.throwError(2, "distance")
            return 0.0

    def __str__(self, mantise=1, **kwargs):
        """Retorna el string del punto"""
        if mantise >= 1:
            if kwargs.get("formated"):
                _format = "/{0}\\\n|{1}|\n\\{2}/"
            else:
                _format = "[{0},{1},{2}]"
            if kwargs.get("point3"):
                _format = "({0},{1},{2})"
            if kwargs.get("point2"):
                _format = "({0},{1})"
            return _format.format(round(self.x, mantise), round(self.y, mantise), round(self.z, mantise))
        else:
            self.throwError(1, "echo")

    def exportToList(self):
        """Exportar el vector a una lista"""
        return [self.x, self.y, self.z]

    def exportToTuple(self):
        """Exportar el vector a una tupla"""
        return self.x, self.y, self.z


def normal3points(a, b, c):
    """Retorna el vector normal dado tres puntos a, b, c"""
    if isinstance(a, types.ListType) or isinstance(a, types.TupleType):
        a = vector3(*a)
        b = vector3(*b)
        c = vector3(*c)
    elif isinstance(a, point3):
        a = vector3(*a.exportToList())
        b = vector3(*b.exportToList())
        c = vector3(*c.exportToList())
    cross_result = (a - c).cross(b - c).getNormalized()
    if cross_result.getX() == -0.0: cross_result.setX(0.0)
    if cross_result.getY() == -0.0: cross_result.setY(0.0)
    if cross_result.getZ() == -0.0: cross_result.setZ(0.0)
    return cross_result


def cos(angle):
    """Retorna el coseno de un angulo"""
    return math.cos(math.radians(angle))


def sin(angle):
    """Retorna el seno de un angulo"""
    return math.sin(math.radians(angle))


def sgn(x):
    """Retorna el signo de x"""
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def SPRtoXYZ(r, fi, theta):
    """Convierte las coordenadas esferiacs (r,fi,theta) a (x,y,z)"""
    x = r * sin(theta) * cos(fi)
    y = r * sin(theta) * sin(fi)
    z = r * cos(theta)
    return x, y, z


def XYZtoSPR(x, y, z):
    """Convierte las coordenadas cartesianas (x,y,z) a las coordenadas esfericas (r,phi,theta) con angulos en grados"""
    # Calculo el radio
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    # Calculo el angulo theta
    if z > 0:
        theta = math.atan(math.sqrt(x ** 2 + y ** 2) / z)
    elif z == 0:
        theta = math.pi / 2
    else:
        theta = math.pi + math.atan(math.sqrt(x ** 2 + y ** 2) / z)
    # Calculo el angulo phi
    if x > 0:
        if y > 0:
            phi = math.atan(y / x)
        else:
            phi = 2 * math.pi + math.atan(y / x)
    elif x == 0:
        phi = sgn(y) * math.pi / 2
    else:
        phi = math.pi + math.atan(y / x)
    theta = math.degrees(theta)
    phi = math.degrees(phi) % 360
    theta = min(max(theta, 0.000001), 180)
    return r, phi, theta
