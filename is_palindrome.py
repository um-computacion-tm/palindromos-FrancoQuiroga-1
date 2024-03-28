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
        

class Testespalindrome(unittest.TestCase):
    def testespalindrome(self):
        palabra = 'a'
        ispalindrome = is_palindrome(palabra)
        self.assertTrue(ispalindrome)

    def testespalindrome1(self):
        palabra = 'Ala'
        ispalindrome = is_palindrome(palabra)
        self.assertTrue(ispalindrome)

    def testnoespalindrome(self):
        palabra = 'ajedrez'
        ispalindrome = is_palindrome(palabra)
        self.assertFalse(ispalindrome)

    def testnoespalindrome1(self):
        palabra = "palindrome3??"
        ispalindrome = is_palindrome(palabra)
        self.assertFalse(ispalindrome)
unittest.main()