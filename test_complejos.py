import unittest
import math
import complejos

class TestComplejos(unittest.TestCase):

#pruebas suma  +
    def test_suma_basica(self):
        self.assertEqual(complejos.suma((1, 2), (3, 4)), (4, 6))

    def test_suma_negativos(self):
        self.assertEqual(complejos.suma((-1, -2), (3, 4)), (2, 2))

    def test_suma_decimales(self):
        self.assertAlmostEqual(complejos.suma((1.5, 2.5), (2.5, 3.5))[0], 4.0)
        self.assertAlmostEqual(complejos.suma((1.5, 2.5), (2.5, 3.5))[1], 6.0)


#pruebas resta  -

    def test_resta_basica(self):
        self.assertEqual(complejos.resta((5, 7), (2, 3)), (3, 4))

    def test_resta_negativos(self):
        self.assertEqual(complejos.resta((-1, -2), (3, 4)), (-4, -6))

    def test_resta_decimales(self):
        self.assertAlmostEqual(complejos.resta((5.5, 2.2), (1.1, 0.2))[0], 4.4)
        self.assertAlmostEqual(complejos.resta((5.5, 2.2), (1.1, 0.2))[1], 2.0)


#pruebas producto  x

    def test_producto_basico(self):
        self.assertEqual(complejos.producto((1, 2), (3, 4)), (-5, 10))

    def test_producto_con_cero(self):
        self.assertEqual(complejos.producto((0, 0), (3, 4)), (0, 0))

    def test_producto_simetrico(self):
        self.assertEqual(complejos.producto((2, 3), (2, -3)), (13, 0))


#pruebas division  /

    def test_division_basica(self):
        resultado = complejos.division((1, 2), (3, 4))
        self.assertAlmostEqual(resultado[0], 0.44, places=2)
        self.assertAlmostEqual(resultado[1], 0.08, places=2)

    def test_division_con_uno(self):
        self.assertEqual(complejos.division((5, -3), (1, 0)), (5.0, -3.0))

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            complejos.division((1, 2), (0, 0))


#pruebas modulo

    def test_modulo_3_4(self):
        self.assertEqual(complejos.modulo((3, 4)), 5.0)

    def test_modulo_cero(self):
        self.assertEqual(complejos.modulo((0, 0)), 0.0)

    def test_modulo_decimales(self):
        self.assertAlmostEqual(complejos.modulo((1.2, 3.4)), math.hypot(1.2, 3.4))


#pruebas conjugado

    def test_conjugado_basico(self):
        self.assertEqual(complejos.conjugado((3, 4)), (3, -4))

    def test_conjugado_cero(self):
        self.assertEqual(complejos.conjugado((0, 0)), (0, 0))

    def test_conjugado_negativo(self):
        self.assertEqual(complejos.conjugado((-2, -5)), (-2, 5))


#pruebas a polar

    def test_a_polar_1_sqrt3(self):
        r, theta = complejos.a_polar((1, math.sqrt(3)))
        self.assertAlmostEqual(r, 2.0, places=5)
        self.assertAlmostEqual(theta, math.pi/3, places=5)

    def test_a_polar_cero(self):
        self.assertEqual(complejos.a_polar((0, 0)), (0.0, 0.0))

    def test_a_polar_cuadrante_negativo(self):
        r, theta = complejos.a_polar((-1, -1))
        self.assertAlmostEqual(r, math.sqrt(2), places=5)
        self.assertAlmostEqual(theta, -3*math.pi/4, places=5)


#pruebas a cartesiano
    def test_a_cartesiano_pi_4(self):
        re, im = complejos.a_cartesiano((math.sqrt(2), math.pi/4))
        self.assertAlmostEqual(re, 1.0, places=5)
        self.assertAlmostEqual(im, 1.0, places=5)

    def test_a_cartesiano_cero(self):
        self.assertEqual(complejos.a_cartesiano((0, 1)), (0.0, 0.0))

    def test_a_cartesiano_otro(self):
        re, im = complejos.a_cartesiano((2, math.pi/3))
        self.assertAlmostEqual(re, 1.0, places=5)
        self.assertAlmostEqual(im, math.sqrt(3), places=5)


# pruebas fase
    def test_fase_basico(self):
        self.assertAlmostEqual(complejos.fase((1, math.sqrt(3))), math.pi/3, places=5)

    def test_fase_negativo(self):
        self.assertAlmostEqual(complejos.fase((-1, 0)), math.pi, places=5)

    def test_fase_cero(self):
        with self.assertRaises(ValueError):
            complejos.fase((0, 0))

if __name__ == '__main__':
    unittest.main()
