import matplotlib.pyplot as plt
import numpy as np


# DELTA_I
with open("dataFortan/v12_2/DELTA_I.dat", "r") as fileFortan:
    for i in range(3):
        fileFortan.readline()
    lines = fileFortan.readlines()
    for i in range(len(lines) - 1):
        lines[i] = lines[i][lines[i].index(':') + 1: len(lines[i])].replace("D", "E")
    lines = "".join(lines).replace("\n", "").split("  ")
    lines = lines[0:-2]
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    delt_i = lines

with open("dataPython/v12_2/DELTA_I.dat", "w", encoding = "utf-8") as filePython:
    for i in delt_i:
        filePython.write(i)
        filePython.write("  ")

# R_I, Z_I
src = "Z_I.dat"
with open(f"dataFortan/v12_2/{src}", "r") as fileFortan:
    for i in range(3):
        fileFortan.readline()

    lines = fileFortan.readlines()
    for i in range(len(lines)-1):
        lines[i] = lines[i][lines[i].index(':') + 4: len(lines[i])].replace("D", "E")
    lines = "".join(lines).replace("\n", "").strip().split()
    array_i = lines


with open(f"dataPython/v12_2/{src}", "w", encoding = "utf-8") as filePython:
    for i in array_i:
        filePython.write(i)
        filePython.write(" ")
