# libreria de numeros complejos CNYT

se implemento una librería de operaciones con numeros complejos en python, sin usar el tipo de datos complex.  
los numeros se representan como tuplas:

- forma cartesiana: (re, im) siendo "re" la parte real y "im" la parte imaginaria.  
- forma polar: (r, θ) donde "r" es el módulo y "θ" la fase en radianes.

# funciones incluidas

La libreria "complejos.py" contiene las siguientes funciones:

1. suma(c1, c2) → retorna la suma (re, im).  
2. resta(c1, c2) → retorna la resta (re, im).  
3. producto(c1, c2) → retorna el producto (re, im).  
4. division(c1, c2) → retorna la division (re, im) (arrojaa ZeroDivisionError si c2 = (0,0)).  
5. modulo(c) → retorna el modulo |c|.  
6. conjugado(c) → retorna el conjugado (re, -im).  
7.  a polar(c) → convierte de cartesiano a polar (r, θ).  
8. a cartesiano(p) → convierte de polar a cartesiano (re, im).  
9. fase(c) → retorna la fase de un numero en radianes (devuelve `ValueError` si el numero es `(0,0)`).


# pruebas

El archivo "test_complejos.py" contiene 3 pruebas (por cada funcion) usando unittest.

