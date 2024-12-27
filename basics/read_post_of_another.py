# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from configuration import load_jwt, save_jwt
import yaml
from blue_yonder import Actor, Another
from os import getenv


PROFILE_PATH = './data/another.yaml'  # Path to the profile file

# create your Actor.
my_actor = Actor(jwt=load_jwt())
save_jwt(my_actor.jwt)

# this one will be slower because it uses public endpoints.
another = Another(bluesky_handle=getenv('BLUESKY_OTHER_ACTOR'))

# We will save it in a yaml file.
with open(PROFILE_PATH, 'w') as profile_file:
    yaml.dump(another, profile_file)

# Now let's get the posts of another
posts_of_another = another.authored()

post = posts_of_another[0]

my_actor.read_post(uri=post['uri'], actor=another.did)

...
