import unittest

def is_palindrome(palabra):
    listadeincluidos = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letra in palabra:
        if letra in listadeincluidos:
            continue
        else:
            palabra = palabra.replace(letra, '')
    palabra = palabra.lower()
    for posicion in range(len(palabra)):
        espalindrome = False
        posicion_opuesta = -posicion-1
        if palabra[posicion] == palabra[posicion_opuesta]:
            espalindrome = True
        if palabra[posicion] != palabra[posicion_opuesta]:
            espalindrome = False
            return espalindrome
    return espalindrome

def obtener_cantidad_de_palabras_palindrome(listadepalabras):
    palindromenumber = 0
    for item in listadepalabras:
        palindromecheck = is_palindrome(item)
        if palindromecheck is True:
            palindromenumber += 1
            palindromecheck = False
    return palindromenumber
        







class TestCantidadDePalabrasPalindromes(unittest.TestCase):

    

    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
			"A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 6)
    def test_cantidad_de_palabras_palindromes_cero(self):
        palabras = ["al??"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 0)

    def test_cantidad_de_palabras_palindromes_simpleconsimbolo(self):
        palabras = ["al  ? a"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)
unittest.main()