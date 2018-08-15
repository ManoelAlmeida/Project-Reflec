# -27.833, -0.6548510942097723, 1491.1217017955298
import reflectance as rflec
import glass_permittivity as gp
import matplotlib.pyplot as plt
import file_reader
import cmath
from PSO import PSO
from squared_error import Error_Function

table = file_reader.get_normalized_experimental_table("Celula_38.prn")
x_values = []
y_values = []
y_values_optmized = []


def Exec1():
    Error = Error_Function()
    Error.file_path = "Celula_38.prn"
    Error.wavelength = 975.1
    Error.permittivity_real_2 = 1
    Error.permittivity_imag_2 = 0
    Error.permittivity_glass = gp.BK7(975.1)

    return Error


P = PSO(Exec1().get_error)
p_real_3, p_imag_3, th = P.best_position

for elem in table:
    angle, reflectance = elem
    x_values.append(angle)
    y_values.append(reflectance)
    radian_angle = (angle * cmath.pi) / 180
    y_values_optmized.append(rflec.total_reflectance(radian_angle, 975.1, 1, 0, p_real_3, p_imag_3, gp.BK7(975.1), th))

plt.plot(x_values, y_values)
plt.plot(x_values, y_values_optmized)
plt.show()