import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

print("Program dimulai...")

# ==============================
# 1. MEMBACA CITRA
# ==============================
image = imageio.imread("gambar.png")
print("Gambar berhasil dibaca")

if len(image.shape) == 3:
    image = np.mean(image, axis=2)

image = image.astype(np.float32)

# ==============================
# 2. MENAMBAHKAN NOISE
# ==============================
mean = 0
std_dev = 20
noise = np.random.normal(mean, std_dev, image.shape)
noisy_image = image + noise
noisy_image = np.clip(noisy_image, 0, 255)

print("Noise berhasil ditambahkan")

# ==============================
# 3. IMAGE RESTORATION (MEAN FILTER)
# ==============================
height, width = noisy_image.shape
restored_image = np.zeros((height, width))

kernel_size = 3
offset = kernel_size // 2

for i in range(offset, height - offset):
    for j in range(offset, width - offset):
        neighborhood = noisy_image[i-offset:i+offset+1, j-offset:j+offset+1]
        restored_image[i, j] = np.mean(neighborhood)

print("Restorasi selesai")

# ==============================
# 4. VISUALISASI
# ==============================
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Citra Asli")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Citra Ternoise")
plt.imshow(noisy_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Citra Setelah Restorasi")
plt.imshow(restored_image, cmap='gray')
plt.axis('off')

print("Menampilkan gambar...")
plt.show(block=True)
