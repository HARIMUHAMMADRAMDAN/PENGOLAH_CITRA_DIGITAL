import numpy as np
import imageio
import matplotlib.pyplot as plt

def extract_red_channel(image_path):
    # Membaca citra
    image = imageio.imread(image_path)
    red_channel = image[:, :, 0]  # Channel Merah

    # Menampilkan channel merah
    plt.imshow(red_channel, cmap='gray')
    plt.title(f'Red Channel - {image_path}')
    plt.axis('off')
    plt.show()

# Ganti dengan path citra daun
image_paths = ['daun_kenikir.jpg', 'daun_pepaya.jpeg', 'daun_singkong.jpeg']
for path in image_paths:
    extract_red_channel(path)
