from PSO import PSO
from squared_error import Error_Function
import glass_permittivity as gp
import pickle


def Exec1():
    Error = Error_Function()
    Error.file_path = "Celula_38.prn"
    Error.wavelength = 975.1
    Error.permittivity_real_2 = 1
    Error.permittivity_imag_2 = 0
    Error.permittivity_glass = gp.BK7(975.1)

    return Error


dimensions = [(-60.261, -27.833), (-9.4685, 1.95), (500, 2500)]

# The two variables that you need to change for the tests
num_particles = 10
max_iterations = 100

P = PSO(Exec1().get_error, dimensions, num_particles, max_iterations)
p_real_3, p_imag_3, th = P.best_position

#It saves l1, l2, l3, l4 as list in a binary file
l1 = P.error_history
l2 = P.best_position
l3 = P.dimensions
l4 = [P.best_error, P.convergence_time, P.num_particles, P.max_iterations]

file_name = "test.txt"
fp = open(file_name, "wb")
pickle.dump(l1, fp)
pickle.dump(l2, fp)
pickle.dump(l3, fp)
pickle.dump(l4, fp)

fp = open(file_name, "rb")
error_history = pickle.load(fp)
best_position = pickle.load(fp)
dimensions = pickle.load(fp)
best_error, convergence_time, num_particles, max_iterations = pickle.load(fp)

print(error_history)
print(best_position)
print(dimensions)
print(best_error, convergence_time, num_particles, max_iterations)
