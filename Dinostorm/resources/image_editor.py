from PIL import Image

import os

#Create function to flip images round
def rotate_image(input_file_path, output_file_path):
    count=1
    for x in os.listdir(input_file_path):
        path = f'{input_file_path}/{x}'
        original_image = Image.open(path)
        flipped_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        image_name = f'{count}.png'
        count += 1
        flipped_image.save(f'{output_file_path}/{image_name}')
        original_image.close()
        flipped_image.close()
    print('Done')


def resize_image(input_file_path, dimensions):
    for x in os.listdir(input_file_path):
        path = f'{input_file_path}/{x}'
        image = Image.open(path)
        image = image.resize(dimensions)
        image.save(path)
        image.close
    print('Done')

# rotate_image('Dinostorm/resources/dino/dead_right', 'Dinostorm/resources/dino/dead_left')
# rotate_image('Dinostorm/resources/dino/idle_right', 'Dinostorm/resources/dino/idle_left')
# rotate_image('Dinostorm/resources/dino/walk_right', 'Dinostorm/resources/dino/walk_left')

# resize_image('Dinostorm/resources/dino/dead_left', (140, 100))
# resize_image('Dinostorm/resources/dino/dead_right', (140, 100))
# resize_image('Dinostorm/resources/dino/idle_left', (140, 100))
# resize_image('Dinostorm/resources/dino/idle_right', (140, 100))
# resize_image('Dinostorm/resources/dino/walk_left', (140, 100))
# resize_image('Dinostorm/resources/dino/walk_right', (140, 100))






