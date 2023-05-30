import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os
from scipy.sparse.linalg import eigs
from scipy import sparse
import time


def matrix_A0(dat):
    matrix = []
    matrixA = [[], [], [], [], [], [], [], [], [], [], [], []] #, [], [], [], [], [], [], [], []]
    delMas = ["Row   1: ", "Row   2: ", "Row   3: ", "Row   4: ", "Row   5: ", "Row   6: ", "Row   7: ", "Row   8: ",
              "Row   9: ", "Row  10: ", "Row  11: ", "Row  12: "] #, "Row  13: ", "Row  14: ", "Row  15: ", "Row  16: ",
              # "Row  17: ", "Row  18: ", "Row  19: ", "Row  20: "]

    with open(f"dataFortan/v12_2/{dat}", "r", encoding = "utf-8") as file:
        for i in range(3):
            file.readline()

        for i in range(500):  # 903
            file.readline()
            stringer = ""
            for j in range(12):
                stringer += file.readline()
            matrix.append(stringer.replace("D", "E").strip().split("\n"))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in delMas:
                if k in matrix[i][j]:
                    matrix[i][j] = matrix[i][j].replace(k, "").strip().split(")  (")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                matrix[i][j][k] = matrix[i][j][k].replace("(", "").replace(")", "").strip().split(",")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                matrixA[j].append(complex(float(matrix[i][j][k][0]), float(matrix[i][j][k][1])))
    return matrixA


def matrix_B0(dat):
    matrix = []
    matrixB = [[], [], [] ]#, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    delMas = ["Row   1: ", "Row   2: ", "Row   3: "]#, "Row   4: ", "Row   5: ", "Row   6: ", "Row   7: ", "Row   8: ",
              # "Row   9: ", "Row  10: ", "Row  11: ", "Row  12: ", "Row  13: ", "Row  14: ", "Row  15: ", "Row  16: ",
              # "Row  17: ", "Row  18: ", "Row  19: ", "Row  20: "]

    with open(f"dataFortan/v12_2/{dat}", "r", encoding = "utf-8") as file:
        for i in range(3):
            file.readline()

        for i in range(500):  # 903
            file.readline()
            stringer = ""
            for j in range(3):
                stringer += file.readline()
            matrix.append(stringer.replace("D", "E").strip().split("\n"))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in delMas:
                if k in matrix[i][j]:
                    matrix[i][j] = matrix[i][j].replace(k, "").strip().split(")  (")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                matrix[i][j][k] = matrix[i][j][k].replace("(", "").replace(")", "").strip().split(",")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                matrixB[j].append(complex(float(matrix[i][j][k][0]), float(matrix[i][j][k][1])))
    return matrixB


# заменяет "e" на "E" (для Fortran)
def scientific_notation(number):
    """
    Format a floating-point scalar as a decimal string in scientific notation.

    Provides control over rounding, trimming and padding. Uses and assumes
    IEEE unbiased rounding. Uses the "Dragon4" algorithm.

    Parameters
    ----------
    x : python float or numpy floating scalar
        Value to format.
    precision : non-negative integer or None, optional
        Maximum number of digits to print. May be None if `unique` is
        `True`, but must be an integer if unique is `False`.
    unique : boolean, optional
        If `True`, use a digit-generation strategy which gives the shortest
        representation which uniquely identifies the floating-point number from
        other values of the same type, by judicious rounding. If `precision`
        was omitted, print all necessary digits, otherwise digit generation is
        cut off after `precision` digits and the remaining value is rounded.
        If `False`, digits are generated as if printing an infinite-precision
        value and stopping after `precision` digits, rounding the remaining
        value.
    trim : one of 'k', '.', '0', '-', optional
        Controls post-processing trimming of trailing digits, as follows:

        * 'k' : keep trailing zeros, keep decimal point (no trimming)
        * '.' : trim all trailing zeros, leave decimal point
        * '0' : trim all but the zero before the decimal point. Insert the
          zero if it is missing.
        * '-' : trim trailing zeros and any trailing decimal point
    sign : boolean, optional
        Whether to show the sign for positive values.
    pad_left : non-negative integer, optional
        Pad the left side of the string with whitespace until at least that
        many characters are to the left of the decimal point.
    exp_digits : non-negative integer, optional
        Pad the exponent with zeros until it contains at least this many digits.
        If omitted, the exponent will be at least 2 digits."""
    return str(np.format_float_scientific(number, unique = False, precision = 13, trim = 'k',
                                          exp_digits = 2)).replace("e", "E")


matrixA_src = "MatrixA_v12_Step_6.dat"
matrixB_src = "MatrixB_v12_Step_2.dat"
matrixA = np.array(matrix_A0(matrixA_src))
matrixB = np.array(matrix_B0(matrixB_src))
print(len(matrixA[0]))
print(len(matrixB[0]))
with open(f"dataPython/v12_2/{matrixA_src}", "w", encoding = "utf-8") as file:
    for i in matrixA:
        for j in i:
            if str(j.real)[0] == "-" and str(j.imag)[0] == "-":
                file.write(f"({scientific_notation(j.real)},{scientific_notation(j.imag)})")
            elif str(j.real)[0] != "-" and str(j.imag)[0] == "-":
                file.write(f"( {scientific_notation(j.real)},{scientific_notation(j.imag)})")
            elif str(j.real)[0] == "-" and str(j.imag)[0] != "-":
                file.write(f"({scientific_notation(j.real)}, {scientific_notation(j.imag)})")
            else:
                file.write(f"( {scientific_notation(j.real)}, {scientific_notation(j.imag)})")
            file.write(" ")
        file.write("\n")

with open(f"dataPython/v12_2/{matrixB_src}", "w", encoding = "utf-8") as file:
    for i in matrixB:
        for j in i:
            if str(j.real)[0] == "-" and str(j.imag)[0] == "-":
                file.write(f"({scientific_notation(j.real)},{scientific_notation(j.imag)})")
            elif str(j.real)[0] != "-" and str(j.imag)[0] == "-":
                file.write(f"( {scientific_notation(j.real)},{scientific_notation(j.imag)})")
            elif str(j.real)[0] == "-" and str(j.imag)[0] != "-":
                file.write(f"({scientific_notation(j.real)}, {scientific_notation(j.imag)})")
            else:
                file.write(f"( {scientific_notation(j.real)}, {scientific_notation(j.imag)})")
            file.write(" ")
        file.write("\n")

# start = time.time()
# vel1, vek1 = eigs(matrixA, 50, matrixB)
# end = time.time()
# len(vel1)
# print(end - start)
#
# plt.plot()
# plt.show()
