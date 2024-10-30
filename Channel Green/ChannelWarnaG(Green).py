import numpy as np
import imageio
import matplotlib.pyplot as plt

def extract_green_channel(image_paths):
    
    plt.figure(figsize=(15, 5))  

    for i, image_path in enumerate(image_paths):
        
        image = imageio.imread(image_path)
        green_channel = image[:, :, 1]  

        
        plt.subplot(1, 3, i + 1)  
        plt.imshow(green_channel, cmap='gray')
        plt.title(f'Green Channel - {image_path}')
        plt.axis('off')

    plt.tight_layout()  
    plt.show()


image_paths = ['daun_kenikir.jpg', 'daun_pepaya.jpeg', 'daun_singkong.jpeg']
extract_green_channel(image_paths)
