from matrix import *
from vector import *
from rational import *

print("Test 1...\n")
print("Checking multiplication\n")
print(Matrix(Rational(1, 2), Rational(1,3), Rational(-2, 7), Rational(2, 8)) @ Matrix(Rational(-1, 3), Rational(2, 7), Rational(2, 5), Rational(-1, 7) ))
 
print("Test 2...\n")
print("Checking inverse\n")
print(Matrix(Rational(1, 2), Rational(1,3), Rational(-2, 7), Rational(2, 8)).inverse())

print("Test 3...\n")
matrix1 = Matrix(Rational(1, 3), Rational(1, 4), Rational(-2, 8), Rational(2, 7))
matrix2 = Matrix(Rational(1, 2), Rational(1, 3), Rational(-2, 7), Rational(2, 8))
matrix3 = Matrix(Rational(1, 7), Rational(2, 3), Rational(-3, 9), Rational(4, 14))
        
print("3a: Checking associative law...\n")

if (matrix1 @ matrix2) @ matrix3 == matrix1 @ (matrix2 @ matrix3):
        print("Associative Law works!\n")
else:
        raise ValueError("Rational contains errors\n")

print("3b: Checking distributive law...\n")

if (matrix1 @ (matrix2 + matrix3) != matrix1 @ matrix2 + matrix1 @ matrix3):
        raise ValueError("Rational contains errors\n")

if (matrix1 + matrix2) @ matrix3 == matrix1 @ matrix3 + matrix2 @ matrix3:
        print("Distributive Law works!\n")

else:
        raise ValueError("Rational contains errors\n")


print("3c: Checking Vector Multiplication...\n")

v1 = Vector(2, 1)

if matrix1(matrix2(v1)) == (matrix1 @ matrix2)(v1):
        print("Vector Multiplication works!\n")

else:
        raise ValueError("Rational contains errors\n")

print("3d: Checking property of determinant...\n")

if matrix1.determinant() * matrix2.determinant() == (matrix1 @ matrix2).determinant():
        print("Property of determinant works!\n")

else:
        raise ValueError("Rational contains error\n")
 
print("3e: Checking inverses...\n")

if matrix1 @ matrix1.inverse() == (matrix1.inverse() @ matrix1) == Matrix(1, 0, 0, 1):
        print("Inverses work!\n")

else:
        raise ValueError("Rational contains error\n")