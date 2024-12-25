# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from configuration import load_jwt, save_jwt
from blue_yonder import Actor
import yaml


image_post_text = 'This is a post with an embedded image.'
IMAGE_FILE = './images/butterfly_big.jpg'
MIME_TYPE = 'image/jpeg'
#                  - or -
# IMAGE_FILE = './images/butterfly.png'
# MIME_TYPE = 'image/png'

image_alt_text = 'This is an image of a butterfly.'

POST_WITH_IMAGE_PATH = './data/post_with_image.yaml'


def main():
    """ This is a simple example of how to post an image.
    :return:
    """

    my_actor = Actor(jwt=load_jwt())
    save_jwt(jwt=my_actor.jwt)

    # Upload the image, get a blob data
    uploaded_blob = my_actor.upload_image(file_path=IMAGE_FILE, mime_type=MIME_TYPE)

    # Post a post with an embedded image;
    # the hight and width let you control the proportions.
    post_with_image = my_actor.post_image(
        text=image_post_text,
        blob=uploaded_blob,
        alt_text=image_alt_text,
        aspect_ratio={'height':1707,'width':2560} #2560 × 1707
    )

    # We will save its ids it in a yaml file.
    with open(POST_WITH_IMAGE_PATH, 'w') as data_file:
        yaml.dump(post_with_image, data_file)


if __name__ == "__main__":
    """ This is a simple example of how to post an image. 
    """
    main()
    ...