import pandas as pd
import random
from PSO import PSO
from utils import Configuration
from squared_error import Error_Function
from glass_permittivity import (BK7)

#Some functions
def Sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total

def Rosenbrock(x):
    total=0
    for i in range(len(x)):
        total += ((100 * (x[i] - x[i]**2)**2) + (x[i] - 1)**2)
    return total

def Exec1():
    Error = Error_Function()
    Error.file_path = "Celula_38.prn"
    Error.wavelength = 975.1
    Error.permittivity_real_2 = 1
    Error.permittivity_imag_2 = 0
    Error.permittivity_glass = BK7(975.1)

    return  Error

PSO(Exec1().get_error)