import numpy as np
import imageio
import matplotlib.pyplot as plt

def convert_to_grayscale(image_paths):
    
    plt.figure(figsize=(15, 5))  

    for i, image_path in enumerate(image_paths):
        
        image = imageio.imread(image_path)
        
        
        grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

        
        plt.subplot(1, 3, i + 1)  
        plt.imshow(grayscale_image, cmap='gray')
        plt.title(f'Grayscale Image - {image_path}')
        plt.axis('off')

    plt.tight_layout()  
    plt.show()


image_paths = ['daun_kenikir.jpg', 'daun_pepaya.jpeg', 'daun_singkong.jpeg']
convert_to_grayscale(image_paths)
