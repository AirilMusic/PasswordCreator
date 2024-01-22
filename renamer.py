import os
import itertools

def rename_images():
    directory = os.getcwd()
    os.chdir(directory)

    image_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_files.sort()

    number_generator = itertools.count(start=1)

    for file in image_files:
        new_name = f"{next(number_generator)}{os.path.splitext(file)[1]}"

        os.rename(file, new_name)
        print(f'Renombrado: {file} a {new_name}')

rename_images()
