import file_reader
import matplotlib.pyplot as plt

normalized_experimental_table = file_reader.get_normalized_experimental_table("Celula_38.prn")
experimental_table = file_reader.get_experimental_table("Celula_38.prn")

x1_values = []
y1_values = []

for elem in normalized_experimental_table:
    angle, reflectance = elem
    x1_values.append(angle)
    y1_values.append(reflectance)

x2_values = []
y2_values = []

for elem in experimental_table:
    angle, reflectance = elem
    x2_values.append(angle)
    y2_values.append(reflectance)

plt.plot(x1_values, y1_values)
plt.plot(x2_values, y2_values)
plt.xlabel("Angle")
plt.ylabel("Reflectance")
plt.show()

print(len(x2_values))
