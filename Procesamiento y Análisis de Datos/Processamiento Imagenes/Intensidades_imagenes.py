import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ============================
# 1. Cargar imagen
# ============================
filename = "091225a_00015.JPG"
imagen = np.array(Image.open(filename))
imagen_gray = np.mean(imagen, axis=2)  # Convertir a escala de grises

# Conversión px → m (5x)
px_a_m = (1e-3) / 780   # 1 mm ~ 780 px

num_perfiles = 200

# ============================
# 2. Seleccionar rectángulo (2 clics)
# ============================
plt.figure(figsize=(8,6))
plt.imshow(imagen, cmap="gray")
plt.title("Selecciona dos puntos: esquina sup-izq y esquina inf-der")
plt.axis("on")

puntos = plt.ginput(2)   # Igual que MATLAB
plt.close()

(x1, y1), (x2, y2) = puntos

x_min, x_max = int(min(x1, x2)), int(max(x1, x2))
y_min, y_max = int(min(y1, y2)), int(max(y1, y2))

rect_width = x_max - x_min
rect_height = y_max - y_min

print("Rectángulo seleccionado:")
print("x_min:", x_min, "x_max:", x_max)
print("y_min:", y_min, "y_max:", y_max)

# ============================
# 3. Generar perfiles
# ============================

todos_perfiles = []
perfiles_para_promedio = []

if rect_width > rect_height:
    # Líneas horizontales
    step = rect_height / num_perfiles

    for j in range(num_perfiles):
        y = int(y_min + j * step)
        x_linea = np.arange(x_min, x_max)

        intensidad = imagen_gray[y, x_linea]
        todos_perfiles.append(intensidad)
        perfiles_para_promedio.append(intensidad)

else:
    # Líneas verticales
    step = rect_width / num_perfiles

    for j in range(num_perfiles):
        x = int(x_min + j * step)
        y_linea = np.arange(y_min, y_max)

        intensidad = imagen_gray[y_linea, x]
        todos_perfiles.append(intensidad)
        perfiles_para_promedio.append(intensidad)

# Convertir a array
perfiles_para_promedio = np.array(perfiles_para_promedio)

# ============================
# 4. Promedio
# ============================

intensidad_media = perfiles_para_promedio.mean(axis=0)

# ============================
# 5. Ubicar cambio más abrupto (gradiente)
# ============================

grad = np.gradient(intensidad_media)
idx_cambio = np.argmax(np.abs(grad))

# ============================
# 6. Eje posicional (centrado en cambio abrupto)
# ============================

posicion_metros = ((np.arange(len(intensidad_media))) - idx_cambio) * px_a_m

# ============================
# 7. Graficar
# ============================
plt.figure(figsize=(8,6))
plt.plot(posicion_metros / 1e-6, intensidad_media, lw=2)
plt.xlabel("Posición [µm]")
plt.ylabel("Intensidad promedio")
plt.grid(True)
plt.title("Perfil promedio")
plt.show()

# ============================
# 8. Guardar los datos
# ============================

datos = np.column_stack([posicion_metros/1e-6, intensidad_media])
np.savetxt("intensidad_promedio.dat", datos)
print("Datos guardados en intensidad_promedio.dat")
