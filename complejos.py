import math

#operaciones
def suma (c1:tuple, c2:tuple)->tuple:
    """+ compl forma cartesiana"""
    return (c1[0]+c2[0],c1[1]+c2[1])

def resta (c1:tuple, c2:tuple)->tuple:
    """- compl forma cartesiana"""
    return (c1[0]-c2[0],c1[1]-c2[1])

def producto(c1: tuple, c2: tuple) -> tuple:
    """x compl forma cartesiana"""
    re = c1[0] * c2[0] - c1[1] * c2[1]
    im = c1[0] * c2[1] + c1[1] * c2[0]
    return (re, im)

def division(c1: tuple, c2: tuple) -> tuple:
    """/ compl forma cartesiana """
    denom = c2[0]**2 + c2[1]**2
    if denom == 0:
        raise ZeroDivisionError("no se puede dividir entre0")
    re = (c1[0] * c2[0] + c1[1] * c2[1]) / denom
    im = (c1[1] * c2[0] - c1[0] * c2[1]) / denom
    return (re, im)

def modulo(c: tuple) -> float:
    """modulo de un complejo en forma cartesiana (re, im)"""
    return math.hypot(c[0], c[1])


def conjugado(c: tuple) -> tuple:
    """conjugado de un complejo en forma cartesiana (re, im)"""
    return (c[0], -c[1])


#conversiones
def a_polar(c: tuple) -> tuple:
    """convierte un complejo cartesiano (re, im) a polar (r, θ)"""
    r = modulo(c)
    if r == 0:
        return (0.0, 0.0)
    theta = math.atan2(c[1], c[0])# rango (-π, π]
    return (r, theta)


def a_cartesiano(p: tuple) -> tuple:
    """convierte un complejo polar (r, θ) a cartesiano (re, im"""
    re = p[0] * math.cos(p[1])
    im = p[0] * math.sin(p[1])
    return (re, im)


def fase(c: tuple) -> float:
    """retorna fase (angulo) de un complejo cartesiano (re, im)"""
    if c[0] == 0 and c[1] == 0:
        raise ValueError("la fase no esta definida para el numero (0,0)")
    return math.atan2(c[1], c[0])# rango (-π, π]
