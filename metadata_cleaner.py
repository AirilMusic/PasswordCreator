import os
import subprocess
from PIL import Image

def remove_metadata_image(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            data = list(img.getdata())
            image_without_exif = Image.new(img.mode, img.size)
            image_without_exif.putdata(data)
            image_without_exif.save(output_path)
        return True
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return False

def remove_metadata_video(video_path, output_path):
    try:
        command = ['ffmpeg', '-i', video_path, '-map_metadata', '-1', '-c:v', 'copy', '-c:a', 'copy', output_path]
        subprocess.run(command, check=True)
        return True
    except Exception as e:
        print(f"Error al procesar el vídeo: {e}")
        return False

directory = os.path.dirname(os.path.realpath(__file__))
processed_dir = os.path.join(directory, "processed")

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path):
        output_path = os.path.join(processed_dir, filename)

        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            if remove_metadata_image(file_path, output_path):
                print(f"Metadatos eliminados de la imagen: {filename}")
            else:
                print(f"No se pudo procesar la imagen: {filename}")

        elif filename.lower().endswith(('.mp4', '.mov', '.avi')):
            if remove_metadata_video(file_path, output_path):
                print(f"Metadatos eliminados del vídeo: {filename}")
            else:
                print(f"No se pudo procesar el vídeo: {filename}")

        else:
            print(f"Archivo no soportado, se omite: {filename}")
