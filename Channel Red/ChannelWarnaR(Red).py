import numpy as np
import imageio
import matplotlib.pyplot as plt

def extract_red_channel(image_paths):
    # Membuat figure dengan subplots
    plt.figure(figsize=(15, 5))  # Ukuran figure

    for i, image_path in enumerate(image_paths):
        # Membaca citra
        image = imageio.imread(image_path)
        red_channel = image[:, :, 0]  # Channel Merah

        # Menampilkan channel merah di subplot
        plt.subplot(1, 3, i + 1)  # 1 baris, 3 kolom
        plt.imshow(red_channel, cmap='gray')
        plt.title(f'Red Channel - {image_path}')
        plt.axis('off')

    plt.tight_layout()  # Mengatur layout agar tidak bertumpuk
    plt.show()

# Ganti dengan path citra daun
image_paths = ['daun_kenikir.jpg', 'daun_pepaya.jpeg', 'daun_singkong.jpeg']
extract_red_channel(image_paths)
