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

my_actor = Actor(jwt=load_jwt())
save_jwt(my_actor.jwt)

with open(LONG_TEXT_PATH, encoding='utf-8', mode='r') as long_text_file:
    long_text = long_text_file.read()

plain_text = remove_markdown(long_text)
with open(LONG_PLAIN_TEXT_PATH, 'w') as plain_text_file:
    plain_text_file.write(plain_text)

# plain_text = """Idea
#
#     As the topical analysis or outline in each chapter indicates, the great ideas are not simple objects of thought. Each of the great ideas seems to have a complex interior structure - an order of parts involving related meanings and diverse positions which, when they are opposed to one another, determine the basic issues in that area of thought.
#     The great ideas are also the conceptions by which we think about things. They are the terms in which we state fundamental problems; they are the notions we employ in defining issues and discussing them. They represent the principal content of our thought. They are what we think as well as what we think about.
#     If, in addition to its objects and content, we wish to think about thought itself - its acts or processes - we shall find in the tradition of the great books a number of related terms which indicate the scope of such inquiry. Some of them are: idea, judgment, understanding, and reasoning; perception, memory, and imagination; sense and mind. Here we are concerned with one of these - the idea. It is probably the most elementary of all these related terms, for according to different conceptions of the nature and origin of ideas, the analysis of thought and knowledge will vary. Different positions will be taken concerning the faculties by which men know, the acts and processes of thinking, and the limits of human understanding."""

images = create_text_images(plain_text, output_dir=IMAGES_OF_TEXT_PATH)
my_actor.thread_of_images(paths_and_texts=images)
...