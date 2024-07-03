from pycipher import Rot13
a=Rot13().encipher('defend the east wall of the castle')
print(a)
b=Rot13().decipher(a)
print(b)