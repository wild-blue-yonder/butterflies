# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from configuration import load_jwt, save_jwt
from blue_yonder import Actor
from utilities import (remove_markdown,
                       preprocess_text,
                       create_text_images)
import yaml

IMAGES_OF_TEXT_PATH = './images_of_text/'

LONG_TEXT_PATH = './texts/long_text.txt'
LONG_PLAIN_TEXT_PATH = './texts/plain_long_text.txt'

# my_actor = Actor(jwt=load_jwt())
# save_jwt(my_actor.jwt)

with open(LONG_TEXT_PATH, 'r') as long_text_file:
    long_text = long_text_file.read()

plain_text = remove_markdown(long_text)
with open(LONG_PLAIN_TEXT_PATH, 'w') as plain_text_file:
    plain_text_file.write(plain_text)

text_lines = preprocess_text(plain_text)
images = create_text_images(text_lines)